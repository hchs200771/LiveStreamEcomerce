
try:
    import logging.config
    from ecommerce import logging_config
    from ecommerce import app_config
    from ecommerce import app

    app_config.CONFIG = app_config.DevelopmentConfig
    logging.config.dictConfig(logging_config.DEV)

    app = app.init(app_config.CONFIG)
    app.run(host=app_config.CONFIG.SERVER_HOST, port=app_config.CONFIG.SERVER_PORT)
except Exception:
    import traceback
    traceback.print_exc()
