#!/bin/bash

case $1 in 
    list)
        if [ -f tasks.csv ]; then
            awk -F ',' '{printf("%d | %s | %s | %s\n", NR, $1, $2, $3)}' tasks.csv
        else
            echo "No tasks found."
        fi
        ;;
    clear)
        > tasks.csv
        ;;
    *)
        echo "Command Not Supported!"
        ;;
esac
