"""This module can be used in conjunction with the for_fetch.html file to see how you can create an http request body"""
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Data_access_layer.dao_imp import DAOImp
from custom_exceptions.failed_transaction import FailedTransaction
from service_access_layer.service_access_imp import ServiceAccessIMP

# Make sure you have flask and flask-cors installed from pypi
app: Flask = Flask(__name__)
CORS(app)  # use this to avoid cors errors

data_object = DAOImp()
service_object = ServiceAccessIMP(data_object)


@app.route("/login", methods=["POST"])
def login():
    try:
        login_dict: dict = request.get_json()
        auth_token = service_object.do_login(login_dict)
        auth_response = {
            "token": auth_token,
            "message": "Identity Confirmed!"
        }
        return auth_response, 201
    except FailedTransaction as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


@app.route("/home", methods=["POST"])
def create_request():
    try:
        request_data: dict = request.get_json()
        for token in request_data:
            if token == "token":
                if request_data[token] is not None:
                    request_data.pop("token")
                    result = service_object.service_create_reimbursement_request(request_data)
                    result_dictionary = result.return_json_friendly_dictionary()
                    result_json = jsonify(result_dictionary)
                    return result_json, 201
        message = {
            "message": "Access Denied"
        }
        return jsonify(message), 400
    except FailedTransaction as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/home", methods=["DELETE"])
def cancel_request():
    try:
        request_data: dict = request.get_json()
        for token in request_data:
            if token == "token":
                if request_data[token] is not None:
                    request_data.pop("token")
                    result = service_object.service_cancel_reimbursement_request(request_data)
                    result_dictionary = {
                        "message": result
                    }
                    result_json = jsonify(result_dictionary)
                    return result_json, 201
        message = {
            "message": "Access Denied"
        }
        return jsonify(message), 400
    except FailedTransaction as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/home", methods=["PATCH"])
def select_request():
    try:
        request_data: dict = request.get_json()
        for token in request_data:
            if token == "token":
                if request_data[token] is not None:
                    request_data.pop("token")
                    result = service_object.service_select_total_amount_requested(request_data)
                    result_dictionary = {
                        "message": result
                    }
                    result_json = jsonify(result_dictionary)
                    return result_json, 201
        message = {
            "message": "Access Denied"
        }
        return jsonify(message), 400
    except FailedTransaction as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
