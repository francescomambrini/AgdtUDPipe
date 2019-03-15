"""
Performs sanity checks on the Postag (`conll.xpos`) string

"""

import sys
import logging
import re

nouns = re.compile(r'^n')

# logging.error("that's an error, dawg!")
def check(fun, postag, sent_id, tok_id):
    if fun(postag):
        logging.error("Sent {}, tok {}, {}: {}".format(sent_id,
                                                         tok_id, postag, fun))

def wrong_length(postag):
    if len(postag) != 9:
        return True
    else:
        return False

def empty_values(postag):
