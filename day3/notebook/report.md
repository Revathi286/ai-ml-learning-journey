Setup Status
1. VS Code installed and functioning correctly
2. Python environment configured and verified
3. Git initialized and connected to repository
4. Node.js installed and operational


Task Inventory
1. Designed and implemented a structured project directory
2. Developed basics.py to demonstrate Python fundamentals and data processing
3. Implemented NumPy operations including array creation, reshaping, and scaling
4. Created a dataset (data.csv) and performed analysis using Pandas
5. Built a Jupyter Notebook to document learning and explain vectorization concepts


Debugging Log
1. ModuleNotFoundError: No module named 'numpy'
Cause: Required library was not installed in the environment
Solution: Installed NumPy using: pip install numpy

pip install numpy
2. FileNotFoundError while accessing data.csv
Cause: Incorrect relative file path was used while executing the script from the root directory
Solution: Updated file path from "../data/data.csv" to "data/data.csv" to correctly locate the dataset