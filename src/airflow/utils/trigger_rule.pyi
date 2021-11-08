class TriggerRule:
    ALL_SUCCESS: str
    ALL_FAILED: str
    ALL_DONE: str
    ONE_SUCCESS: str
    ONE_FAILED: str
    NONE_FAILED: str
    NONE_FAILED_OR_SKIPPED: str
    NONE_SKIPPED: str
    DUMMY: str
    @classmethod
    def is_valid(cls, trigger_rule): ...
    @classmethod
    def all_triggers(cls): ...
