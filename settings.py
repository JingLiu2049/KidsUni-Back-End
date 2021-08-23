import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def get_db_uri(dbinfo):
    engine = dbinfo.get('ENGINE') or 'postgresql'
    driver = dbinfo.get('DRIVER') or 'psycopg2'
    user = dbinfo.get('USER') or 'postgres'
    pw = dbinfo.get('PW') or 'liujing121'
    host = dbinfo.get('HOST') or 'localhost'
    port = dbinfo.get('PORT') or '5432'
    name = dbinfo.get('NAME') or 'kidsunirebuild'
    uri = f"{engine}+{driver}://{user}:{pw}@{host}:{port}/{name}"
    return uri

class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kidsUni_rebuilding_server'

class DevelopConfig(Config):
    DEBUG = True
    DTATABASE = {
        'ENGINE' : 'postgresql',
        'DRIVER' : 'psycopg2',
        'USER' : 'postgres',
        'PW' : 'liujing121',
        'HOST' : 'localhost',
        'PORT' : '5432',
        'NAME' : 'kidsunirebuild'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DTATABASE)



envs = {
    'develop':DevelopConfig,
}