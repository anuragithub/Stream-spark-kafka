#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.2 --jars spark-streaming-kafka-0-10_2.11-2.3.2.jar pyspark-shell'


# In[7]:


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from model import process


# In[14]:


def processrdd(rdd):
    try:
        transactions = rdd.map(lambda p : p['payload'])
        records = transactions.map(lambda p : p.split(","))
        rowRecord = records.map(lambda p : Row(Timestamp=p[0],FeaA=p[1],FeaB=p[2],FeaC=p[3],FeaD=p[4],FeaE=p[5]))
        for x in records.collect():
            print(x)
        for y in records.collect():
            print(y)
        transactionsDataFrame = spark.createDataFrmae(rowRecord)
        output = process(transactionsDataFrame)
        for x in output:
            print(x)
    except:
        pass


# In[8]:


sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")


# In[9]:


ssc = StreamingContext(sc,5)


# In[10]:


kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming', {'connect-test':1})


# In[11]:


parsed = kafkaStream.map(lambda v: json.loads(v[1]))


# In[12]:


parsed.pprint()


# In[15]:


parsed.foreachRDD(processrdd)


# In[16]:


ssc.start()


# In[ ]:


ssc.awaitTermination(timeout=)


# In[ ]:




