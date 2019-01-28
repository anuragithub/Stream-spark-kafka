# Stream-spark-kafka

Requirements for running the code:
## kafka_2.10-0.10.2.2
## spark-2.3.2-bin-hadoop2.7
## Python requirements
## train.csv, test.csv to be present 

Steps to run:
## Make configurations related to kafka:
  ### Go to the config folder, open “connect-file-source.properties” file and edit the file value to the file name from which we want import. 
  ### Change this file to test.txt.
  ### Change the topic on which these import will be broadcasted, make to default connect-test topic. 
  ### Modify the “connect-file-sink.properties” file to let kafka know where to sink all the incoming data. Change the file value to test.sink.data.
## Run configurations for kafka:
  ### bin/zookeeper-server-start.sh config/zookeeper.properties
  ### bin/kafka-server-start.sh config/server.properties
  ### bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
## Python configurations
  ### Create virtualenv and from env make "pip install -r requirements.txt"
## SPark configurations
  ### Download spark and set environment variables $SPARK_HOME and $PYTHONPATH using export PATH=$PATH:/usr/local/spark/bin

## Runnig the code:
  ### Start by executing ParseData.py after starting kafka.
  ### Then after altering the input file and output file fileGen.py execute FileGen.py as well.(input file : actual csv file for data, output file : source file for kafka



## Discussion Questions:
  A1) The approach was to build your model and then save it in filesystem and use it for making prediction. The kafka file connector is being used
      for publishing changes of file into a sink file whose topic in turn is being connected to by Spark streaming which processes the input and
      returns prediction for each input row by loading the model.
  A2) Model accuracy is 99.08%.
  A3) Performance is bit slow as tested on 4 core CPU with no GPU. The complexity is manging the batch interval, window length and sliding interval
  for spark streaming.
  A4) Model's perfomance and runtime performance can be further improved if had time.
