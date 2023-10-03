from flask import Flask, request, jsonify
import json
import bcrypt

app = Flask(__name__)


def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def write_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)


@app.route('/signup', methods=['POST'])
def signup():
    try:
        # right but doesnt work for Postman
        # user_email = request.args.get("email")
        # user_password = request.args.get("password")

        data = request.json

        user_email = data.get("email")
        user_password = data.get("password")

        if not user_email or not user_password:
            return jsonify({"error": "Fields are missing"}), 400

        auth_dict = read_json_file("authorized.json")

        if user_email in auth_dict:
            return jsonify({"message": "This email is already used"}), 409

        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())

        new_authorized = {
            "email": user_email,
            "password": hashed_password.decode('utf-8')
        }

        auth_dict[user_email] = new_authorized

        write_json_file("authorized.json", auth_dict)

        users_dict = read_json_file("users.json")
        users_dict[user_email] = {
            "email": user_email,
            "password": hashed_password.decode('utf-8')
        }
        write_json_file("users.json", users_dict)

        return jsonify({"message": "Successfully added"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/signin', methods=['POST'])
def signin():
    try:
        data = request.json

        user_email = data.get("email")
        user_password = data.get("password")

        auth_dict = read_json_file("authorized.json")

        if user_email not in auth_dict:
            return jsonify({"message": "There is no account with this email"}), 404

        stored_password = auth_dict[user_email]["password"]

        if not bcrypt.checkpw(user_password.encode('utf-8'), stored_password.encode('utf-8')):
            return jsonify({"message": "Invalid password"}), 401

        return jsonify({"message": "Successfully signed in"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/logout', methods=['POST'])
def logout():
    try:
        data = request.json

        user_email = data.get("email")

        users_dict = read_json_file("users.json")
        if user_email in users_dict:
            del users_dict[user_email]
            write_json_file("users.json", users_dict)

        return jsonify({"message": "Successfully logged out"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
