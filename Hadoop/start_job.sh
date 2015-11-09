/usr/bin/hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-*streaming*.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input out_file.txt -output out.txt
