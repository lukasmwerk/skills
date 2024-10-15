# **Apache Cassandra** - Architecture Overview

[back to README](/README.md)

## Coordinator

The coordinator is a special node that manages entire request paths, essentially a proxy for the application and the cassandra worker nodes.

## Partitioner

Nodes in a cluster are assigned ranges of tokens to be used in a consistent hashing strategy. Each node may have many small ranges to simulate virtual nodes, remedying uneven token ranges especially among failures, scaling, varying performance across machines.

### Token Ring

Cassandra uses a token ring (just like dynamo) to walk nodes. It hashes the key