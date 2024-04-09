## dependency-install.sh

# @docs
# This script comes along with the documentation so that way you have the understanding 
# how this works. Basically, this script allows the ability to setup and install all
# the dependencies for developing, and maintaining the subjects feature of Smith-Pad. 


# @docs
# In this section, we are going to make an if statement that uses the uname -a command 
# to determine the operating system. If the operating system is Linux, then we are going
# to install the dependencies for developing on Linux. If the operating system is macOS, 
# then we are going to install the dependencies for developing on macOS. 

# @docs
# There are two commands for the if statements. One is the good old' uname -a, 
# as well as the good old' cat /etc/os-release command which brings up a Linux 
# Distribution



# if $(uname -a | grep -q Darwin); then
    
# fi

if $(cat /etc/os-release | grep -q Arch Linux); then
    echo "it works"
    sudo pacman -Syyu --noconfirm
fi


if $(cat /etc/os-release | grep -q Ubuntu); then
    echo "it works"
    sudo apt update -y && sudo apt full-upgrade -y
fi