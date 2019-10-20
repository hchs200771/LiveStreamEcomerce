DEV = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(process)d:%(threadName)-s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 10000000,
            'backupCount': 3,
            'filename': 'server.log',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'engineio': {
            'handlers': ['console', 'file'],
            'level': 'WARN',
            'propagate': False
        }
        # 'urllib3.connectionpool': {
        #     'handlers': ['console', 'file'],
        #     'level': 'ERROR',
        #     'propagate': False
        # }
    }
}
