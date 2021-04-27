import pandas as pd
import regex as re

tgs_cols = {
    "CELEBRATE": "Do you celebrate Thanksgiving?",
    "MAIN_DISH": (
        "What is typically the main dish at "
        "your Thanksgiving dinner?"
    ),
    "HAVE_GRAVY": "Do you typically have gravy?",
    "TYPE_APPLE": (
        "Which type of pie is typically served at your "
        "Thanksgiving dinner? Please select all that apply. - Apple"
    ),
    "TYPE_PUMPKIN":  (
        "Which type of pie is typically served at your "
        "Thanksgiving dinner? Please select all that apply. - Pumpkin"
    ),
    "TYPE_PECAN": (
        "Which type of pie is typically served at your "
        "Thanksgiving dinner? Please select all that apply. - Pecan"
    ),
    "REVENUE": (
        "How much total combined money did all members of your HOUSEHOLD "
        "earn last year?"
    ),
    "TRAVEL": "How far will you travel for Thanksgiving?",
    "MEET_UP": (
        "Have you ever tried to meet up with hometown friends on "
        "Thanksgiving night?"
    ),
    "FRIENDSGIVING": 'Have you ever attended a "Friendsgiving?"'

}

print("----------")
print(" Partie 1")
print("----------")
data = pd.read_csv("donnees/thanksgiving.csv")
print(data.head(2), "\n")
print(data.columns, "\n")

print(
    tgs_cols["MAIN_DISH"],
    "\n",
    data[tgs_cols["CELEBRATE"]].value_counts(),
    "\n"
    )
actual_tgs = data[data[tgs_cols["CELEBRATE"]] == "Yes"]
print(tgs_cols["CELEBRATE"], "= Yes\n", actual_tgs, "\n")

print(
    tgs_cols["MAIN_DISH"],
    "\n",
    actual_tgs[tgs_cols["MAIN_DISH"]].value_counts(),
    "\n"
    )
print(
    tgs_cols["MAIN_DISH"], "= Tofurkey et ",
    tgs_cols["HAVE_GRAVY"], "\n",
    actual_tgs[
        actual_tgs[tgs_cols["MAIN_DISH"]] == "Tofurkey"
    ][tgs_cols["HAVE_GRAVY"]],
    "\n"
    )

apple_isnull = pd.Series(
    list(actual_tgs[tgs_cols["TYPE_APPLE"]].isnull()),
    actual_tgs.RespondentID
    )
print("apple_isnull : \n", apple_isnull, "\n")
pumpkin_isnull = pd.Series(
    list(actual_tgs[tgs_cols["TYPE_PUMPKIN"]].isnull()),
    actual_tgs.RespondentID
    )
print("pumpkin_isnull : \n", pumpkin_isnull, "\n")
pecan_isnull = pd.Series(
    list(actual_tgs[tgs_cols["TYPE_PECAN"]].isnull()),
    actual_tgs.RespondentID
    )
print("pecan_isnull : \n", pecan_isnull, "\n")

pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(pies)
print("Pies : \n", pies.value_counts())

# partie 2
print("----------")
print(" Partie 2")
print("----------")


def age_to_int(age):
    # check if a line is nan, NaN can't be equal to itself
    if age != age:
        return None
    return int(age.split()[0].replace("+", ""))


data["int_age"] = data["Age"].apply(age_to_int)
print("\nQuestion 1 :")
print(data["int_age"].describe())


def revenue_to_int(revenue):
    if revenue != revenue:
        return None
    revenue = re.sub(r'[$,]', '', revenue)
    revenue = revenue.split()[0]
    if revenue == "Prefer":
        return None
    return int(revenue)


data["int_income"] = data[tgs_cols["REVENUE"]].apply(revenue_to_int)
print("\nQuestion 2 :")
print(data["int_income"].describe())

print("\nQuestion 3 :")
lower_than_15 = data["int_income"] < 150000
print("Pour les revenues inférieurs à 150 000 :")
print(data[tgs_cols["TRAVEL"]][lower_than_15].value_counts())
superior_than_15 = data["int_income"] >= 150000
print("Pour les revenues supérieurs à 150 000 :")
print(data[tgs_cols["TRAVEL"]][superior_than_15].value_counts())

print("\nQuestion 4 :")
print("\n1. Pour l'age :")
print(data.pivot_table(
    index=tgs_cols["MEET_UP"],
    columns=tgs_cols["FRIENDSGIVING"],
    values="int_age"
    ))
print("\n2. Pour le revenue :")
print(data.pivot_table(
    index=tgs_cols["MEET_UP"],
    columns=tgs_cols["FRIENDSGIVING"],
    values="int_income"
    ))
