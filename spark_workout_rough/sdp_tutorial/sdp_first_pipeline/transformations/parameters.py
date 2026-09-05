from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Commented out the dynamic table creation approach because:
# 1. Decorators inside for loops don't work in SDP (evaluated at module load time)
# 2. The 'list' config parameter was not set in pipeline settings
# 3. All function definitions had the same name 'table()' causing conflicts

# If you need multiple tables, define them statically like this:

@dp.table(name="table_1")
def table_1():
    df = spark.readStream.table("sdp_catalog.source.sales")
    return df

@dp.table(name="table_2")
def table_2():
    df = spark.readStream.table("sdp_catalog.source.sales")
    return df

@dp.table(name="table_3")
def table_3():
    df = spark.readStream.table("sdp_catalog.source.sales")
    return df
