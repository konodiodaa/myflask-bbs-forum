from datetime import datetime
from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    @property  # 把类中一个方法定义为一个属性
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password, method='pbkdf2:sha1', salt_length=8)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result   # return  whether password are same after encoding

