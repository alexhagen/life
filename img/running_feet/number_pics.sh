#!/bin/sh
num=1
for file in *.jpg; do
  cp "$file" "$(printf "%u" $num).jpg"
  sips -Z 990 "$(printf "%u" $num).jpg"
  let num=$num+1
done
