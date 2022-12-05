#!/bin/ksh

AVAILABILITY_METRIC_NAME=kaiju_CUJ__-__CRM__-__Post__update__to__case_availability
PERFORMANCE_METRIC_NAME=kaiju_CUJ__-__CRM__-__Post__update__to__case_performance
TESTCASEID=33101

TEMPLATES=../TEMPLATES
RUNNING=../RUNNING
OUTPUT=../OUTPUT
SCRIPT=../SCRIPT

rm -rf ../RUNNING/*
rm -rf ../OUTPUT/*

cp ../TEMPLATES/* ../RUNNING/
cd ../RUNNING

for i in `ls -1`
do
echo $i

sed -ie 's/AVAILABILITY_METRIC_NAME/kaiju_CUJ__-__CRM__-__Post__update__to__case_availability/g' $i 
sed -ie 's/TESTCASEID/33101/g' $i
sed -ie 's/PERFORMANCE_METRIC_NAME/kaiju_CUJ__-__CRM__-__Post__update__to__case_performance/g' $i

wait 10
mv $i ../OUTPUT/

done

cd ..
