from wtforms.validators import EqualTo

class GreaterEqualThan(EqualTo):
    def __call__(self, form, field) -> None: ...
