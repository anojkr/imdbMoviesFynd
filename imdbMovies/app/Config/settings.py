

"""
This file contains project config related settings
"""


class Config(object):
    """
    Config class to store configuration for the project. this file can be dynamically
    populated at runtime too.
    """
    LIMIT = 10
    LOGGER_CONFIGURATION = {
	    'version': 1,
	    'formatters': {'default': {
	        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
	    }},
	    'handlers': {'wsgi': {
	        'class': 'logging.StreamHandler',
	        'stream': 'ext://flask.logging.wsgi_errors_stream',
	        'formatter': 'default'
	    }},
	    'root': {
	        'level': 'INFO',
	        'handlers': ['wsgi']
	    }
	}
