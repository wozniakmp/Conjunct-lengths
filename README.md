
# Conjunct Lengths in English, Dependency Length Minimization, and Dependency Structure of Coordination

This is a project conducted together with Adam Przepiórkowsi PhD from Institute of Computer Science Polish Academy of Sciences and University of Warsaw.

There are 2 modules containing functions used in the project.

### Coord

The most important function of **Coord** is *get_head(tree, t, coord_pos)*. It returns the governor of a coordination in NLTK phrase-structure tree.

Other functions of the module include e.g.:
- a function calculating syntactic complexity of a tree
- a function returning the parent of given node
- a function returning raw text from a given subtree


### Syllables

This is a module containing functions used to calculate syllables in a sentence defined as a phrase-structure tree. Calculations are based on entries from a CMUdict or some regex-based heuristics if a word was not found there. Numbers were transformed into lexical forms using Inflect library.
