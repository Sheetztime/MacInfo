# MacInfo
Docker image run to get company info for an input MAC address using REST in python

Getting Started
1) - Create a API key from "https://macaddress.io/api/documentation/making-requests" using your account 
2) $ git clone https://github.com/Sheetztime/MacInfo
3) $ cd MacInfo      :
4) $ docker build -t macinfo .       
5) $ docker run --rm macinfo 98-01-a7-a2-df-fd APIKEY_You_Created_in_Step1     

Prerequisites:
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
docker run --rm macinfo 44:38:39:ff:ef:57 APIKEY_You_Created


Running the tests cases:


1) If you don't pass both the argurments  following error will occur:
- INvalid MAC address :
Error: invalid MAC address format, please enter a Valid MAC in format ff:ff:ff:ff:ff:ff ,ff-ff-ff-ff-ff-ff,ffffffffffff:
2) Not passing all arguments:
Error: "pass a MAC address  and API key as as  input to this script Example : /usr/local/bin/python3 Mactest.py <MAC ADDR> <API KEY>"
3) INvalid API key :
Program will exist without any error:
 
 4) No connection:
 "Curl command failure error":

Security:
Program calls a REST API to https://macaddress.io/ server and fetch Company info available for the given MAC
Detailed Documentation available here "https://macaddress.io/api/documentation/making-requests"

THere are 2 methods to Aunthenticate available:
1) Query based 
2) Header based 

Query based authentication is programmed in the code with API Key , you need to create an APIKEy from "https://macaddress.io/api/documentation/making-requests" and pass it as an Argument to the docker run
