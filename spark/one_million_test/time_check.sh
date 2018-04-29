#!/bin/bash
start_time="$(date -u +%s)"
spark-submit MovieSimilarities1M.py 260
end_time="$(date -u +%s)"

elapsed="$(($end_time-$start_time))"
echo "Total of $elapsed seconds elapsed for process"
