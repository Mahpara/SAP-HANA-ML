from connect import connect_to_hana
import pandas as pd
from sklearn.datasets import fetch_openml

def main():
    connection = connect_to_hana()

    # Loading dataset
    print("Loading dataset...")
    wine_data = fetch_openml(name="wine-quality-white", version=1, as_frame=True)
    data = wine_data.data
    data['quality'] = pd.to_numeric(wine_data.target)
    print(data.head())


    table_name = "WINE_QUALITY"
    try:
        print(f"Uploading data to simulated table '{table_name}'...")
        connection.create_dataframe_from_pandas(data.to_dict(orient="records"), table_name=table_name)
    except Exception as e:
        print(f"Failed to upload data: {e}")
        return


    try:
        result = connection.sql(f"SELECT * FROM {table_name}").to_dict(orient="records")

    except Exception as e:
        print(f"Failed to query data: {e}")

    # Performing analysis
    try:
        avg_quality = sum([float(row['quality']) for row in result]) / len(result)
        print(f"The average wine quality is: {avg_quality:.2f}")
    except Exception as e:
        print(f"Failed to analyze data: {e}")

if __name__ == "__main__":
    main()
