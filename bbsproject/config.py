from sqlalchemy import create_engine

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = '1q1w1e2e3q3w3e'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'mybbs'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLCHEMY_TRACK_MODIFICATION = False

# conn = create_engine(DB_URL)
# result = conn.execute('select 1')
# print(result.fetchone())

