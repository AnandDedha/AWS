---
marp: true

---


Amazon Redshift does not reclaim free space automatically. Such available space is created whenever you delete or update rows on a table. This process is a design choice inherited from PostgreSQL and a routine maintenance process that we need to follow for our tables to maximize the utilization of our Amazon Redshift cluster.

So by running a Vacuum command on one of our tables, we reclaim any free space that is the result of delete and update operations. At the same time, the data of the table get sorted.

This way, we end up with a compact and sorted table, which are useful for the performance of our cluster.

If you wonder why the update operations are also included together with deletes, this happens because behind the scenes an UPDATE command is the combination of a DELETE command, where the old row is first deleted, and then an INSERT command where the new row is inserted.

During a DELETE command, a row is marked as deleted but not removed. Additionally, the query processor has to scan all the rows, including those marked as deleted. So it is easy to understand that keeping deleted rows on a table costs additional process and thus slow down your queries.

In extreme situations, you might even end up with queries that may timeout due to the extra overhead the deleted but not reclaimed space might add.


https://www.rudderstack.com/guides/vacuum-amazon-redshift/
