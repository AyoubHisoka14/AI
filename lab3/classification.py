import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Load and explore the dataset
filepath = "tips.csv"
df = pd.read_csv(filepath)
df.dropna(inplace=True)  # Drop missing values


def calculate_mse(X, y, model):
    prediction = model.predict(X)
    mse = np.round(np.mean((prediction - y) ** 2), 2)
    return mse


X, y = df.iloc[:, :-1], df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Baseline Model
models = {'KNeighborsRegressor': KNeighborsRegressor(),
          'LinearRegression': LinearRegression(),
          'DecisionTreeRegressor': DecisionTreeRegressor(),
          'SVR': SVR(),
          'RandomForestRegressor': RandomForestRegressor()
          }

model = RandomForestRegressor()

model.fit(X_train, y_train)
mse_train = calculate_mse(X_train, y_train, model)
mse_test = calculate_mse(X_test, y_test, model)
print(f"{'RandomForestRegressor'}:\n\tMSE (training): "
      f"{mse_train}\n\tMSE (test): {mse_test}.")
