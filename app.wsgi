#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApache/SpeedOfLuca")
# Here `FlaskApache` is the parent one, not the nested one
from app import app as application