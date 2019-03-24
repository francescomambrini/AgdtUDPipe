import pyconll
from glob import glob
import sys
import os
from tqdm import tqdm

path = os.path.join(sys.argv[1], "*.conllu")
print(path)
fs = glob(path)
with open("pronouns.txt") as inp:
    prons = [l.rstrip() for l in inp.readlines()]

for f in tqdm(fs):
    conll = pyconll.load_from_file(f)
    toks = [t for s in conll for t in s]
    for t in tqdm(toks):
        if t.lemma in prons:
            t.xpos = "p" + t.xpos[1:]
            t.upos = "Pron"
    fname = os.path.split(f)[-1]
    with open("edited/" + fname, "w") as out:
        conll.write(out)
