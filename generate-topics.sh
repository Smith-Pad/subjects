## generate-topics.sh 

## This script is used demostrate the ability to create subject generations.






new_line=$(expr 2 + 30)          
echo "$new_line"
sed -n "${new_line}p" topic_routes.py



## This prompts the user to enter a title name
echo "Create title"
read name
echo "$lesson_title!"




echo """
$lesson_title
""" >> topic_routes.py