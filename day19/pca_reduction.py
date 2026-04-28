import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import pandas as pd
digits = load_digits()
X = digits.data
y = digits.target
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"Variance retained by 2 components:{sum(pca.explained_variance_ratio_)*100:.2f}%")
plt.figure(figsize=(10, 7))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis',
s=20)
plt.colorbar(label='Digit Class')
plt.title("Digits Dataset Projected into 2D Space via PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()