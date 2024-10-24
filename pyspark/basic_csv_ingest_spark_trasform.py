# Overview
# Ingestion: Read data from a CSV file.
# Transformation: Perform basic cleaning and aggregation on the data.
# Output: Write the transformed data to a new CSV file.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Step 1: Create a Spark session
spark = SparkSession.builder \
    .appName("Sample Data Pipeline") \
    .getOrCreate()

# Step 2: Ingest the data from a CSV file
input_path = "path_to_input_data.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Show the input data
print("Initial Data:")
df.show()

# Step 3: Transformation - Clean and aggregate the data
# Example transformation: Filter, group by, and aggregate sales data by product category

# Filter out null or invalid data
cleaned_df = df.filter(col("Sales").isNotNull())

# Group by category and sum up the sales
aggregated_df = cleaned_df.groupBy("Category").agg(sum("Sales").alias("Total_Sales"))

# Show the transformed data
print("Transformed Data:")
aggregated_df.show()

# Step 4: Output the transformed data to a new CSV file
output_path = "path_to_output_data.csv"
aggregated_df.write.csv(output_path, header=True)

# Step 5: Stop the Spark session
spark.stop()
