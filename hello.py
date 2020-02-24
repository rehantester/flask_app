import json
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

#GET is by default
#200 is by default
@app.route('/')
def hello():
    return "Hello, world"
    
@app.route('/customer', methods=["POST"])
def create_customer():
    #json.loads > turns request BODY the client sends into a JSON object.
    #jsonify > returns a HTTP Response that flash can understand to the User.
    return jsonify(json.loads(request.data)), 201
    
@app.route('/redirect-customer')
def redirect_customer():
    return redirect('http://example.com')
    