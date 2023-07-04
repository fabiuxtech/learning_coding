#!/bin/bash
if [[ $(cat ./test.txt) == *10.0* ]]; then
    echo "versione 10"
elif [[ $(cat ./test.txt) == *8.3* ]]; then
    echo "versione 8"
else
    echo "versione non riconosciuta"
    exit 1
fi