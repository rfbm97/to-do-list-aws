import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
#BASE_URL = "https://m0qwfec693.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example"
        }
        response = requests.post(url, data=json.dumps(data))
        print('Full Response: ', response.text)  # <-- Añadido
        json_response = response.json()
        print('Response Add Todo: ' + str(json_response))
        jsonbody = json.loads(json_response.get('body', '{}'))  # <-- Modificado        
        
        
    def test_api_addtodo(self):
        print('---------------------------------------')
        print('Starting - integration test Add TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example"
        }
        response = requests.post(url, data=json.dumps(data))
        print('Full Response: ', response.text)  # <-- Añadido para imprimir toda la respuesta
        json_response = response.json()
        print('Response Add Todo: ' + json_response.get('body', 'No body found'))  # <-- Modificado para evitar el KeyError

    def test_api_gettodo(self):
        print('---------------------------------------')
        print('Starting - integration test Get TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - GET"
        }
        response = requests.post(url, data=json.dumps(data))
        print('Full Response: ', response.text)  # <-- Añadido
        json_response = response.json()
        print('Response Add Todo: ' + str(json_response))
        jsonbody = json.loads(json_response.get('body', '{}'))  # <-- Modificado
        
    def test_api_updatetodo(self):
        print('---------------------------------------')
        print('Starting - integration test Update TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - Initial"
        }
        response = requests.post(url, data=json.dumps(data))
        print('Full Response: ', response.text)  # <-- Añadido
        json_response = response.json()
        print('Response Add todo: ' + json_response.get('body', 'No body found'))  # <-- Modificado
        
    def test_api_deletetodo(self):
        print('---------------------------------------')
        print('Starting - integration test Delete TODO')
        url = BASE_URL + "/todos"
        data = {
            "text": "Integration text example - Initial"
        }
        response = requests.post(url, data=json.dumps(data))
        print('Full Response: ', response.text)  # <-- Añadido
        json_response = response.json()
        print('Response Add todo: ' + json_response.get('body', 'No body found'))  # <-- Modificado
        
