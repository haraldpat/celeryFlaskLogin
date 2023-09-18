import bcrypt
from mongoengine import Document, StringField

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    username = StringField(unique=True, required=True)
    password = StringField(required=True)

    @staticmethod
    def hash_password(passwordo):
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(passwordo.encode('utf-8'), salt)
        return password.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))



  
