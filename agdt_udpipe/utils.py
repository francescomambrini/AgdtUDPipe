from perseus_nlp_toolkit.utils import Sentence, Word, Artificial, Morph
import logging

logger = logging.getLogger()

def convert_pos(w):
    pos = "X"
    if w.postag:
        m = Morph(w.postag)
        pos = m.pos.title()
    return pos



def generate_feats(w):
    morphfeats = "_"
    if w.postag:
        m = Morph(w.postag)
        feats = []
        for k,i in m.full.items():
            if i != '-':
                feats.append("{}={}".format(k.title(), i.title()))
        if feats:
            morphfeats = "|".join(feats)

    return morphfeats


def set_misc(w):
    misc = "_"
    if w.cite:
        misc = "cite=" + w.cite

    if isinstance(w, Artificial):
        misc = "type=Artificial"
    return misc

def _is_governed_by_artificial(t, tokens):
    h = t.head
    for tok in tokens:
        if tok.id == h:
            if isinstance(tok, Artificial):
                return True
            else:
                return False


def set_head_deprel_deps(w, sent, sentindex):
    true_head = _find_true_head(w, sent, sentindex)
    deprel = w.relation
    deps = "_"

    if w.head != true_head:
        # it means the head is an Artificial
        deprel = "ExD"
        deps = "{}:{}".format(w.head, w.relation)

    # what do we do with the artificial nodes themselves? We attach them to the root
    if isinstance(w, Artificial):
        true_head = '0'
        deps = "{}:{}".format(w.head, w.relation)

    return "{}\t{}\t{}".format(true_head, deprel, deps)


def _find_true_head( t, tokens, sentindex):
    """
    Checks a node's head. If this head is an Arificial then it (recursively) searches for the first
    non-artificial node that is at the root of the subtree.
    Otherwise, it simply returns the original node's head

    Parameters
    ----------
    t : namedtuple
        Word or Artificial node
    tokens : list
        the full sentence, as a list of Artificial or Word

    Returns
    -------
    str : the id of the first Word element governing the whole structure

    """
    arts_ids = [tok.id for tok in tokens if isinstance(tok, Artificial)]
    h = t.head
    if h not in arts_ids:
        return h
    else:
        for tok in tokens:
            if h == tok.id:
                # then we found the target immediate head
                true_head = tok.head
                # now let's check if th is an artificial
                if true_head in arts_ids:
                    try:
                        true_head = _find_true_head(tok, tokens, sentindex)
                    except RecursionError:
                        true_head = h
                        logger.error("Recursion error in Sentence {}, Token {}".format(sentindex, t.id))
        return true_head