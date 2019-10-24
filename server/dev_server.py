
try:
    import subprocess
    import logging.config
    from ecommerce import logging_config
    from ecommerce import app_config
    from ecommerce import app
    from shutil import which

    # TODO make different check between localhost and heroku
    if which('docker') is None:
        raise Exception('docker not installed.')
    if which('docker-compose') is None:
        raise Exception('docker-compose not installed.')
    subprocess.run('docker-compose -f docker-compose.yml up -d', shell=True)

    app_config.CONFIG = app_config.DevelopmentConfig
    logging.config.dictConfig(logging_config.DEV)

    app = app.init(app_config.CONFIG)
    app.run(host=app_config.CONFIG.SERVER_HOST, port=app_config.CONFIG.SERVER_PORT)
except Exception:
    import traceback
    traceback.print_exc()
