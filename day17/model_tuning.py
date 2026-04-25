from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer


data = load_breast_cancer()
X, y = data.data, data.target

param_grid = {
'n_estimators': [50, 100, 200],
'max_depth': [None, 10, 20],
'min_samples_split': [2, 5, 10]
}


rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
cv=3, scoring='accuracy', verbose=1)


grid_search.fit(X, y)
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Score:{grid_search.best_score_:.4f}")