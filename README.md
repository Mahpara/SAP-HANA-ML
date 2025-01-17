# Wine Quality Analysis with SAP HANA Integration

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![hana-ml](https://img.shields.io/badge/hana--ml-v2.12-blue?logo=SAP)
![pandas](https://img.shields.io/badge/pandas-v1.5.2-green?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.2-orange?logo=scikit-learn&logoColor=white)
![OpenML](https://img.shields.io/badge/OpenML-D00000?logo=openml&logoColor=white)

## Overview

This repository demonstrates the integration of machine learning workflows using the `hana-ml` library with SAP HANA. The project is organized into two main components:
1. `sap-hana-mock/`: Contains code that simulates the SAP HANA environment, which allows to test and demonstrate ML workflows without needing an actual instance.
2. `sap-hana-instance/`: Contains the actual integration with an SAP HANA instance. It includes the necessary code to connect to SAP HANA, perform analysis, and use machine learning models with the `hana-ml` library. In this version, the model is trained using the **Wine Quality dataset** and utilizes `PolynomialRegression` for predictions.

For more information about the dataset, visit [Wine Quality dataset on OpenML](https://api.openml.org/d/43612).


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mahpara/sap-hana-ml.git
cd sap-hana-ml
```

### 2. Install Dependencies
Install the required libraries for both environments. Navigate to the appropriate folder and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Script
Run the main.py script in the appropriate folder:
```bash
python main.py
```

