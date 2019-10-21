# MacInfo
Docker image run to get company info for an input MAC address using REST in python

Getting Started
- Create a API key from "https://macaddress.io/api/documentation/making-requests" using your account 
- $ git clone https://github.com/Sheetztime/MacInfo
$ cd MacInfo
$ docker build -t macinfo  
$ docker run --rm macinfo 98-01-a7-a2-df-fd <your APIKEY>

Prerequisites
- Docker Engine , refer https://docs.docker.com/install/
- This has been tested on Docker running on MAC OS  with Python version 3.X.
- You need a working  internet connection

Installing
Copy the code in a linux/Unix/desbian/windows machine capable of runnig Docker engine
File list include 
- Dockerfile
- Mactest.py 

To build Docker Container run
-docker build -t macinfo .
Where macinfo is the container Name 

To Run the container:
docker run --rm macinfo <MAC ADDRESS TO GET INFO OF> <APIKEY>
Idea is to get the output from the program and then delete the container as it serves no other purpose, hence you see "--rm" parameter. 

Example
docker run --rm macinfo 44:38:39:ff:ef:57 <APIKEY>


Running the tests cases:
If you don't pass both the argurments  following error will occur:
- INvalid MAC address 
Error: invalid MAC address format, please enter a Valid MAC in format ff:ff:ff:ff:ff:ff ,ff-ff-ff-ff-ff-ff,ffffffffffff
- Not passing all arguments 
Error: "pass a MAC address  and API key as as  input to this script Example : /usr/local/bin/python3 Mactest.py <MAC ADDR> <API KEY>"
- INvalid API key 
Program will exist without any error 
 - No connection 
 "Curl command failure error"

Security:
Program calls a REST API to https://macaddress.io/ server and fetch Company info available for the given MAC
Detailed Documentation available here "https://macaddress.io/api/documentation/making-requests"

THere are 2 methods to Aunthenticate available 
1) Query based 
2) Header based 

Query based authentication is programmed in the code with API Key , you need to create an APIKEy from "https://macaddress.io/api/documentation/making-requests" and pass it as an Argument to the docker run
