from pyspark import SparkConf, SparkContext

def loadMovieNames():
    movieNames = {}
    
    with open('ml-100k/u.item') as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
            
    return movieNames

def parseInput(line):
    fields = line.split()
    return (int(fields[1]), (float(fields[2]),1.0))

if __name__ == '__main__':
    conf = SparkConf().setAppName('WorstMovies')
    sc = SparkContext(conf=conf)
    
    movieNames = loadMovieNames()
    
    lines = sc.textFile('YOUR_PATH_HERE')
    
    
    # (movieID, (rating, 1.0))
    movieRatings = lines.map(parseInput)
    
    # (movieID, (total sum of ratings, total counts of rating))
    total_count = movieRatings.reduceByKey(lambda movie1, movie2: (movie1[0]+movie2[0]), (movie1[1]+movie2[1]))
    
    # (movieID, average rating)
    average_rating = total_count.mapValues(lambda x: x[0]/x[1])
    
    # Sort average ratings
    sorted_rating = average_rating.sortBy(lambda x: x[1])
    
    print(sorted_rating.collect())