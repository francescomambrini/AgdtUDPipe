"""
Usage:
    convert2conllu.py [-n docname -v version -o outputpath -s speakerfile] <filename> <doc-prefix>

Options:
    -n docname       a name for your document
    -v version       the version number [default: 1]
    -o outputpath    path for the output CoNLL-U file
    -s pathtospeak   path to the csv file with the Speaker list. It must have a col. named "Speaker",
                     one row per sentence and the sentences must be in the exact same order as the sents in the
                     treebank file!
"""


from agdt_udpipe.reader import AGLDTConverter
from docopt import docopt
import os


def add_speakers(conll_string, path_to_csv):
    import pyconll
    import pandas as pd

    df = pd.read_csv(path_to_csv)
    speaker_list = df["Speaker"]

    conll = pyconll.load_from_string(conll_string)

    assert len(conll) == len(speaker_list), \
        "List of speakers and list of sentences not in sync ({} speakers, {} sentences)".format(len(speaker_list),
                                                                                               len(conll))
    for c,s in zip(conll, speaker_list):
        c.set_meta("speaker", s)

    return conll

args = docopt(__doc__)

if args["-o"]:
    outpath = args["-o"]
else:
    outpath = os.path.splitext(os.path.basename(args["<filename>"]))[0] + ".conllu"

tb = AGLDTConverter(args["<filename>"], args["<doc-prefix>"], docname=args["-n"], version=int(args["-v"]))

conllu = tb.to_conllu()

if args["-s"]:
    conll = add_speakers(conllu, args["-s"])
    with open(outpath, "w") as out:
        conll.write(out)
else:
    tb.write_to_file(conllu, outpath)





