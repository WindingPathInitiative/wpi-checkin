from flask import Flask, request, Response
from functools import wraps
import json
import requests
import logging
from peewee import *

with open('config.json', 'r') as f:
	config = json.load(f)

from models import *

app = Flask(__name__)

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		logging.warning('Checking JWT')
		auth_header = request.headers.get('Authorization')
		if ('Authorization' not in request.headers) or (request.headers['Authorization'] is None):
			logging.warning('No Auth Header')
			return Response({"message":"Authorization Token not provided","status":403}, status=403, mimetype='application/json')
		headers = {'Authorization':auth_header}
		logging.warning('Running Request')
		url = config['hub']['server']+'v1/user/me?offices=1'
		logging.warning('Calling URL '+url)
		r = requests.get(url, headers=headers)
		if r.status_code != 200:
			logging.warning('Error response')
			try:
				json = r.json()
				logging.warning('Returning JSON Error'+r.text)
				return Response(r.json(), status= r.status_code, mimetype='application/json')
			except:
				logging.warning('Returning Unknown error, status code '+r.status_code+' response '+r.text)
				return Response({"message":"Error Checking JWT","status":500}, status=500, mimetype='application/json')
		logging.warning('Got response! '+r.text)
		logging.warning('passing through to function!')
		return f(*args, **kwargs)
	return decorated_function

@app.route('/')
@login_required
def hello_world():
	return 'Hello, World!'