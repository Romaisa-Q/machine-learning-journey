import pandas as pd
data=pd.read_csv('data.csv')
print("Data from CSV file:\n")
print(data)
print("\nColumns:")
print(data.columns)
print("\nFirst 5 rows:")
print(data.head(5)) #head() → first 5 rows dikhata hai   “Sirf upar wali 5 rows dikhao”
print("\nTotal students:", len(data))
avg_maths = data['maths'].mean()#.mean() → average nikalna    “Maths marks ka average batao”
print("\nAverage Maths score:", avg_maths)
topper = data.loc[data['maths'].idxmax()]#.idxmax() → jiski sabse badi value hai uska index nikalta hai   “Maths mein highest marks kisne laaye?” loc[] → us row ka poora record “Maths topper ka poora data dikhao”
print("\nTopper in Maths:")
print(topper)
