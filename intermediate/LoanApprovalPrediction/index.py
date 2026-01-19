import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1️⃣ Load train + test data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print("Train shape:", train.shape)
print("Test shape:", test.shape)

# 2️⃣ Handle missing values
cols_to_fill_mode = ["Gender", "Married", "Dependents", "Self_Employed", "Loan_Amount_Term", "Credit_History"]
for col in cols_to_fill_mode:
    train[col].fillna(train[col].mode()[0], inplace=True)
    test[col].fillna(test[col].mode()[0], inplace=True)

train["LoanAmount"].fillna(train["LoanAmount"].mean(), inplace=True)
test["LoanAmount"].fillna(test["LoanAmount"].mean(), inplace=True)

# 3️⃣ Encode categorical variables
encoder = LabelEncoder()
cat_cols = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area", "Loan_Status"]
for col in cat_cols:
    train[col] = encoder.fit_transform(train[col].astype(str))

test_cat_cols = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]
for col in test_cat_cols:
    test[col] = encoder.fit_transform(test[col].astype(str))

#  Loan_ID bhi drop karo!
# 4️⃣ Features & target
X = train.drop(["Loan_Status", "Loan_ID"], axis=1)  
y = train["Loan_Status"]

# 5️⃣ Train/validation split (internal)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

#  Standardization add karo!
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# 6️⃣ Train model (max_iter bhi badha do optional)
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# 7️⃣ Validate
val_pred = model.predict(X_val)
print("Validation Accuracy:", accuracy_score(y_val, val_pred))

#  Test IDs pehle save karo!
test_ids = test["Loan_ID"].copy()  

# Phir test se Loan_ID drop karo
test = test.drop("Loan_ID", axis=1)

# Test data bhi scale karo!
test_scaled = scaler.transform(test)

# 8️⃣ Predict on real test set
test_predictions = model.predict(test_scaled)

# 9️⃣ Prepare submission file
output = pd.DataFrame({
    "Loan_ID": test_ids,  # ← Saved IDs use karo
    "Loan_Status": test_predictions
})
output["Loan_Status"] = output["Loan_Status"].map({1: "Y", 0: "N"})
output.to_csv("loan_predictions.csv", index=False)
print("Saved predictions to loan_predictions.csv")