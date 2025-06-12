#!/usr/bin/python3
"""
This module defines a basic HTTP server using Flask to serve API endpoints,
demonstrating both HTTP Basic Authentication and JWT-based authentication """

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)  # Initialize the Flask application
auth = HTTPBasicAuth()  # Initialize Flask-HTTPAuth for Basic Authentication
app.config["JWT_SECRET_KEY"] = "super_secrete_key"
jwt = JWTManager(app)  # Initialize Flask-JWT-Extended

# In-memory user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"), "role": "user"},
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Callback function for HTTP Basic Auth.
    Verifies the provided username and password against the stored users
    """
    user = users.get(username)  # Get user data from the in-memory store
    # Checks if user exists & password hash matches
    if user in users and check_password_hash(user["password"], password):
        return user
    else:
        return None  # If credentials are invalid


@app.route('/')
def home():
    """Returns a welcome message for the API."""
    return "Welcome to secured API!"


@app.route('/basic-protected')
@auth.login_required  # Protects this route with HTTP Basic Authentication
def basic_protected():
    """
    An endpoint protected by HTTP Basic Authentication.
    Access requires valid username/password in Authorization header
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login, authenticates credentials, and issues
    a JWT access token
    Expects JSON with 'username' and 'password'.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"Bad username or password"}), 401
    else:
        # Create an access token for the authenticated user
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()  # Protects this route, requiring a valid JWT access token
def jwt_protected():
    """
    An endpoint protected by JWT authentication.
    Access requires a valid JWT in the Authorization: Bearer header
    """
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()  # Requires a valid JWT
def admin():
    """
    An endpoint for admin users only.
    Requires a valid JWT and checks if the user has 'admin'
    role from their identity
    """
    # Get the identity from the JWT payload
    current_user_identity = get_jwt_identity()
    # Checks if the user's role includes 'admi'
    if "admin" in users[current_user_identity]["role"]:
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
