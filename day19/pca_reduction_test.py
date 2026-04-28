import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.data
y = digits.target
pca_full = PCA().fit(X)
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)
n_95 = np.where(cumulative_variance >= 0.95)[0][0] + 1
print(f"Number of components needed to keep 95% info: {n_95}")
plt.plot(cumulative_variance)
plt.axhline(y=0.95, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.show()