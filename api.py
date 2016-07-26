__author__ = 'gsibble'

#Import our config
from config import settings

#Import our models
from models import sql_models

#Import necessary packages
from flask import Flask
from flask_restful import Api

#Initialize our Flask APP
APP = Flask(__name__)
#from werkzeug.contrib.profiler import ProfilerMiddleware
#APP.wsgi_app = ProfilerMiddleware(APP.wsgi_app, restrictions=[30])
#Set app to bundle API Errors
APP.config['BUNDLE_ERRORS'] = True

#Set debug
if settings.DEBUG:
    APP.debug = True

#Initialize our restful API
API = Api(APP)


#Import our endpoints
from endpoints import ALL_ENDPOINTS

#Create our endpoint resources
for endpoint in ALL_ENDPOINTS:
    API.add_resource(endpoint, '/' + settings.BASE_API_VERSION + endpoint.location)


#Tear down Session after every request
@APP.teardown_appcontext
def shutdown_session(exception=None):
    sql_models.SESSION.close()

#Run the app
if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000)
