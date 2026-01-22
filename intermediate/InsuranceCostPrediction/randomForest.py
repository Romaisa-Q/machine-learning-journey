import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1) Load dataset
data = pd.read_csv("insurance.csv")

# 2) Encode categorical variables
data = pd.get_dummies(data, drop_first=True)

# 3) Features & target
X = data.drop("charges", axis=1)
y = data["charges"]

# 4) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5) Random Forest model
model = RandomForestRegressor(
    n_estimators=200,       # number of trees
    max_depth=6,            # control overfitting
    min_samples_leaf=10,    # stable leaves
    random_state=42,
    n_jobs=-1               # use all CPU cores
)

model.fit(X_train, y_train)

# 6) Predictions
y_pred = model.predict(X_test)

# 7) Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
