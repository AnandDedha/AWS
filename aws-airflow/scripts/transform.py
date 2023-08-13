import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1691969769821 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://airflowoutputtos3bucket/raw/weather_api_data.csv"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1691969769821",
)

# Script generated for node Change Schema
ChangeSchema_node1691969957128 = ApplyMapping.apply(
    frame=AmazonS3_node1691969769821,
    mappings=[
        ("dt", "string", "dt", "string"),
        ("weather", "string", "weather", "string"),
        ("`main.temp`", "string", "temp", "double"),
        ("`main.feels_like`", "string", "feels_like", "double"),
        ("`main.temp_min`", "string", "min_temp", "double"),
        ("`main.temp_max`", "string", "max_temp", "double"),
        ("`main.pressure`", "string", "pressure", "bigint"),
        ("`main.sea_level`", "string", "sea_level", "bigint"),
        ("`main.grnd_level`", "string", "ground_level", "bigint"),
        ("`main.humidity`", "string", "humidity", "bigint"),
        ("`wind.speed`", "string", "wind", "string"),
    ],
    transformation_ctx="ChangeSchema_node1691969957128",
)

# Script generated for node Amazon S3
AmazonS3_node1691970092196 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1691969957128,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://airflowoutputtos3bucket/transformed/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1691970092196",
)

job.commit()
