import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1) Load dataset
data = pd.read_csv("house_prices.csv")

# 2) Drop useless column
data = data.drop("Id", axis=1)

# 3) Convert categorical columns to numbers
data = pd.get_dummies(data, drop_first=True)

# 4) Separate features & target
X = data.drop("Price", axis=1)
y = data["Price"]

# 5) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6) Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 7) Predictions
y_pred = model.predict(X_test)

# 8) Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
