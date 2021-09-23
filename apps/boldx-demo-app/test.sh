#! /usr/bin/env bash

HOST="http://localhost:8080"


function make_requests() {

  for ROUTE in "${ROUTES[@]}"
  do

    response=$(curl --write-out '%{http_code}' --silent --output /dev/null $HOST/api/$ROUTE)
    echo $HOST/api/$ROUTE
    echo status_code: $response
    echo "---"
    sleep 1
  done
}



ROUTES=('hello' 'bad-request' 'forbidden' 'unauthorized' 'error')
while true; do
  ROUTE=${ROUTES[RANDOM%6]}
  response=$(curl --write-out '%{http_code}' --silent --output /dev/null $HOST/api/$ROUTE)
  echo $HOST/api/$ROUTE
  echo status_code: $response
  sleep 0.5
  #make_requests;
done

