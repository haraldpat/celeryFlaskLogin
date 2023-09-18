import logging
import requests
from flask import request,jsonify
from src.models import User
from src.services import UserService
from src.app import simple_app
logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the Flask scaffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        user_services = UserService()
        u_name = data["username"]
        passw = data["password"]
        new_user = User(username= u_name,password = passw)
        # new_user1 = User(username ="John",password ="12345678")
        # new_user1.password = new_user1.hash_password("12345678")
        # new_user1.save()
        # new_user2 = User(username = "Sonu",password = "sonu11")
        # new_user2.password = new_user2.hash_password("sonu11")
        # new_user2.save()
        # new_user3 = User(username = "Harry",password = "123")
        # new_user3.password = new_user3.hash_password("123")
        # new_user3.save()
        # all_users = User.objects.all()
        # for user0 in all_users:
        #     logger.info(user0.username)
        #     logger.info(user0.password)
        return user_services.login_user(new_user.username,new_user.password)

    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        return jsonify({"message": "Error occurred during login"}), 500

def get_status():
    task_id = request.args.get('id')
    status = simple_app.AsyncResult(task_id,app=simple_app)
    return jsonify({"status":"Status of the task " + str(status.state)}), 200

def task_result():
    task_id = request.args.get('id')
    result = simple_app.AsyncResult(task_id).result
    return jsonify({"result":"Result of the task " + str(result)}), 200

   

