import logging
from src.models import User
from flask import jsonify
from src.app import simple_app

logger = logging.getLogger("default")

class UserService(object):
    """
    service function for user related business logic
    """
    def call_method(self,username):
        logger.info("Invoking method")
        res = simple_app.send_task('tasks.update_last_login',kwargs={'user_name':username})
        logger.info(res.backend)
        return res.id   
    
    def login_user(self,un,passw):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        #3 cases
        #1 username not found
        #2 password not matched
        #3 if everything is allright
        try:
            user = User.objects(username=un).first()
            logger.info(user)
            if user:
                if user.check_password(passw):
                    id = self.call_method(un)
                    return jsonify({"message":"Valid","task_id": id}),200
                else:
                    return jsonify({"message":"Invalid Credentials"}), 403

            else:
                return jsonify({"message":"Go to register page"}), 401
        
        except Exception as e:
            logger.error(f"Error during accesing database:{str(e)}")
            return jsonify({"message":"Error occured accessing things"}),500


     
