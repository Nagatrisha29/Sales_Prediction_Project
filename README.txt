==============================
SALES PREDICTION PROJECT
==============================

Project Overview:
-----------------
This project predicts product sales using Machine Learning techniques in Python.
It analyzes advertising expenditure (TV, Radio, Newspaper) to forecast future sales.

The model helps businesses:
- Optimize advertising budget
- Improve marketing strategy
- Increase revenue
- Make data-driven decisions


Project Structure:
------------------

Sales_Prediction_Project/
│
├── main.py
├── README.txt
├── data/
│     └── sales_data.csv
├── src/
│     ├── load_data.py
│     ├── visualization.py
│     ├── model.py
│     └── evaluate.py


Requirements:
-------------
Make sure Python is installed.

Install required libraries using:

pip install pandas numpy matplotlib seaborn scikit-learn


How to Run the Project:
-----------------------

1. Open VS Code
2. Open the folder: Sales_Prediction_Project
3. Open Terminal in VS Code
4. Run the command:

   python main.py

5. The model will:
   - Load dataset
   - Show visualizations
   - Train the model
   - Evaluate performance


Dataset:
--------
The dataset file must be placed inside the "data" folder:

data/sales_data.csv

Make sure the file name matches exactly.


Model Used:
-----------
Linear Regression (from sklearn)


Evaluation Metrics:
--------------------
- R2 Score
- Mean Squared Error (MSE)


Common Errors & Fixes:
----------------------

1. ModuleNotFoundError
   -> Run: python -m pip install library_name

2. FileNotFoundError
   -> Ensure sales_data.csv is inside the data folder

3. Python not recognized
   -> Reinstall Python and check "Add to PATH"


Author:
-------
RAVIPATI NAGATRISHA


==============================
End of File
==============================