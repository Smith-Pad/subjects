# subjects

Smith-Pad Subjects engages students with tactile learning.

## Dependencies

- python-flask

## Installation Instructions

- `sudo pacman -S python-flask`
- `pip install flask`
- `sudo pacman -S dialog`
- `brew install dialog`

## Debugging and Compiling SASS/SCSS Files on macOS

In this section, we are going to be talking about some ways to setup,
install, debug, and compile SASS on macOS

1. Make sure you have Brew installed on macOS

2. `brew install sassc`

3. Then you make sure that sassc does work by using this command: `sassc`

## Debugging and Compiling SASS/SCSS Files on Windows

In this section, we are going to be talking about some ways to setup,
install, debug, and compile SASS on Windows. On Windows the implementation
of installing dependencies to get SASS to work may be different. 

So here are the instructions on how to do it.

On Node.js implementation, here are the steps to install SASS. 

1. Download the Node.js package for Windows from the Website

2. Make sure the node.js works by using CMD or Powershell

3. In the CMD or Powershell use this command: `npm install -g sass`

4. In the CMD or Powershell, use this command: `sass` to make sure it works properly.

## In other news

- Creating Scripts to make it more efficient to maintain the Subjects feature of the Smith-Pad platform 

## Experimental Instructions

In this section, these instructions are considered experimental, so these instructions,
may not be accurate in a sense.

### Topic Route Test.

In this subsection, we are going to be talking about the experimental feature called 
Topic Route Test. Topic Route Test allows the ability to test out dynamic features 
when it comes to Subjects Generation.

For the test, the script that is used for the topic route is based on shell scripting.
like BASH, which has user prompts what will generate a lesson plan and generate it 
dynamically. 

### Experimenting Subjects on WSL

In this subsection, we are going to be talking about experimenting Subjects on WSL.
This is experimental. 

#### On WSL Ubuntu Setup

In this section, we are going to be talking about setting up dependencies for running
Subjects and developing it on WSL Ubuntu. 

Here is how to get started on that: 

1. `sudo apt update`

2. `sudo apt full-upgrade`

3. `sudo apt install neofetch`

4. `sudo apt install fish`

5. `sudo apt install micro`

6. `sudo apt install python-flask*`

#### Common issues in Ubuntu WSL

Here are some common issues when using Ubuntu WSL

- When running Flask, the default loopback address that is set to is `127.0.0.1:5000` which DOES NOT go out of the container

#### Solution

Here are the solutions

1. In the `index.py` file, you need to change the IP address loopback from `127.0.0.1:5000` to `0.0.0.0`. This is how you change it. By default, the loopback port number is 5000.
   
   ```python
   if __name__ == '__main__':
     app.run(host='0.0.0.0')
   ```

### Experimenting Subjects on Ubuntu Multipass

In this subsection, we are going to be talking about experimenting Subjects on Ubuntu
Multipass. Ubuntu Multipass is useful if you are developing Subjects on macOS. 

Here is how to get started on that: 

1. `brew install multipass`
2. `multipass launch`
3. `multipass shell <name>`
4. `sudo apt update`
5. `sudo apt upgrade`
6. `sudo apt install neofetch`
7. `sudo apt install python-flask*`

#### Common issues in Multipass

Here are some common issues when using Multipass

- When running Flask, the default loopback address that is set to is `127.0.0.1:5000`, which DOES NOT go out of the container

#### Solution

Here are the solutions

1. In the `index.py` file, you need to change the IP address loopback from `127.0.0.1:5000` to `0.0.0.0`. This is how you change it. By default, the loopback port number is 5000. 
   
   ```python
   if __name__ == '__main__':
       app.run(host='0.0.0.0')
   ```

2. Then in the macOS side, in the terminal you need to use this command: 
   
   ```shell
   multipass list 
   ```

3. Look the IP address of the container that you used and installed Subjects on to it, and then use this command: 
   
   ```shell
   chromium --kiosk <ip_address>:5000
   ```
