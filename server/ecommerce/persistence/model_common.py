import inspect
import logging
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from types import ModuleType
from ecommerce import util
from ecommerce import app_config
from playhouse.postgres_ext import PostgresqlExtDatabase

log = logging.getLogger(__name__)


@util.log_scope(log)
def is_database_exist(dbname):
    con = psycopg2.connect(
        dbname=app_config.CONFIG.POSTGRES_DEFAULT,
        host=app_config.CONFIG.POSTGRES_HOST,
        user=app_config.CONFIG.POSTGRES_USER,
        password=app_config.CONFIG.POSTGRES_PASSWORD
    )
    cur = con.cursor()
    cur.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname='%s';" % dbname)

    return True if cur.fetchall() else False


@util.log_scope(log)
def reset_database(dbname):
    con = psycopg2.connect(
        dbname=app_config.CONFIG.POSTGRES_DEFAULT,
        host=app_config.CONFIG.POSTGRES_HOST,
        port=app_config.CONFIG.POSTGRES_PORT,
        user=app_config.CONFIG.POSTGRES_USER,
        password=app_config.CONFIG.POSTGRES_PASSWORD
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    if is_database_exist(dbname):
        cur.execute("DROP DATABASE %s;" % dbname)

    cur.execute("CREATE DATABASE %s;" % dbname)


@util.log_scope(log)
def get_model_tables(module_obj):
    if not isinstance(module_obj, ModuleType):
        raise RuntimeError('Invalid module.')

    tables = []
    for name, obj in inspect.getmembers(module_obj, lambda obj: inspect.isclass(obj) and issubclass(obj, module_obj.BaseModel)):
        if name.find('BaseModel') == -1:
            tables.append(obj)

    return tables


def generate_db_object(dbname):
    db_obj = PostgresqlExtDatabase(
        dbname,
        host=app_config.CONFIG.POSTGRES_HOST,
        port=app_config.CONFIG.POSTGRES_PORT,
        user=app_config.CONFIG.POSTGRES_USER,
        password=app_config.CONFIG.POSTGRES_PASSWORD,
        thread_safe=True
    )
    return db_obj


@util.log_scope(log)
def create_model(module_name, dbname):
    module_obj = sys.modules[module_name]
    reset_database(dbname)
    db_obj = generate_db_object(dbname)
    module_obj.database_proxy.initialize(db_obj)
    db_obj.create_tables(get_model_tables(module_obj), safe=True)


@util.log_scope(log)
def load_model(module_name, dbname):
    module_obj = sys.modules[module_name]
    db_obj = generate_db_object(dbname)
    module_obj.database_proxy.initialize(db_obj)
