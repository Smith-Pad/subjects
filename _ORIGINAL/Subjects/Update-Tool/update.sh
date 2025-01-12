###########################################################################
#                      The Smith-Pad Updater Tool 
#
#
#               Written by Senal Bulumulle
#              
#   Version 1.0 
###########################################################################
## Displays the banner 
sudo apt update
sudo apt upgrade 
## Run as Root 
sudo -i 
cd /var/www/html/

cd Smith-Pad

git pull 

## Restart 
sudo reboot
