import os
from os import environ


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


JWT_SECRET_KEY = os.getenv('SECRET_KEY') # the values of those depend on your setup
POSTGRES_URL = get_env_variable("127.0.0.1:5432")
POSTGRES_USER = get_env_variable("postgres")
POSTGRES_PW = get_env_variable("bigjim66")
POSTGRES_DB = get_env_variable("Junkyard") 
