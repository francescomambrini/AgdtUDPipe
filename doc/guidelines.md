# Guidelines
This document details the guidelines for morphosyntactic annotation that were followed
for this fork of the [Ancient Greek Dependency Treebank]().

In general, the same annotation rules and principles as the AGDT (v 1.7) will be followed.
We discuss here only the case where some additional details add to be specified,
or where some corrections had to be made to the original annotation.

## Morphological analysis and Lemmatization

### Irregular comparatives and superlatives
Lemmatize irregular (i.e. polytematic) comparatives and superlatives under themselves; the proper
degree (comp. or sup.) must be marked in the appropriate position of the pos-tag.

### Special words

#### ὡς

#### καί

#### μᾶλλον and μάλιστα
μᾶλλον and μάλιστα must be lemmatized under μᾶλλον and μάλιστα, and tagged as comparative
and superlative respectively.

## Syntax

### Special cases

#### Predicative participles with verb in accusative (or indirect cases)
Those constructions are annotated as if the corresponding infinitive clause were used.

E.g. Soph. Aj. 1-2: `δέδορκα σε... θηρόμενον` is annotated with θηρόμενον as OBJ of δέδορκα and
σε as SBJ of the participle.

This annotation allows us to:
1. preserve the correct valency of the main verb (δέδορκα is a bivalent verb, independently of the
  construction chosen)
2. keep the opposition between participial vs acc./inf. construction, which is retrivable from the morphology

#### "Raised" objects
This is a frequent construction in Sophocles, and it is equivalent to structure that can be observed in English as well:

```Can you hear the wind, how it howls```
