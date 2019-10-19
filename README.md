# MacInfo
Docker image to get company info for an input MAC address using REST in python

Getting Started
Clone/Download the Git code

Prerequisites
- Docker Engine , refer https://docs.docker.com/install/
This has been tested on Docker running on MAC OS  with Python version 3.X
You need a working  internet connection

Installing
Copy the code in a linux/Unix/desbian/windows machine capable of runnig Docker engine
File list include 
- Dockerfile
- Mactest.py 

To build Docker Container run
-docker build -t python-macinfoapi .
Where python-macinfapi is the container Name 

To Run the container:
docker run --rm python-macinfoapi <MAC ADDRESS TO GET INFO OF>
Idea is to get the output from the program and then delete the container as it serves no other purpose, hence you see "--rm" parameter. 

Example
docker run --rm python-macinfoapi 44:38:39:ff:ef:57

OutPut:
sangra$ docker run --rm python-macinfoapi 44:38:39:ff:ef:57

Company details for the MAC address44:38:39:ff:ef:57
"companyName":"Cumulus Networks Inc
"companyAddress":"650 Castro Street suite 120-245 Mountain View CA 94041 US
sangra$

Running the tests
If you don't pass any any argument following error will occur:
"pass a MAC address as as single input to this script in format XX:XX:XX:XX:XX:XX"
 

Security:
Program calls a REST API to https://macaddress.io/ server and fetch Company info available for the given MAC
Detailed Documentation available here "https://macaddress.io/api/documentation/making-requests"

THere are 2 methods to Aunthenticate available 
1) Query based 
2) Header based 

Query based authentication is programmed in the code with API Key , if you would like to chnage that, refer to the documentation and change the API call accordingly. You can create your account and change th API-KEY paramater in the call and pass the API key as the header. 




