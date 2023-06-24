## Deep Copy

#### 1) Using the Original Table & DDL Command

Steps to Create Deep Copy for Amazon Redshift Copy Table
     
      Using the CREATE Table DDL, create a copy of the parent table.
      Use the INSERT command to insert the data from the parent table to the newly created table. 
      Drop the parent table.
      Use the ALTER TABLE command to rename the new table with the original name.

Let’s understand the above steps with a real-time example. Consider a table of sales that contains the sales records of the products as shown in the code below:

        CREATE TABLE SALES_COPY (
        sales_id int,
        order_id int,
        transaction_id int,
        sales_date datetime,
        sales_transaction double);
      
      INSERT INTO SALES_COPY (SELECT * FROM SALES) 
      
Once the data is completely copied to the SALES_COPY table, drop the original table as shown in the code below:
      
      DROP TABLE SALES;

Rename the new table with the old table as shown in the code below:
      
      ALTER TABLE SALES_COPY RENAME TO SALES;
      
#### 2) Using CREATE TABLE LIKE Command

This method is useful when the create table DDL is not available. This method uses the CREATE TABLE LIKE command that inherits the encoding, distribution key, sort key, etc., from the old table to the new table. It doesn’t inherit the old table’s primary and foreign keys.

Steps to Create Deep Copy for Amazon Redshift Copy Table

        Using the CREATE TABLE LIKE command, create a copy of the parent table.
        Use the INSERT command to insert the data from the parent table to the newly created table. 
        Drop the parent table.
        Let us understand the above steps with a real-time example. Consider a table sales that contains the sales records of the products. 

        CREATE TABLE SALES_COPY (
        sales_id int,
        order_id int,
        transaction_id int,
        sales_date datetime,
        sales_transaction double);
        
        INSERT INTO SALES_COPY (SELECT * FROM SALES) 

Once the data is completely copied to the SALES_COPY table, drop the original table as shown in the code below:

        DROP TABLE SALES;

Rename the new table with the old table as shown in the code below:

        ALTER TABLE SALES_COPY RENAME TO SALES;

#### 3) Amazon Redshift Copy Table: Using a Temporary Table & Truncating Original Table

This method is useful when dependencies are in the parent table and cannot be deleted. Using the temporary table approach improves the performance, but also there is a risk of losing data.

The temporary table is session-based. Hence the temporary table will automatically drop when the current session ends. Therefore this method produces a risk of losing data if anything goes wrong. 

Steps to perform Deep Copy for Amazon Redshift Copy Table
        Use CREATE TABLE AS SELECT command (CTAS) to create a temporary table similar to the parent table. 
        Truncate the parent table.
        Use the INSERT command to insert the data from the temporary table to the parent table.
        Let us understand the above steps with a real-time example. Consider a table of sales that contains the sales records of the products. The code is shown below:
        
        CREATE TEMP TABLE SALES_TEMP AS (SELECT * FROM SALES) 
        TRUNCATE SALES;
        INSERT INTO SALES (SELECT * FROM SALES_TEMP);
        DROP TABLE SALES_TEMP;
