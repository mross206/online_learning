import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

#create a spark session
spark = (SparkSession
         .builder
         .appName("SparkSQLExampleApp")
         .getOrCreate()
         )

#path to data set
csv_file = "/content/coursera_pyspark_Superstore.csv"

df = spark.read \
    .format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(csv_file)

#create a temporary view to run SQL queries against
#df.createOrReplaceTempView("u")

#explore/sample dataset
df.printSchema()
df.show()


# identify product sub-category with highest sales quantity
highest_sales_quantity = df.groupBy('Sub-Category') \
                           .agg(sum('Quantity').alias('total_quantity')) \
                           .orderBy(col('total_quantity').desc()) \
                           .first()

if highest_sales_quantity:
  print("Sub-category with the most total quantity: ")
  print(highest_sales_quantity['Sub-Category'], ":", highest_sales_quantity['total_quantity'])
else:
  print("No data found in the DataFrame.")


# identify product category with highest profit
highest_profit_category = df.groupBy('Product Name') \
                            .agg(sum('Profit').alias('total_profit')) \
                            .orderBy(col('total_profit').desc()) \
                            .first()

if highest_profit_category:
  print("Product with the most total profit:")
  print(highest_profit_category['Product Name'], ":", highest_profit_category['total_profit'])
else:
  print("No data found in the DataFrame.")


#identify top 10 list of most valuable customers based on profit
top_10_customers = df.groupBy('Customer Name') \
                   .agg(sum('Profit').alias('total_profit')) \
                   .orderBy(col('total_profit').desc()) \
                   .limit(10)

if top_10_customers.count() > 0:
  print("Top 10 Customers with Most Profit:")
  top_10_customers.show()
else:
  print("No data found in the DataFrame.")


#identify state with highest number of orders by quantity
highest_order_total_by_state = df.groupBy('State') \
                            .agg(sum('Quantity').alias('total_quantity')) \
                            .orderBy(col('total_quantity').desc()) \
                            .first()

if highest_order_total_by_state:
  print("State with the most total quantity:")
  print(highest_order_total_by_state['State'], ":", highest_order_total_by_state['total_quantity'])
else:
  print("No data found in the DataFrame.")
