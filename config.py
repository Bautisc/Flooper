

class Dev_config():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flooper_db'
    MYSQL_CURSORCLASS = "DictCursor"


config = {
    'desarrollo': Dev_config
}
