# **Apache Cassandra**

Cassandra is an open source NoSQL distributed (P2P) database designed for large scalable industry-grade viability.

_Inspired by Amazon's DynamoDB and Google's Big Table_

Pros:

*   **High throughput** : Cassandra can handle large volumes of writes, and is great for messaging, time-series/streaming, logging, analytics, IoT.
*   **Scalable** : Distributed design, built to scale well.
*   **Wide-Column Store** : Works well for chronological data.
*   **No single point of failure** : Can survive large outages, even at the scale of datacenters, fault tolerant.
*   **Horizontally Scalable** : Great for supplementation and real-time scaling purposes.

Cons:

*   Not for small datasets
*   **Lower Read Speed** : Distributed nature does not support high-speed reads.
*   **Sophisticated Queries** : Complicated queries and cross-table joins are not suited for cassandra, complex analytics workloads won't do well.
*   **Transactions** : Not necassarily ACID compliant, not consistency optimized, not ideal for transactional data, use a relational solution instead.
*   **Administration Load** : Not the most straight forward to administer, deploy, maintain.
*   **No Relational Schema** : Relational, highly-connected or flexible schemas shouldn't use Cassandra.

---

**Quick Links**

*   [Case Studies](https://cassandra.apache.org/_/case-studies.html)
*   [Official Documentation](https://cassandra.apache.org/doc/latest/)
*   [Official Resources](https://cassandra.apache.org/_/resources.html)
*   [Blog](https://cassandra.apache.org/_/blog.html)
*   [Best Buy Cassandra as Supplemental Scaling](https://www.slideshare.net/slideshow/cassandra-and-riak-at-bestbuycom/30239678)

**Notes**

*   [Architecture](/architecture.md)

**Experience**

*   High througput writes on a small cluster for an ecommerce application, was able to write a large volume of commerce and transaction data efficiently.