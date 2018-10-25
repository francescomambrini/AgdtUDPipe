from perseus_nlp_toolkit.reader import CapitainCorpusReader
import os
from ufal.udpipe import Model, Pipeline, ProcessingError

class Pipe():
    def __init__(self, filename,
                 root=os.path.expanduser("~/cltk_data/greek/canonical-greekLit/data")):
        """
        Arguments
        ---------

        filename : str or list
            path of the file relative to root; can also be a list or a regexp
        root : str
            root folder of the corpus
        """
        self._root = root
        self.filename = filename
        self.corpus = CapitainCorpusReader(root, filename)
        self.sents = self.corpus.sents(self.filename)

    def _to_vertical(self, sents):
        verts = ""
        for s in sents:
            verts += "\n".join(s) + "\n\n"
        return verts

    def run_udpipe(self, path_to_model, sents=None):
        if sents is None:
            sents = self.sents
        verticals = self._to_vertical(sents)
        model = Model.load(path_to_model)
        pipeline = Pipeline(model, "vertical", Pipeline.DEFAULT, Pipeline.DEFAULT, "conllu")
        error = ProcessingError()
        conllu = pipeline.process(verticals, error)

        return conllu

    def to_agdt_conllu(conllu, document_metadata=None):
        """
        Get a rather poor CoNLL-U representation of a text or sentence;
        return an enriched version that contains text, sentence and token metadataself.
        Those metadata include Author, Title (doc); Sentence_ID, span (sentence);
        cts_urn (token).

        The method makes use of the library `pyconll`

        Arguments
        ---------
        conllu : str
            the content of a file or sentence as a string
        document_metadata : dict
            key-pair values of metadata to be parsed
        """
        pass
