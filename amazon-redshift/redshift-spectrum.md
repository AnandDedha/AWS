## Amazon spectrum with examples

Amazon Redshift Spectrum allows you to query data directly from your Amazon S3 data lake using familiar SQL syntax. It leverages the separation of compute and storage, where the data resides in S3, and the processing happens on Redshift Spectrum compute nodes.
To get started, you first need to create an external schema that points to your S3 data. Here's an example of creating an external schema named "my_spectrum_schema" in Redshift:
     
     CREATE EXTERNAL SCHEMA my_spectrum_schema
     FROM DATA CATALOG DATABASE 'my_database'
     IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftSpectrumRole'
     CREATE EXTERNAL DATABASE IF NOT EXISTS;

Next, you can create an external table that defines the schema and structure of the data in S3. Here's an example of creating an external table named "my_spectrum_table":

    CREATE EXTERNAL TABLE my_spectrum_schema.my_spectrum_table (
        column1 integer,
        column2 varchar,
        column3 varchar,
        column4 varchar
       )
     ROW FORMAT DELIMITED
     FIELDS TERMINATED BY '|'
     LOCATION 'https://s3.console.aws.amazon.com/s3/object/datatechbucket?region=us-east-2&prefix=tickitdb/category_pipe.txt';
     
 
 Once the external table is created, you can query it using regular SQL statements. 

