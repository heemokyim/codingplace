from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Config")
sc = SparkContext.getOrCreate(conf = conf)