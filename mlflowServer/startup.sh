#!/usr/bin/env bash


set -e

if [ -z $FILE_DIR ]; then
  echo >&2 "FILE_DIR must be set"
  exit 1
fi


mkdir -p $FILE_DIR && mlflow server \
    --backend-store-uri postgresql://${DBUSER}:${DBPASSWORD}@${DBIP}:${DBPORT}/${DBNAME} \
    --default-artifact-root s3://${AWS_BUCKET}/artifacts \
    --host 0.0.0.0 \
    --port $PORT
