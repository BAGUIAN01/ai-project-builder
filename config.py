import logging
import os
from dotenv import load_dotenv


ENV = os.getenv('ENV', 'development')
if ENV == 'development':
    load_dotenv()


class Config:
    """Basic setup"""
    DEBUG = False
    TESTING = False

    PROJECT_NAME = os.getenv('PROJECT_NAME')
    VENV_DIRECTORY = os.getenv('VENV_DIRECTORY')
    PYTHON_EXECUTABLE = os.getenv('PYTHON_EXECUTABLE')

    @staticmethod
    def configure_logging():
        """Configure logging settings."""
        log_level = logging.DEBUG if Config.DEBUG else logging.WARNING

        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
            ]
        )


class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True


class ProductionConfig(Config):
    """Configuration for production."""
    DEBUG = False


class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

current_config = config.get(ENV, DevelopmentConfig)
current_config.configure_logging()
