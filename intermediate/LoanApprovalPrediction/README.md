# Loan Approval Prediction (Intermediate ML)

## 📌 Project Summary
Predict whether a loan application will be approved or rejected based on applicant details using Machine Learning.

## 📁 Dataset
This project uses the **Loan Prediction Problem Dataset** from Kaggle.
It includes:
- `train.csv` → Includes features + target (`Loan_Status`)
- `test.csv`  → Includes only features (predict loan status)

## 🧠 ML Task
Binary Classification using Logistic Regression.

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Scikit-Learn

## 📊 Workflow
1. Load Train + Test data
2. Missing value handling
3. Encode categorical features
4. Train model
5. Predict on test data
6. Save predictions to `loan_predictions.csv`

## 📈 Output
A CSV file with:
- `Loan_ID`
- `Loan_Status` (Y/N)

## 📌 What I Learned
- Handling real train/test splits
- Encoding categorical data
- Model training & evaluation
- Creating a Kaggle submission file
