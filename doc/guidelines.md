# Guidelines
This document details the guidelines for morphosyntactic annotation that were followed
for this fork of the [Ancient Greek Dependency Treebank]().

In general, the same annotation rules and principles as the AGDT (v 1.7) will be followed.
We discuss here only the case where some additional details add to be specified,
or where some corrections had to be made to the original annotation.

## Morphological analysis and Lemmatization

### Pronouns

In contrast to other POS (like adjectives or nouns), pronouns belong to a close class, but it is not always easy to to assign the different lemmata to this or that category. Bear in mind that POS does not register syntactic annotation, thus proper pronouns (like ὅδε) used adjectively are *not* annotated as adjectives.

Thus, the list of pronouns varies considerably, depending on whether one considers syntactic, semantic or morphological (i.e. based on flexion) aspects to make the distinction.

Our list and classification is based on that of Kuhner and Blass (pp. 579-ss), with some minor modifications (marked with *):

1. personal pronouns: ἐγώ, σύ, ἡμεῖς, ὑμεῖς, σφεῖς with various peculiar forms for the other persons and cases (ἕ, νῶϊ, οὗ etc.)

2. possessive pronouns: ἐμός, σός, ἡμέτερος, ὑμέτερος, (ἑ)ὅς, νωΐτερος, σφέτερος

3. reflexive pron.: ἐμαυτοῦ, σαυτοῦ, ἑαυτοῦ

4. reciprocal pron.: ἀλλήλων

5. demonstrative pronouns:
   * ὁ, ὅδε
   * αὐτός
   * οὗτος, ἐκεῖνος
   * ἄλλος
   * τόσος, τοσόσδε, τοσοῦτος
   * τοῖος, τοιόσδε, τοιοῦτος
   * τήλικος, τηλικόσδε, τηλικοῦτος

6. interrogative pronouns:
   * τίς
   * πότερος*
   * πόσος
   * ποῖος
   * πηλίκος

7. relative-interrogative pron:
   * ὅς
   * ὁποῖος
   * ὅσος, ὁπόσος
   * ὁπότερος (vedi K-B par 157.8)
   * ἡλίκος
   * ὁπηλίκος

8. indefinite and interrogative pronouns:
   * τις
   * ὅστις
   * δεῖνα
   * ἑκάτερος, ἕκαστος (vedi K-B par 157.8)
   * ποσός
   * ποιός

Note that K-B correctly identifies a class of pronominal adverbs (together with pronominal adjectives and nouns); however they also rightly state that these pronouns behave more as adverbs and we will annotate them as such.

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
