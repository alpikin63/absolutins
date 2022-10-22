import os
from pathlib import Path

import yaml
from dotmap import DotMap

from core.common.utils.singleton import Singleton

__all__ = ['settings']


class Settings:
    """Класс для хранения настроек стенда."""

    __metaclass__ = Singleton

    def __init__(self):
        self.stand = getattr(self._get_settings(), os.getenv('Stand', 'auto'))

    @staticmethod
    def _get_settings():
        yaml_path = Path(__file__).parent / 'config.yaml'
        with open(yaml_path) as file:
            _yaml = yaml.load(file, Loader=yaml.FullLoader)
            return DotMap(_yaml)


settings = Settings()
