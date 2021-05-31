from sqlalchemy import create_engine
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem
import requests
import json

GOOGLE_KEY_API = "AIzaSyBk0zyeV9FlFSoknxN2CPneVwc1VntBSqY"

def connect_db(username='', password='', host='localhost', dbname=''):
    return create_engine(f"mysql://{username}:{password}@{host}/{dbname}?charset=utf8mb4")

config_file = "dbconfig.json"
config = None
with open(config_file, "r") as f:
    config = json.load(f)

db = connect_db(**config)


class Customer():
    def __init__(self, customer_id=None, store_id=None, first_name="", last_name="", email="", address_id=None, active=True, create_date=None, last_update=None) -> None:
        self.customer_id = customer_id
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.store_id = store_id
        self.address_id = address_id
        self.active = active
        self.create_date = create_date
        self.last_update = last_update
    def __repr__(self) -> str:
        return f"(firstname:{self.firstname}, lastname:{self.lastname}, email:{self.email}, store: {self.store_id})"
    def __str__(self) -> str:
        return (
            f"Prénom : {self.firstname}\n"
            f"Nom : {self.lastname}\n"
            f"email : {self.email}\n"
        )


class Address():
    def __init__(self, address_id=None, address="", complement_address="", phone="", district="", postal_code="", location="", create_date=None, last_update=None) -> None:
        self.address_id = address_id
        self.address = address
        self.complement_address = complement_address
        self.postal_code = postal_code
        self.district = district
        self.location = location
        self.phone = phone
        self.city_id = None
        self.create_date = create_date
        self.last_update = last_update
    def __str__(self) -> str:
        return (
            f"Addresse : {self.address}\n"
            f"Complement : {self.complement_address}\n"
            f"Code Postal : {self.postal_code}\n"
            f"District : {self.district}\n"
            f"Location : {self.location}\n"
            f"Phone : {self.phone}\n"
        )


class City():
    def __init__(self, city_id=None, city="", country_id=None, create_date=None, last_update=None) -> None:
        self.city_id = city_id
        self.city = city
        self.country_id = country_id
        self.create_date = create_date
        self.last_update = last_update
    def __str__(self) -> str:
        return (
            f"Ville : {self.city}"
        )


class Country():
    def __init__(self, country_id=None, country="", create_date=None, last_update=None) -> None:
        self.country = country
        self.country_id = country_id
        self.create_date = create_date
        self.last_update = last_update
    def __str__(self) -> str:
        return (
            f"Pays : {self.country}"
        )


def insert_customer(customer: Customer, address: Address, city: City, country: Country):
    if country.country == '':
        raise ValueError("You need to provide a country")
    if city.city == '':
        raise ValueError("You need to provide a city")
    with db.connect() as connection:
        if country.country_id is None:
            result = db.execute("SELECT country_id FROM country WHERE country = '%s'" % (
                country.country)).fetchone()
            if result is None:
                result = db.execute(
                    "INSERT INTO country (country) VALUES ('%s')" % (country.country))
                city.country_id = last_insert_id(db)
            else:
                city.country_id = result['country_id']
        else:
            city.country_id = country.country_id
        result = db.execute(
            "SELECT city_id FROM city WHERE city = '%s'" % (city.city)).fetchone()
        if result is None:
            result = db.execute(
                "INSERT INTO city (city, country_id) VALUES ('%s', '%d')" % (city.city, city.country_id))
            address.city_id = last_insert_id(db)
        else:
            address.city_id = result['city_id']
        with connection.begin():
            connection.execute("INSERT INTO address (address, address2, district, city_id, postal_code, phone, location) VALUES ('%s', '%s', '%s', '%d', '%s', '%s', ST_GeomFromText('POINT(%s)'))" % (
                address.address, address.complement_address, address.district, address.city_id, address.postal_code, address.phone, address.location))
            customer.address_id = last_insert_id(connection)
            connection.execute("INSERT INTO customer (store_id, first_name, last_name, email, address_id) VALUES ('%d', '%s', '%s', '%s', '%d')"%(customer.store_id, customer.firstname, customer.lastname, customer.email, customer.address_id))
        
def last_insert_id(connection):
    result = connection.execute("SELECT LAST_INSERT_ID();").fetchone()
    return int(result[0])


def new_customer():
    customer = Customer()
    address = Address()
    city = City()
    country = Country()
    stores = db.execute("SELECT * FROM store INNER JOIN address USING(address_id)").fetchall()
    countries = db.execute("SELECT * FROM country").fetchall()
    store_names = []
    if stores is None:
        raise ValueError("Couldn't get stores from database")
    for store in stores:
        store_names.append(store["address"])
    store_selected = SelectionMenu.get_selection(store_names, title="Sélectionner un Magasin", show_exit_option=False)

    customer.store_id = int(stores[store_selected]["store_id"])
    print(f"Magasin sélectionné : {store_names[store_selected]}")
        
    customer.firstname = input("Prénom : ")
    customer.lastname = input("Nom de Famille : ")
    customer.email = input("Addresse e-mail : ")


    address.phone = input("Téléphone : ")
    address.address = input("Adresse : ")
    address.complement_address = input("Complément adresse : ")
    address.postal_code = input("Code Postal : ")
    city.city = input("Ville : ")
    address.district = input("District : ")
    # Recuperation du pays
    if countries is not None:
        country_menu = SelectionMenu([ctr["country"] for ctr in countries], title="Sélectionner un pays", exit_option_text="Entrer manuellement")
        country_menu.show()
        if country_menu.selected_option < len(countries):
            country.country_id = int(countries[country_menu.selected_option]["country_id"])
            country.country = countries[country_menu.selected_option]["country"]
    if country.country_id is None:
        country.country = input("Pays : ")

    # Position geographique
    rq = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address.address},{address.postal_code} {city.city},{country.country}&key={GOOGLE_KEY_API}')
    if rq.status_code == 200:
        response = rq.json()
        if response['status'] == "OK":
            menu = SelectionMenu([addr['formatted_address'] for addr in response['results']], exit_option_text="Entrer manuellement")
            menu.show()
            if menu.selected_option < len(response['results']):
                address.location = f"{response['results'][menu.selected_option]['geometry']['location']['lat']} {response['results'][menu.selected_option]['geometry']['location']['lng']}"
        else:
            print(response)
    if address.location == "":
        address.location = input("Position géographique (LAT LONG) : ")
    
    print("Avant d'insérer, confirmer les données :")
    print(f"Magasin sélectionné : {store_names[store_selected]}")
    print(customer)
    print(address)
    print(city)
    print(country)
    if input("Confirmer ? (y/N)") == "y":
        insert_customer(customer, address, city, country)
        print("Client ajouté !")
        input("Taper pour continuer...")

def find_customers(name: str = "") -> list[Customer]:
    where = f" WHERE first_name REGEXP '{name}' OR last_name REGEXP '{name}'" if name != '' else ''
    result = db.execute(f"SELECT * FROM customer{where}")
    if result is None:
        return []
    customers: list[Customer] = []
    for data in result:
        customers.append(Customer(**data))
    return customers
    
def ask_client() -> Customer:
    name = input('Rechercher un client :')
    customers = find_customers(name)
    if len(customers) == 0:
        print('Aucun clients trouvés')
        return ask_client()
    menu = SelectionMenu([f"{customer.firstname} {customer.lastname}" for customer in customers], exit_option_text="Nouvelle recherche")
    menu.show()
    selection = menu.selected_option
    if selection == len(customers):
        return ask_client()
    return customers[selection]

def find_rentals():
    customer = ask_client()
    rentals = pd.read_sql_query(f"SELECT rental_id, inventory_id, film_id, title, rental_date FROM rental INNER JOIN inventory USING(inventory_id) INNER JOIN film USING (film_id) WHERE customer_id='{customer.customer_id}'", db)
    print(f"Client : {customer.firstname} {customer.lastname}")
    print(rentals)
    input("Taper pour continuer...")

def generate_graphs():
    rentals = pd.read_sql_query(f"SELECT * FROM rental INNER JOIN payment USING(rental_id) INNER JOIN inventory USING(inventory_id) INNER JOIN film USING(film_id) WHERE YEAR(rental_date) = '2005'", db)
    rentals["Month"] = rentals.rental_date.dt.month
    rentals_by_month = rentals.groupby('Month')
    plt.figure(figsize=[15,5])
    plt.subplot(131)
    total_rentals = rentals_by_month["film_id"].count()
    total_rentals.plot(kind="bar")
    plt.title("Location par mois en 2005")
    plt.xlabel("Mois de l'année")
    plt.ylabel("Nombre de locations")
    plt.subplot(132)
    rentals_by_month['amount'].sum().plot()
    plt.title("Chiffre d'affaire mensuel 2005")
    plt.xlabel("Mois de l'année")
    plt.ylabel("Revenus")
    plt.subplot(133)
    sn.histplot(rentals, x="Month", hue="store_id")
    plt.show()


if __name__ == "__main__":
    menu = ConsoleMenu("Programme Magasin")
    menu.append_item(FunctionItem("Afficher les locations d'un client", find_rentals))
    menu.append_item(FunctionItem("Ajouter un client", new_customer))
    menu.append_item(FunctionItem("Statistiques", generate_graphs))
    menu.show()
