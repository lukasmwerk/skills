# **Apache Cassandra** - The original paper

*   [Paper File Link](/cassandra_paper.pdf)
*   [Paper Online Link](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf)

_Note: the paper was published in 2009, there are notable differences in the latest releases but the concepts are the same and the insights are relevant._

---

### Data Model

*   **Table** : A distributed multi-dimensional map indexed by a key.
*   **Row Key** : A string with no size restriction.
*   **Value** : A highly structured object.
*   **Columns** : Grouped into column families (simple and super/nested).
*   Operations under each row key is atomic per replica.

### API

*   insert(table; key; rowMutation)
*   get(table; key; columnName)
*   delete(table; key; columnName)