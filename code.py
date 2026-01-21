import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(os.path.dirname(__file__))

df = pd.read_csv("patient.csv")

df.head()
df.shape
df.columns
df.info()
df.isnull().sum()

df['confirmed_date'] = pd.to_datetime(df['confirmed_date'], errors='coerce')
df['released_date'] = pd.to_datetime(df['released_date'], errors='coerce')
df = df.dropna(subset=['confirmed_date'])

df['age'] = 2020 - df['birth_year']
df['recovery_days'] = (
    df['released_date'] - df['confirmed_date']
).dt.days

print("Q1.")
df['sex'].value_counts()
sns.countplot(x='sex', data=df)
plt.show()
sns.histplot(df['age'], bins=20)
plt.show()

print("Q2.")
plt.figure(figsize=(10, 6))

sns.countplot(
    y='infection_reason',
    data=df,
    order=df['infection_reason'].value_counts().index
)

plt.title("Infection Reasons Distribution")
plt.tight_layout()
plt.show()

plt.savefig("infection_reason.png")
plt.close()


print("Q3.")
df['recovery_days'].mean()

plt.figure(figsize=(8,5))
sns.histplot(df['recovery_days'], bins=20)
plt.title("Recovery Days Distribution")
plt.xlabel("Recovery Days")
plt.ylabel("Number of Patients")
plt.show()


plt.savefig("recovery_days.png")
plt.close()

print("Q4.")
df['region'].value_counts().head(10)
sns.barplot(
    x=df['region'].value_counts().head(10).values,
    y=df['region'].value_counts().head(10).index
)
plt.show()

plt.savefig("region.png")
plt.close()

print("Q5.")
df[['age', 'contact_number', 'infection_order', 'recovery_days']].corr()

from sklearn.linear_model import LinearRegression

df_model = df.dropna(subset=['recovery_days'])

X = df_model[['age', 'contact_number', 'infection_order']].fillna(0)
y = df_model['recovery_days']

model = LinearRegression()
model.fit(X, y)

r2_score = model.score(X, y)

print("R² score:", r2_score)

with open("R2_Result.txt", "w") as file:
    file.write(f"Final R^2 Score for Question 5 (Recovery Time Regression):\n")
    file.write(f"{r2_score:.5f}")