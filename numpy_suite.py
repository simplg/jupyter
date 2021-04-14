import numpy as np


def country_consumption(world, country="", year="1989"):
    return world[:, 4][(world[:, 2] == country) & (world[:, 0] == year)].astype(float).sum()


def get_countries_consumption(data, year="1989"):
    countries = np.unique(data[:, 2])
    return {country: country_consumption(data, country) for country in countries}


world_alcohol = np.genfromtxt(
    "donnees/world_alcohol.csv", delimiter=",", skip_header=True, dtype=str
    )

print(world_alcohol)

countries_is_france = world_alcohol[:, 2] == "France"
print(countries_is_france)

countries_france = world_alcohol[countries_is_france]
print(countries_france)
print(countries_france.shape)

countries_is_algeria = world_alcohol[:, 2] == "Algeria"
countries_algeria = world_alcohol[countries_is_algeria]
print(countries_algeria)
print(countries_algeria.shape)

countries_is_1984 = world_alcohol[:, 0] == "1984"
countries_1984 = world_alcohol[countries_is_1984]
print(countries_1984)
print(countries_1984.shape)

is_algeria_1986 = countries_is_algeria & (world_alcohol[:, 0] == "1986")
countries_is_algeria_1986 = world_alcohol[is_algeria_1986]
print(countries_is_algeria_1986)

countries_is_canada = world_alcohol[:, 2] == "Canada"
is_algeria_or_canada = countries_is_algeria | countries_is_canada
print(world_alcohol[is_algeria_or_canada])
print(world_alcohol[is_algeria_or_canada].shape)

world_alcohol_copy = world_alcohol.copy()
#world_alcohol_copy[:, 0][world_alcohol_copy[:, 0] == "1986"] = "2018"
#print(world_alcohol_copy[world_alcohol_copy[:, 0] == "2018"])

is_value_empty = world_alcohol_copy[:, 4] == ""
world_alcohol_copy[:, 4][is_value_empty] = "0"
print(world_alcohol[is_value_empty][0])
print(world_alcohol_copy[is_value_empty][0])

alcohol_consumption = world_alcohol_copy[:, 4].astype(float)
print(alcohol_consumption)

print(alcohol_consumption.sum())
print(alcohol_consumption.mean())

is_1987 = world_alcohol_copy[:, 0] == "1987"
is_canada_1987 = countries_is_canada & is_1987
canada_1987_consumption = (
    world_alcohol_copy[:, 4][is_canada_1987].astype(float)
    )
print(canada_1987_consumption)
print(canada_1987_consumption.sum())
print(canada_1987_consumption.mean())

is_beer = world_alcohol_copy[:, 3] == "Beer"
countries_is_america = world_alcohol_copy[:, 1] == "Americas"
is_america_beer = countries_is_america & is_beer
america_beer_consumption = (
    world_alcohol_copy[:, 4][is_america_beer].astype(float)
    )
print(america_beer_consumption)
print(america_beer_consumption.sum())
print(america_beer_consumption.mean())
print(world_alcohol_copy[countries_is_canada & is_beer])

print(get_countries_consumption(world_alcohol_copy))
countries_consumption = np.array(list(get_countries_consumption(world_alcohol_copy).items()))
maximum = countries_consumption[:, 1].astype(float).max()
print(countries_consumption[countries_consumption[:, 1] == str(maximum)])
