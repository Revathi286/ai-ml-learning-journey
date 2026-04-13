 Day 4 Report – Pre-processing Protocol

🔹 Technical Summary
Today, I worked on **data preprocessing techniques** which are crucial before building any Machine Learning model.

I learned:
- Handling missing data using **Pandas (Imputation)**
- Filling missing values using:
  - Mean (for numerical data like Age)
  - Default values (for Score)
- Feature Scaling using **MinMaxScaler (Scikit-Learn)**
- Data Visualization using **Seaborn Heatmaps**

These steps ensure that the dataset is clean, consistent, and ready for model training.



🔹 Bug Log
**Issue Faced:**
While running the scaling code, I got an error:
`ModuleNotFoundError: No module named 'sklearn'`

Fix:
I realized that Scikit-Learn was not installed in my environment.

Solution:
I installed it using:
pip install scikit-learn