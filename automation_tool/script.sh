#!/bin/bash

for i in `ls $1`
do
echo $i
  if [[ $i == *".tar.gz"* ]];
	then
	tar -xzvf $1/$i -C $1
	dir=`ls -t $1 | tail -1`
	grep -nrw "ERROR" $1/$dir > $1/fuel_full_error.log
  elif [[ $i == *"filtered"* ]];
	then
	grep -i -A 5 -B 5 "ERROR" $1/$i > $1/fuel_filtered_error.log
  elif [[ $i == *"console"* ]]
	then
	grep -i -A 5 -B 5 "ERROR" $1/$i > $1/console_error.log
  fi;
done;