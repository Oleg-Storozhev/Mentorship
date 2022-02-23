import os


class Config(object):
    """Base config, uses staging database server."""
    SECRET_KEY = "YOUR_SECRET_KEY"
    DATABASE = os.path.join("instance", "project.sqlite")
    FILES_DIR = "add_files"
