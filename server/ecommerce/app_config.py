
CONFIG = None


class Config:

    SWAGGER_UI_DOC_EXPANSION = 'list'
    FLASK_ADMIN_SWATCH = 'cerulean'
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000

    POSTGRES_DBNAME = 'postgres'
    POSTGRES_HOST = SERVER_HOST
    POSTGRES_PORT = 5432
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'postgres'


class ProductionConfig(Config):
    DEBUG = False
    TEST = False
    PROD = True


class DevelopmentConfig(Config):
    DEBUG = True
    TEST = False
    PROD = False


class UnitTestConfig(Config):
    DEBUG = False
    TEST = True
    PROD = False
    SERVER_PORT = 12345
