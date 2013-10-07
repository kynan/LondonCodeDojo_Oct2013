PINT = 20
HALF_PINT = PINT/2
PITCHER = 3*PINT

class NoContentException(Exception):
    pass


class DontBeGreedyException(Exception):
    pass


class Glass(object):
    _content = None

    def __init__(self):
        self._content = self._max

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, v):
        if v < 0 or v == 0 and self.is_empty():
            self._content = 0
            raise NoContentException()
        self._content = v

    def is_full(self):
        return self.content == self._max

    def is_empty(self):
        return self.content == 0

    def refill(self):
        self.content = self._max

    def drink(self):
        self.content -= 1

    def quaff(self):
        if self.content < 4:
            self.content = 0
        else:
            self.content -= 4

    def down(self):
        self.content = 0


class PintGlass(Glass):
    _max = PINT


class HalfPintGlass(Glass):
    _max = HALF_PINT


class Pitcher(Glass):
    _max = PITCHER
