class WeightRule:
    DOWNSTREAM: str
    UPSTREAM: str
    ABSOLUTE: str
    @classmethod
    def is_valid(cls, weight_rule): ...
    @classmethod
    def all_weight_rules(cls): ...
