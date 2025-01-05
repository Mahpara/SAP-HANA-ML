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

    # Step 4: Query and prepare data for training
    try:
        print(f"Querying data from table '{table_name}'...")
        hana_df = connection.table(table_name)
        print(f"Data schema: {hana_df.dtypes()}")
    except Exception as e:
        print(f"Failed to query data: {e}")
        return

    # Step 5: Split data into features and target
    features = [col for col in hana_df.columns if col != 'quality']
    target = 'quality'

    # Step 6: Train a Polynomial Regression model
    print("Training Polynomial Regression model...")
    model = PolynomialRegression(degree=1)  # Degree 1 corresponds to linear regression
    model.fit(hana_df, features=features, label=target)
    print("Model trained successfully!")

    # Step 7: Evaluate the model
    try:
        predictions = model.predict(hana_df).collect()
        print("Sample predictions:")
        print(predictions.head())
    except Exception as e:
        print(f"Failed to evaluate model: {e}")
        return

if __name__ == "__main__":
    main()
