# How to Use DISTKEY, SORTKEY and Define Column Compression Encoding in Redshift

# Selecting Sort Keys
   When you create a table on Redshift, you can (and should) specify one or more columns as the sort key. You can think of a sort key as a specialized type of index, since Redshift does not have the regular indexes found in other relational databases. Redshift stores data on disk in sorted order according to the sort key, which has an important effect on query performance.

   You choose sort keys based on the following criteria:

   1. If recent data is queried most frequently, specify the timestamp column as the leading column.
   2. If you frequently filter by a range of values or a single value on one column, that column should be the sort key.
   3. Columns frequently used in joins should be used as the sort key
    Here are some examples of defining the sort key:
 
     -- sale_date is the timestamp column
     CREATE TABLE sales (
     sale_id BIGINT NOT NULL PRIMARY KEY,
     sale_date timestamp NOT NULL SORTKEY,
     <other colums>
     );

     -- use the SORTKEY table attribute keyword to create a multi-column sort key
     -- In this case searches are done frequently by the location columns,
     -- so state and city are part of sort key
     CREATE TABLE dim_customers (
       ... <some columns>...
       state VARCHAR,
       city VARCHAR
     )
    SORTKEY (state, city);

# Selecting Distribution keys

EVEN: In this style, data is distributed evenly across compute nodes without any specific column-based distribution. It is suitable for tables where distribution is not critical to query performance or when a table is not used in queries with joins or when there is no clear choice of distribution method between the next two.

KEY: The distribution key is chosen based on one or more columns with high cardinality or frequently used in join conditions. Rows with the same values in the distribution key are co-located on the same compute node, which can enhance query performance for join operations.

ALL: With this style, a complete copy of the table is stored on each compute node, ensuring that all data is available locally on every node. It is useful for small dimension tables or tables used in lookup operations.


    -- Specifying a column as DISTKEY automatically sets distribution style to KEY
    CREATE TABLE sales (
      sale_id BIGINT NOT NULL PRIMARY KEY,
      sale_date timestamp NOT NULL SORTKEY,
      customer_id int DISTKEY,
      amount float
     );

    -- Use DISTSTYLE table attribute to set it to ALL
    CREATE TABLE atrribute_lookup (
       attribute_id INT NOT NULL PRIMARY KEY,
       attribute_name VARCHAR
       )
     DISTSTYLE ALL;
