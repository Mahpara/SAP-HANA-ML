from hana_ml.dataframe import ConnectionContext


hana_host = "host"  # hana-host
hana_port = 443  # default
hana_user = "username"
hana_password = "password"

def connect_to_hana():
    """
    Establishes a connection to the instance.
    """
    try:
        conn = ConnectionContext(address=hana_host, port=hana_port, user=hana_user, password=hana_password)
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Failed to connect to SAP HANA: {e}")
        return None
