import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = 'development'
    DEBUG: bool = True
    DB_USER: str = 'admin'
    DB_PASS: str = 'steds_care_db'
    DB_HOST: str = 'localhost'
    DB_NAME: str = 'stedscare'
    DB_URL: str = f'mariadb+mariadbconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}'


class DevelopmentConfig(Config):
    DEBUG: str = True


class TestingConfig(Config):
    DEBUG: str = True


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv('ENV', 'development')
    config_type = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig(),
    }
    return config_type[env]


config = get_config()
