from core.common.base_randomizer import BaseRandomizer


class BaseBuilder(BaseRandomizer):

    def but(self):
        return self

    def random(self):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError
