import os

class Config:
    SECRET_KEY = '8cce3372ecd5b36188ef0172fdba0a00' # os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/nakshatra' # os.environ['SQLALCHEMY_DATABASE_URI']