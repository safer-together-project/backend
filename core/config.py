import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = 'development'
    DEBUG: bool = True
    DB_USER: str = 'admin'
    DB_PASS: str = 'steds_care_db'
    DB_HOST: str = 'localhost'
    DB_NAME: str = 'stedscare'
    DB_URL: str = f'mariadb+asyncmy://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}'
    HASH_SECRET: str = 'e460a24f6eb1ace0bcd8d7fb48b91dd0ff19a2094dd3aea3897398a892213bdd'


class DevelopmentConfig(Config):
    DEBUG: bool = True


class TestingConfig(Config):
    DEBUG: bool = True


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv('ENV', 'development')
    config_type = {
        'development': DevelopmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig(),
    }
    return config_type[env]


config = get_config()
