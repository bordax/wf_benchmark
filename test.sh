#!/bin/bash
for port in '8080' '8000' '5000'
do
    if [[ $1 == "--post" ]]; then
        autocannon http://localhost:$port/users -d 10 -c 30 -m POST --body '{"name":"joao","age":5,"location":"sao carlos"}' -H "Content-Type":"application/json"
    elif [[ $1 == "--get" ]]; then
        autocannon http://localhost:$port/ -d 10 -c 30
    else
        echo "Use one of the options: --post, --get"
        break
    fi
done