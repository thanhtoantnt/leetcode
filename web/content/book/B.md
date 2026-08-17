Sets, relations, functions, graphs, and trees — the vocabulary appendix. Skim-level familiarity assumed by every chapter; the worth-noticing bits:

## Sets and relations

Equivalence relations (reflexive, symmetric, transitive) *partition* their set into equivalence classes — which is exactly why union-find (Ch. 21) maintains a partition, and why "connected" is an equivalence relation on undirected graphs but *not* on directed ones (asymmetry breaks transitivity... reachability is only a preorder). Partial orders → topological sorting (Ch. 22); total orders are what comparison sorts (Ch. 8) presuppose.

## Functions

Injective/surjective/bijective — the words for counting arguments. The pigeonhole principle is the appendix's one-liner with teeth: hash collisions (Ch. 11: |U| > m means collisions are unavoidable), bound arguments, and every "must exist two identical..." interview prompt.

## Graphs — the free lessons

- The handshaking lemma: Σ deg(v) = 2|E| — undirected degree sums are even; the basis of many parity arguments.
- Every DAG has a topological order; a directed graph is acyclic ⟺ it has one (the cycle/back-edge equivalence DFS uses).
- The contraction property: undirected graph components form equivalence classes; directed strong connectivity is an equivalence relation whose classes are the SCCs (Ch. 22.5).
- Representations (adjacency list/matrix) tie directly to Ch. 22.1.

## Trees

The characterizations worth remembering: an undirected graph is a tree ⟺ connected with |V|−1 edges ⟺ connected and acyclic ⟺ unique simple paths between vertex pairs. The last one is why BFS trees and DFS trees behave (unique paths), and why MST correctness proofs can talk about "the path in T between u and v" (Ch. 23's exchange argument).

Free trees, rooted trees, ordered trees — and the fact that "tree" in algorithms almost always means rooted-and-ordered once recursion gets involved.
