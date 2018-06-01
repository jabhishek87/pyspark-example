# pyspark-example
:sparkles: :sparkles: :sparkles: some pyspark python wrapper example :sparkles: :sparkles: :sparkles:


Resources
Pyspark Documentation
- http://spark.apache.org/docs/latest/api/python/index.html

Movie rating datasets
- https://grouplens.org/datasets/movielens/

sql functions and calls
- https://www.analyticsvidhya.com/blog/2016/10/spark-dataframe-and-operations/


Steps to download data
======================

```
# download datasets and unzip
$ ./setup.sh -d
$ ./setup.sh -u
$ ./setup.sh -r
```

view rating histograms
====

it will read ml-20m/ratings.csv which has 


| UserID | MovieID | ratings | UnixTimestamps |
| ------ | ------- | ------- | -------------- |
| 138493 | 60816   | 4.5     | 1259865163     |



```
$ python generate_ratings_histogram.py

#load data into sqlitedb
python import_csv.py

# run sql spark
$ python spark_sql.py
```



