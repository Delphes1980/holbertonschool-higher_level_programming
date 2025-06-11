#!/usr/bin/python
"""
This module defines a basic HTTP server using Flask to serve API endpoints """

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


users = {}


@app.route('/')
def home():
    """Returns a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Returns a list of all available usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Returns the API status (OK)."""
    return "OK"


@app.route('/users/<username>')
def get_user_by_username(username):
    """
    Retrieves user data by username.
    Args:
        username (str): The username to retrieve.
    Returns:
        JSON: User data if found, or an error message with 404 status.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """ Adds a new user to the system."""
    user_data = request.get_json()
    username = user_data.get("username")
    if username:
        users[username] = user_data  # Add the new user's data
    else:
        return jsonify({"error": "Username is required"}, 400)


if __name__ == "__main__":
    app.run()
