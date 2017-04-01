from django.db.backends.base.base import BaseDatabaseWrapper


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'neo4j'
    data_types = {

    }

    def _start_transaction_under_autocommit(self):
        pass

    def _set_autocommit(self, autocommit):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_connection_params(self):
        pass

    def get_new_connection(self, conn_params):
        pass

    def init_connection_state(self):
        pass

    def create_cursor(self, name=None):
        pass

    def chunked_cursor(self):
        pass

    def check_constraints(self, table_names=None):
        pass

    def is_usable(self):
        pass

    def neo4jdriver_version(self):
        pass

    def neo4j_version(self):
        pass
