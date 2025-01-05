from connect import connect_to_hana
import pandas as pd
from sklearn.datasets import fetch_openml
from hana_ml.algorithms.pal.regression import PolynomialRegression
from hana_ml import dataframe

def main():
    connection = connect_to_hana()
    if not connection:
        return

    print("Loading dataset...")
    wine_data = fetch_openml(name="wine-quality-white", version=1, as_frame=True)
    data = wine_data.data
    data['quality'] = pd.to_numeric(wine_data.target)

    print(data.head())

    table_name = "WINE_QUALITY"
    try:
        print(f"Uploading data to the table...")
        hana_df = dataframe.create_dataframe_from_pandas(connection, data, table_name=table_name, force=True)

    except Exception as e:
        print(f"Failed to upload data: {e}")
        return

    try:
        hana_df = connection.table(table_name)  # query data
        print(f"Data schema: {hana_df.dtypes()}")
    except Exception as e:
        print(f"Failed to query data: {e}")
        return

    features = [col for col in hana_df.columns if col != 'quality']
    target = 'quality'
    # train model
    model = PolynomialRegression(degree=1)  # degree 1 corresponds to linear regression
    model.fit(hana_df, features=features, label=target)
    print("Model trained successfully!")

    # evaluate
    try:
        predictions = model.predict(hana_df).collect()
        print("Sample predictions:")
        print(predictions.head())
    except Exception as e:
        print(f"Failed to evaluate model: {e}")
        return

if __name__ == "__main__":
    main()
