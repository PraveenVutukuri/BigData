#!/bin/bash

#Bash file to find the count of all tables in a Database to reduce manual work

hive --showHeader=false --outputformat=tsv2 -e"use dbname; show tables;" > /home/ariessupport/dbname.txt

#This will copy the list of tables in that particular database to the text file
#Sending the file as input 

input="/home/ariessupport/dbname.txt"

while IFS= read -r tname
do
count=$(hive --showHeader=false --outputformat=tsv2 -e "select count(*) from dbname.${tname};")
echo $tname,$count >> /home/ariessupport/dbname.csv
#Saving the tablename and counts in csv format, we can save in our required format

done < "$input"

