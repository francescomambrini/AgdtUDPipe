"""
This is just a script! It is designed to work with Homer. You might want to adjust how the CTS_URN reference is unpacked:
now it is designed to work with book and line number; you might run into texts that have different citation schemes.

"""

import pyconll
from lxml import etree
from pyCTS import CTS_URN
from tqdm import tqdm

conllpath = "/home/francesco/PycharmProjects/AgdtUDPipe/data/v1/tlg0012.tlg001.perseus-grc1.tb.conllu"
tei_path = "/home/francesco/Documents/work/Nextcloud/Documents/Projects/Homer_Speakers/tlg0012.tlg001.perseus-grc2.xml"
outname = "tlg0012.tlg001.perseus-grc1.tb_SPEAKER.conllu"

tei = etree.parse(tei_path)
conll = pyconll.load_from_file(conllpath)

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

def guess_speaker(sent, tei_file):
    u = CTS_URN(list(sent[0].misc["cite"])[0])
    book,line = u.passage_component.split(".")

    # retrieve the line in TEI
    xp = "//tei:div[@subtype='Book' and @n='{}']/descendant::tei:l[@n='{}']".format(book, line)
    l = tei_file.xpath(xp, namespaces=ns)[0]
    p = l.getparent()
    try:
        speaker = p.attrib["who"]
    except KeyError:
        speaker = "Narrator"

    sent.set_meta("speaker", speaker)


for sent in tqdm(conll):
    guess_speaker(sent, tei)

with open(outname, "w") as out:
    conll.write(out)

