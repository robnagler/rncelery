#!/bin/bash
#
# Run three tasks, watching output. You should see STARTED
#
host=127.0.0.1
port=8000
set -e
if [[ ! $(rncelery 2>&1) =~ 'rncelery module' ]]; then
    pip install -r requirements.txt
    pip install -e .
fi
if ! (> /dev/tcp/$host/5672) >& /dev/null; then
    echo 'Please start rabbitmq' 1>&2
    exit 1
fi
if (> /dev/tcp/$host/$port) >& /dev/null; then
    echo "Port $port already in use" 1>&2
    exit 1
fi
celery worker -A rncelery.tasks -l info -Q rncelery &
celery=$!
rncelery service $host $port &
service=$!
trap "kill $celery $service >& /dev/null" SIGINT SIGTERM EXIT ERR
sleep 1
uri=http://$host:$port
for _ in $(seq 3); do
    sleep 1
    curl $uri/start
done
for _ in $(seq 6); do
    sleep 3
    curl $uri/status
done
