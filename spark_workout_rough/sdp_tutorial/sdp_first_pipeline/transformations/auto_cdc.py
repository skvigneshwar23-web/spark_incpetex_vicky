# from pyspark import pipelines as dp
# from pyspark.sql.functions import *


# #empty streaming table

# dp.create_streaming_table("products_scd2")
# dp.create_streaming_table("products_scd1")

# #streaming view source

# @dp.temporary_view
# def products_source():
#     df=spark.readStream.table("sdp_catalog.source.products")
#     return df

# #scr_type2
# dp.create_auto_cdc_flow(
#   target = "products_scd2",
#   source = "products_source",
#   keys = ["product_id"],
#   sequence_by = col("updated_at"),
#   except_column_list = ["updated_at"],
#   stored_as_scd_type = "2"
# )

# #scd_type2
# dp.create_auto_cdc_flow(
#   target = "products_scd1",
#   source = "products_source",
#   keys = ["product_id"],
#   sequence_by = col("updated_at"),
#   except_column_list = ["updated_at"],
#   stored_as_scd_type = "1"
# )
