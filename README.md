
# BIN/IIN Checker API

This application hosts a RestFul API using Python's Flask module. It uses publicly available
(and slightly out-of-date) BIN/IIN information that has been compiled into a MongoDB. The 
main goal of this project was to make a BIN checker that had accurate US Prepaid Gift Card
information. The Prepaid Gift Card information was inputted manually into the database.

## Data Sources

 - [Binlist](https://github.com/binlist)
 - [iannuttall](https://github.com/iannuttall/binlist-data)
 - The information in both lists above has been modified to fit.
## Demo

Insert gif or link to demo


## API Reference

#### Get BIN Information

```http
  GET http://localhost:8393/bin/<bin number>
```

Takes the IP address of the running `api.py` file. 


## Installation

Create a new [Digital Ocean]('https://cloud.digitalocean.com/) project.

Digital Ocean is the platform used in the installation steps. 

Inside of your project create a droplet and a MongoDB database. Fill in the `sample_creds.json`
file with your MongoDB information and connection string. Please note you will need to end
the connection string at `&tlsCAFile=`. The notebook we use will have a place for you to
name your CA-Certificate file. 

Inside of your `Database Clusters` in Digital Ocean, click on your database. Press Edit Sources
and include the droplet you have made. Failure to do so will result in your `api.py` never 
yielding a result.

Inside of your droplet you will need to enter your desired directory before proceeding.
```bash
  cd <your directory>
```
Copy all of the files to this directory and rename `sample_creds.json` to `creds.json`.
```bash
  apt get install python3-pip --fix-missing
  pip3 install flask flask_restful pymongo
  python3 api.py
```
This will start on your public IP in debug mode. This is not recommended with development servers.
    
