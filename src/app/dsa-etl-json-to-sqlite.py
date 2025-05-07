""" 
****** Auxiliary code *******
Create database to store DSA ETL data
python /m/projects/github/pyspark-kafka-dsa/src/auxiliary_code/project01/dsa-cria-database.py
---

Geranate random data to be used in the ETL process
python /m/projects/github/pyspark-kafka-dsa/src/auxiliary_code/project01/dsa-gera-users-json.py
"""

"""
docker exec -it dsa-pyspark-master /opt/spark/bin/spark-submit \
    --jars /opt/spark/storage/jars/sqlite-jdbc-3.44.1.0.jar \
    --master spark://spark-master:7077 \
    --deploy-mode client \
    /opt/spark/apps/dsa-etl-json-to-sqlite.py 

ou

docker exec -it dsa-pyspark-master ./bin/spark-submit \
    --jars ./storage/jars/sqlite-jdbc-3.44.1.0.jar \
    --deploy-mode client \
    ./apps/dsa-etl-json-to-sqlite.py 
"""

# Importing necessary libraries
import  os
from pyspark.sql import SparkSession, types
from pyspark.sql.functions import col, regexp_replace

spark = SparkSession.builder \
    .appName("ETL JSON to SQLite") \
    .getOrCreate()

# Define o schema de dados
schema = types.StructType([
    types.StructField("uuid", types.StringType(), True),
    types.StructField("name", types.StringType(), True),
    types.StructField("age", types.IntegerType(), True),
    types.StructField("birth_date", types.StringType(), True),
    types.StructField("cpf", types.StringType(), True),
    types.StructField("nationality", types.StringType(), True),
    types.StructField("email", types.StringType(), True),
    types.StructField("phone", types.StringType(), True),
    types.StructField("salary", types.IntegerType(), True),
    types.StructField("city", types.StringType(), True),
    types.StructField("profession", types.StringType(), True),
    types.StructField("marital_status", types.StringType(), True),
    types.StructField("gender", types.StringType(), True),
    types.StructField("active", types.BooleanType(), True)
])

# Read JSON file from storage
df_dsa = spark.read.schema(schema).json("./storage/dsa-usuarios.json")

# Remove columns will be not used in the database
df_dsa_not_used_in_db = df_dsa.drop("age","birth_date","nationality","phone","marital_status","gender","active")

df_final = df_dsa_not_used_in_db.filter(
    (col("age") >= 35) &
    (col("city") == "Natal") &
    (col("salary") <= 7000)
)

# Check if dataframe is empty
if df_final.rdd.isEmpty():
    print("DataFrame is empty. No data to write to SQLite.")
else:
    # Clean the data removing special characters from the 'name' column
    df_cleaned = df_final.withColumn("name", regexp_replace(col("name"), "@", ""))

    # DB Path
    db_path =  os.path.abspath("./storage/dsa-usuarios.db")

    # DB URL for JDBC
    db_uri = f"jdbc:sqlite://{db_path}"

    # Define the JDBC driver
    jdbc_properties = {"driver": "org.sqlite.JDBC"}

    # Check if the table already exists
    try:
        spark.read.jdbc(url=db_uri, table="dsa_usuarios", properties=jdbc_properties)
        write_mode = "append"
    except Exception as e:
        write_mode = "overwrite"
        print(f"Table does not exist. Creating new table: {e}")

    # Load the DataFrame into database
    df_cleaned.write.jdbc(
        url=db_uri,
        table="dsa_usuarios",
        mode=write_mode,
        properties=jdbc_properties
    )

    print(f"Data loaded into database successfully in 'dsa_usuarios.db' using mode '{write_mode}'.")

spark.stop()