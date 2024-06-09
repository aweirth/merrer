# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper scripts/mapper.py \
  -reducer scripts/reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py
```
