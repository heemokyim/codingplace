from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def loadMovieNames():
    movieNames = {}
    with open('ml-100k/u.item') as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
            
    return movieNames

def parseInput(line):
    fields = line.split()
    return Row(movieID = int(fields[1]), rating = float(fields[2]))

if __name__ == '__main__':
    spark = SparkSession.builder.appName('Popular Movies').getOrCreate()
    
    movieNames = loadMovieNames()
    
    lines = spark.sparkContext.textFile('hdfs:///user/maria_dev/ml-100k/u.data')
    movies = lines.map(parseInput)
    
    # Row object를 받아서 DataFrame을 만든다.
    movieDataset = spark.createDataFrame(movies)
    
    # movieID로 group해서 rating을 avg내라
    # (movieID, average rating)
    avg_ratings = movieDataset.groupBy('movieID').avg('rating')
    
    # moveID로 group해서 rating이 몇개나 있는지 count해라
    # (movieID, that movie's counts)
    counts = movieDataset.groupBy('movieID').count()
    
    avg_counts = counts.join(avg_ratings, 'movieID')
    
    topTen = avg_counts.orderBy('avg(rating)').take(10)
    
    for movie in topTen:
        print(movieNames[movie[0]], movie[1], movie[2])