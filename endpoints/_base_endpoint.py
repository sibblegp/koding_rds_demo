"""Base endpoint module used for all endpoints"""
__author__ = 'gsibble'

from flask_restful import Resource
from flask import redirect, request, abort

from models import sql_models
from config import settings

class ApiEndpoint(Resource):
    """Base API Endpoint for Flask Restful"""
    models = sql_models

    def options(self, *args, **kwargs):
        """API Result to return when http "options" is called"""
        return self.make_html_response('')

    def make_response(self, response_data=None, response_code=200, failure_reason=None):
        """Make JSON serialized API response"""
        api_response = response_data
        headers = {}
        headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
        #headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Max-Age'] = str(1728000)
        headers['Access-Control-Allow-Headers'] = 'accept, origin, api_key, content-type, user-api-key'
        headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return api_response, response_code, headers

    def make_html_response(self, html):
        """Make HTML API Response"""
        headers = {}
        headers['Allow'] = 'GET, POST, PUT, DELETE, OPTIONS'
        #headers['Access-Control-Allow-Origin'] = '*'
        headers['Access-Control-Max-Age'] = str(1728000)
        headers['Access-Control-Allow-Headers'] = 'accept, origin, api_key, content-type, user-api-key'
        headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return (html, 200, headers)

    def make_redirect_response(self, redirect_url):
        """Make a redirect response"""
        return redirect(redirect_url)
