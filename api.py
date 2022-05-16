from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import json

# Initialize Flask API
app = Flask(__name__)
api = Api(app)

def get_database(db_name):
    # Load connection string from creds.json
    db_cert = "ca-certificate.crt" 
    with open('creds.json') as creds:
        CONNECTION_STRING = json.load(creds)['MongoDB']['connection_string'] + db_cert

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client[db_name] # return database

# Make class for particular resource

class GetBin(Resource):
    def get(self, bin):
        # get db instance and open bins collection
        db = get_database('bin_list')
        bins = db['bins']
        # get all bins matching bin
        find = bins.find({'Bin': str(bin)})
        bins = [bin for bin in find]
        # if bins found
        if len(bins) != 0:
            del bins[0]['_id']
            return bins[0]
        else:
            # no bins found
            return jsonify({'error': '404', 'message': 'BIN Not Found'})
    def post(self):
        # only accept get requests
        return jsonify({'error': '401', 'message': 'Unauthorized'})

api.add_resource(GetBin, '/bin/<int:bin>')

if __name__ == '__main__':
    # public host and port 8393
    app.run(host = '0.0.0.0', port = '8393')