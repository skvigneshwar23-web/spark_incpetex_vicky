from pyspark import pipelines as dp
from pyspark.sql.functions import *

#creating empty streaming table
dp.create_streaming_table("total_sales")


#appedning north sales to the total_sales

@dp.append_flow(target="total_sales")
def north_sales():
    df=spark.readStream.table("sdp_catalog.source.sales_north")
    return df

#appedning south sales to the total_sales
@dp.append_flow(target="total_sales")
def south_sales():
    df=spark.readStream.table("sdp_catalog.source.sales_south")
    return df
