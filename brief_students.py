import numpy as np
import pandas as pd


def compute_total_students(df):
    return df.groupby("Major_category")["Total"].sum().to_dict()


all_ages = pd.read_csv("donnees/all-ages.csv")
recent_grades = pd.read_csv("donnees/recent-grads.csv")

print("First 5 values (all-ages) : \n", all_ages.head(5), "\n")
print("First 5 values (recent-grads) : \n", recent_grades.head(5), "\n")

print("All Ages unique MC : ", all_ages["Major_category"].unique(), "\n")
print("Recent Grades unique MC : ", recent_grades["Major_category"].unique(), "\n")

aa_cat_counts = compute_total_students(all_ages)
rg_cat_counts = compute_total_students(recent_grades)

print("aa_cat_counts : ", aa_cat_counts, "\n")
print("rg_cat_counts : ", rg_cat_counts, "\n")

low_wage_proportion = recent_grades["Low_wage_jobs"].sum() / recent_grades["Total"].sum()
print(f"low_wage_proportion : {low_wage_proportion * 100: 2.3f}%\n")
print(set(all_ages["Major"].unique()) - set(recent_grades["Major"].unique()))

rg_lower_count = 0
for cat in recent_grades["Major"].unique():
    aa_cat = all_ages[all_ages["Major"] == cat]
    rg_cat = recent_grades[recent_grades["Major"] == cat]
    if len(rg_cat) == 0 or len(aa_cat) == 0:
        continue
    if rg_cat["Unemployment_rate"].values[0] < aa_cat["Unemployment_rate"].values[0]:
        rg_lower_count += 1
print("rg_lower_count : ", rg_lower_count)
