
from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession

# create SparkContext using standalone mode
#conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .config("spark.driver.extraClassPath", "sqlite-jdbc-3.23.1.jar") \
        .config("spark.executor.extraClassPath", "sqlite-jdbc-3.23.1.jar") \
        .getOrCreate()

sqlContext = SQLContext(sc)

linesRDD = sqlContext.read.format('jdbc').\
     options(url='jdbc:sqlite:example.db',\
     dbtable='ratings',driver='org.sqlite.JDBC').load()

linesRDD.printSchema()
linesRDD.select('UserID','MovieID').show(5)
linesRDD.show(2,truncate= True)
linesRDD.count()
linesRDD.describe().show()
linesRDD.describe('MovieID').show()
# import pdb; pdb.set_trace()