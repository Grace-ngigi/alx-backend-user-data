#!/usr/bin/env python3
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
app = Flask(__name__)


AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    ''' return bienvenue'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    ''' Register user '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{email}", "message": "user created"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    '''' login '''
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    res = jsonify({"email": f"{email}", "message": "logged in"})
    res.set_cookie("session_id", session_id)
    return res


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> None:
    session_id = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)    

    AUTH.destroy_session(user.id)
    # redirect
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
