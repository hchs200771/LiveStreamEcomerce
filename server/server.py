
try:
    import os
    import urllib.parse
    import subprocess
    import logging.config
    from ecommerce import logging_config
    from ecommerce import app_config
    from ecommerce import app
    from shutil import which

    if os.environ.get('ENV') == 'production':
        app_config.CONFIG = app_config.ProductionConfig
    else:
        app_config.CONFIG = app_config.DevelopmentConfig
    logging.config.dictConfig(logging_config.DEV)

    if os.environ.get('ON_HEROKU'):
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(os.environ['DATABASE_URL'])
        app_config.CONFIG.POSTGRES_DBNAME = url.path[1:]
        app_config.CONFIG.POSTGRES_HOST = url.hostname
        app_config.CONFIG.POSTGRES_PORT = url.port
        app_config.CONFIG.POSTGRES_USER = url.username
        app_config.CONFIG.POSTGRES_PASSWORD = url.password
    else:
        if which('docker') is None:
            raise Exception('docker not installed.')
        if which('docker-compose') is None:
            raise Exception('docker-compose not installed.')
        subprocess.run('docker-compose -f docker-compose.yml up -d', shell=True)

    app = app.init(app_config.CONFIG)
    app.run(host=app_config.CONFIG.SERVER_HOST, port=app_config.CONFIG.SERVER_PORT)
except Exception:
    import traceback
    traceback.print_exc()
