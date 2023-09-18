from celery import Celery
from celery.utils.log import get_task_logger
import mongoengine
from datetime import datetime
from models import User  
from models.userlog import UserLog
logger = get_task_logger(__name__)
app = Celery('tasks',broker='redis://redis:6379/0', backend='redis://redis:6379/0',)

@app.task
def update_last_login(user_name):
    logger.info("Work Started")
    try:
        mongoengine.connect(db='scaffolding', host='db')

        user = User.objects(username=user_name).first()
        if user:
            user_log = UserLog(username = user.username,login_time = datetime.now())
            user_log.save()
            logger.info("Work Ended")
            return f"Last login updated for user {user.username}"
        else:
            logger.info("Work Ended")
            return f"User with ID {user_name} not found"
    except Exception as e:
        logger.info("Work Ended")
        return f"Error updating last login: {str(e)}"
