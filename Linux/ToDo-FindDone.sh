#!/bin/bash

case $1 in 
    find) 
        shift
        while [ -n "$1" ]; do
            search_term=$1
                grep -n "$search_term" tasks.csv | while IFS=: read -r line_number line; do
                echo "$line" | awk -F ',' '{printf("%d | %s | %s | %s\n", '$line_number', $1, $2, $3)}'
            done
            shift
        done
        ;;
    done)
        shift
        while [ -n "$1" ]; do
            task_id=$1
            awk -v task_id="$task_id" -F ',' 'BEGIN {OFS = FS} 
                NR == task_id {$1 = 1} {print}' tasks.csv > tasks.tmp && mv tasks.tmp tasks.csv
            shift
        done
        ;;
    *)
        echo "Command Not Supported!"
        ;;
esac