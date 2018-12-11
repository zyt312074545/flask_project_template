"""
    .----------------.  .----------------.  .----------------.
    | .--------------. || .--------------. || .--------------. |
    | |   _____      | || |     ____     | || |    ______    | |
    | |  |_   _|     | || |   .'    `.   | || |  .' ___  |   | |
    | |    | |       | || |  /  .--.  \  | || | / .'   \_|   | |
    | |    | |   _   | || |  | |    | |  | || | | |    ____  | |
    | |   _| |__/ |  | || |  \  `--'  /  | || | \ `.___]  _| | |
    | |  |________|  | || |   `.____.'   | || |  `._____.'   | |
    | |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'
"""

import os
import logging
import logging.config

import toml


def setup_logging(
        default_path='log.toml',
        default_level=logging.INFO,
):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r') as f:
            config = toml.loads(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    return logging


# Reset Werkzeug log level
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Return logger
# Flask App should remove default_handler
logger = setup_logging()
