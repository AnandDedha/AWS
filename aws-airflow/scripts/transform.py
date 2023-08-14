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
weather_dyf = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://airflowoutputtos3bucket/raw/weather_api_data.csv"],
        "recurse": True,
    },
    transformation_ctx="weather_dyf",
)

# Script generated for node Change Schema
changeschema_weather_dyf = ApplyMapping.apply(
    frame=weather_dyf,
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
    transformation_ctx="changeschema_weather_dyf",
)


redshift_output = glueContext.write_dynamic_frame.from_jdbc_conf(
    frame=changeschema_weather_dyf,
    catalog_connection="redshift-demo-connection",
    connection_options={"dbtable": "public.weather_data","database":"dev"},
    redshift_tmp_dir = "s3://aws-glue-assets-262136919150-us-east-1/temporary/",
    transformation_ctx = "redshift_output"
)

job.commit()
