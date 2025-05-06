"""
docker exec -it dsa-pyspark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  /opt/spark/apps/get-users-json.py
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .getOrCreate()

df_users = spark.read.json("./storage/users.json")
count = df_users.count()
df_users.show(3)

spark.stop()
