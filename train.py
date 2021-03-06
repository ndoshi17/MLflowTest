import os
import sys
import mlflow
from mlflow import log_metric, log_param, log_artifact



def main():
    param1 = sys.argv[0]
    # Log a parameter (key-value pair)
    with mlflow.start_run():

        log_param("param1", param1)

    # Log a metric; metrics can be updated throughout the run
        log_metric("foo", 1)
        log_metric("foo", 2)
        log_metric("foo", 3)

    # Log an artifact (output file)
    #with open("output.txt", "w") as f:
        #f.write("Hello world!")
    #log_artifact("output.txt")