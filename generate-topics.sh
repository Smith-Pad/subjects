## generate-topics.sh 




## In this function, we are calculating the 2+2 function 
## which creates a new line 
new_line=$(expr 2 + 30)          
echo "$new_line"



sed -n "${new_line}p" topic_routes.py


echo """
it works

""" >> topic_routes.py