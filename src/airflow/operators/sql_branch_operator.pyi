from airflow.operators.sql import BranchSQLOperator as BranchSQLOperator

class BranchSqlOperator(BranchSQLOperator):
    def __init__(self, *args, **kwargs) -> None: ...
