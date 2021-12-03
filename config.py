
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://u8afqm51hf1iuji6:JMorwFcnW4fYwjp5PLQx@localhost:3306/uce")
    #SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://acroming_u8afqm51hf1iuji6:JMorwFcnW4fYwjp5PLQx@acroming.com:3306/acroming_ucemining")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
