from flask import Flask
import json
from peewee import *

with open('config.json', 'r') as f:
	config = json.load(f)

db = MySQLDatabase(config['db']['database'],user=config['db']['username'],password=config['db']['password'], host=config['db']['host'], port=config['db']['port'])

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'