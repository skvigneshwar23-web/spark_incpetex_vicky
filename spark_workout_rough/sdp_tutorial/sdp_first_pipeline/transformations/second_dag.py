# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# @dp.table(name="src_sales_stream")
# def src_sales_stream():
#     df = spark.readStream.table("sdp_catalog.source.sales")
#     df=df.withColumn("date",to_date(col("date"),"MM-dd-yyyy"))
#     return df

# #Materialized view referring to another view
# @dp.table(name="enr_sales_stream")
# def enr_sales_stream():
#     df = spark.readStream.table("src_sales_stream")
#     df= df.withColumn("revenue",col("revenue")*1.05)
#     return df

# #Materialized view referring to another view
# @dp.table(name="cur_sales_stream")
# def cur_sales_stream():
#     df = spark.readStream.table("enr_sales_stream")
#     df= df.groupBy("date").agg(sum("revenue").alias("revenue"))
#     return df

