#!/bin/bash

operator=$1
shift

if [ $# -eq 0 ]; then
  echo "No numbers provided"
  exit 1
fi

res=$1
shift

case $operator in
  +)
    while [ -n "$1" ]; do
      res=$(($res + $1))
      shift
    done
    echo "addition of your two numbers are $res"
    ;;
  -)
    while [ -n "$1" ]; do
      res=$(($res - $1))
      shift
    done
    echo "subtraction of your two numbers are $res"
    ;;
  x)
    while [ -n "$1" ]; do
      res=$(($res * $1))
      shift
    done
    echo "multiplication of your two numbers are $res"
    ;;
  /)
    while [ -n "$1" ]; do
      if [ "$1" -eq 0 ]; then
        echo "Error: Division by zero"
        exit 1
      fi
      res=$(($res / $1))
      shift
    done
    echo "division of your two numbers are $res"
    ;;
  *)
    echo "Invalid operator"
    ;;
esac


#input
#./solution.sh / 128 4 2 2 2
#output
# division of your two numbers are 4