#!/bin/bash
#
# Run three tasks, watching output. You should see STARTED
#
set -e
if [[ ! $(type -p rncelery) ]]; then
    pip install -e .
fi
if ! : > /dev/tcp/localhost/5672; then
    echo 'Please start rabbitmq' 1>&2
    exit 1
fi
celery worker -A rncelery.tasks -l info -Q rncelery &
celery=$!
rncelery service &
service=$!
trap "kill $celery $service >& /dev/null" SIGINT SIGTERM EXIT ERR
sleep 1
uri=http://127.0.0.1:8000
for _ in $(seq 3); do
    sleep 1
    curl $uri/start
done
for _ in $(seq 6); do
    sleep 3
    curl $uri/status
done
