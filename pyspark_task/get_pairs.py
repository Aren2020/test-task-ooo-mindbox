from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def get_product_category_pairs_with_no_category(spark, products_df, categories_df, product_category_df):
    # left join
    product_category_pairs = products_df.join(product_category_df, 'product_id', 'left') \
                                        .join(categories_df, 'category_id', 'left') \
                                        .select(products_df['product_name'], categories_df['category_name']) \
                                        .withColumnRenamed('product_name', 'Product') \
                                        .withColumnRenamed('category_name', 'Category')
    
    # products without categories
    products_with_no_category = products_df.join(product_category_df, 'product_id', 'left_anti') \
                                           .select(products_df['product_name']) \
                                           .withColumnRenamed('product_name', 'Product') \
                                           .withColumn('Category', when(col('Product').isNull(), 'No Category').otherwise(None))
    
    result_df = product_category_pairs.union(products_with_no_category)
    return result_df

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()
    
    products_df = spark.read.csv("pyspark_task/csv/products.csv", header = True, inferSchema = True)
    categories_df = spark.read.csv("pyspark_task/csv/categories.csv", header = True, inferSchema = True)
    product_category_df = spark.read.csv("pyspark_task/csv/product_category.csv", header = True, inferSchema = True)
    
    result = get_product_category_pairs_with_no_category(spark, products_df, categories_df, product_category_df)
    
    # Show the result dataframe
    result.show()
