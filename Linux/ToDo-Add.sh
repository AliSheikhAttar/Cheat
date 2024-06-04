#!/bin/bash

priority="L"
name=""


if [[ $1 == "add" ]]; then
    shift
else
    echo "Invalid command. Use 'add'."
    exit 1
fi


while [[ -n "$1" ]]; do
    case "$1" in
        -t|--title)
            if [[ -n "$2" && ! "$2" =~ ^- ]]; then
                name="$2"
                shift 2
            else
                echo "Option -t|--title Needs a Parameter"
                exit 1
            fi
            ;;
        -p|--priority)
            if [[ "$2" =~ ^[LMH]$ ]]; then
                priority="$2"
                shift 2
            else
                echo "Option -p|--priority Only Accept L|M|H"
                exit 1
            fi
            ;;
        *)
            echo "Invalid option: $1"
            exit 1
            ;;
    esac
done


if [[ -z "$name" ]]; then
    echo "Option -t|--title Needs a Parameter"
    exit 1
fi


task="0,$priority,\"$name\""


touch tasks.csv
echo "$task" >> tasks.csv

