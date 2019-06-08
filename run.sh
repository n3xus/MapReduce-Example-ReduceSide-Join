#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./run.sh [input_location] [output_location]"
    exit  1
fi

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapreduce.job.name='ReduceSideJoin' \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-r \
-file category_mapper.py \
-mapper category_mapper.py \
-file category_reducer.py \
-reducer category_reducer.py \
-input $1 \
-output $2
