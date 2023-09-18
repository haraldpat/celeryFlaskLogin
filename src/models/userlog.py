from mongoengine import Document,StringField,DateTimeField

class UserLog(Document):
    username = StringField(required=True)
    login_time = DateTimeField(required=True)
