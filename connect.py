import pandas as pd

class MockConnection:
    def __init__(self):
        self.data = {}

    def create_dataframe_from_pandas(self, data, table_name, force=False):
        self.data[table_name] = data
        print(f"Simulated table '{table_name}' created.")
        return pd.DataFrame(data)

    def sql(self, query):
        table_name = query.split("FROM")[1].strip().split()[0]
        if table_name in self.data:

            return pd.DataFrame(self.data[table_name])
        else:
            raise ValueError(f"Table '{table_name}' does not exist.")

def connect_to_hana():
    """
    Simulating a mock connection to SAP HANA.
    """

    return MockConnection()
