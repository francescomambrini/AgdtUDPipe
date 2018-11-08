
from .utils import *
import os
from perseus_nlp_toolkit.reader import AGLDTReader


class AGLDTConverter(AGLDTReader):
    """
    This class is NOT intended as a converter to an official export to UD. It is just a convenience tool to export
    an AGLDT treebank file into the CoNLL-U format
    """

    def __init__(self, filename, docprefix, docname=None, version=1):
        root, fname = os.path.split(filename)
        AGLDTReader.__init__(self, root, fname)
        self.fileid = fname
        self.doc_prefix = docprefix
        self.docname = docname if docname else ".".join(os.path.basename(filename).split(".")[:2]) + ".uagdt"
        self.version = version


    def to_conllu(self):
        c = "# newdoc id = {}\n".format(self.docname)
        tbsents = self.annotated_sents(self.fileid)
        for i,s in enumerate(tbsents):
            sentid = "urn:cite2:uagdt:sentences.v{}:{}_{}".format(self.version, self.doc_prefix, i+1)
            c += "# sent_id = {}\n# speaker = None\n".format(sentid)
            c += "# text = {}\n".format(" ".join([w.form for w in s]))

            for w in s:
                pos = convert_pos(w)
                feats = generate_feats(w)
                lemma = w.lemma if w.lemma else "_"
                id = w.id
                xpos = w.postag if w.postag else "_"
                synt = set_head_deprel_deps(w, s, i+1)
                misc = set_misc(w)

                # id form lemma upos xpos feats head deprel deps misc
                line = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(id, w.form, lemma, pos, xpos, feats, synt, misc)
                c += line

            c += "\n"

        return c



    def write_to_file(self, conllustring, outputpath):
        with open(outputpath, "w") as out:
            out.write(conllustring)
