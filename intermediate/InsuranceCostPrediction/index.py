# Insurance Cost Prediction - Regression Project

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1️⃣ Load dataset
data = pd.read_csv("insurance.csv")
print("Dataset loaded")
print(data.head())

# 2️⃣ Encode categorical columns
encoder = LabelEncoder()
categorical_cols = ["sex", "smoker", "region"]

for col in categorical_cols:
    data[col] = encoder.fit_transform(data[col])

# 3️⃣ Split features and target
X = data.drop("charges", axis=1)
y = data["charges"]

# 4️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6️⃣ Predictions
y_pred = model.predict(X_test)

# 7️⃣ Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)
