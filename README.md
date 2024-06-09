# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

The mapper.py script reads input text data, tokenizes it into words, and emits key-value pairs where the word is the key and the count is initialized to 1.

The reducer.py script aggregates the counts of the same word emitted by the mapper, producing the final word count result.

Both scripts have been modified to handle contiguous strings of letters instead of treating words as strings separated by spaces.

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
