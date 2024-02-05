import sys
import boto3
from datetime import datetime
from awsglue.transforms import *
from delta.tables import *
from pyspark.sql.functions import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job