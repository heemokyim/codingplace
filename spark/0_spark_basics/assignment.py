from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext.getOrCreate(conf=conf)


def parseLine(lines):
    tok = lines.split(',')
    ID = tok[0]
    amount = float(tok[2])
    print(ID,amount)
    return (ID, amount)

lines = sc.textFile(
    "file:/home/ej/codingplace/spark/dataset/customer-orders.csv")
ID_amount = lines.map(parseLine)
sum_amount = ID_amount.reduceByKey(lambda x, y: x+y)

sum_amount.collect()