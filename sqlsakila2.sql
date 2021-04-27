SET lc_time_names = 'fr_FR';
# Question 1
SELECT MONTHNAME(rental_date) as mois 
FROM rental 
WHERE year(rental_date) = 2006;
# Question 2a
# SELECT rental_duration 
# FROM film;
# Question 2b
SELECT f.title, TIMEDIFF(return_date, rental_date) as rental_duration_hours 
FROM rental 
INNER JOIN inventory iv ON iv.inventory_id = rental.inventory_id 
INNER JOIN film f ON f.film_id = iv.film_id;
# Question 3
SELECT f.title, f.description, DATE_FORMAT(rental.rental_date, "%W %D %M %Y à %H heures %i minutes et %s secondes") as dateformat 
FROM rental 
INNER JOIN inventory inv ON inv.inventory_id = rental.inventory_id
INNER JOIN film f ON f.film_id = inv.film_id 
WHERE HOUR(rental_date) < 1 and YEAR(rental_date) = 2005;
# Question 4
SELECT f.title, f.description, rental_date 
FROM rental 
INNER JOIN inventory inv ON inv.inventory_id = rental.inventory_id
INNER JOIN film f ON f.film_id = inv.film_id 
WHERE MONTH(rental_date) BETWEEN 4 AND 5;
# Question 5a
SELECT title 
FROM film 
WHERE LOWER(title) REGEXP "^(?!le).+$";
# Question 5b (avec "le ")
SELECT title 
FROM film 
WHERE LOWER(title) REGEXP "^(?!le ).+$";
# Question 6
SELECT title, IF(rating = "NC-17", "oui", "non") as is_nc_17 
FROM film 
WHERE rating IN ("PG-13", "NC-17");
# Question 7
SELECT * 
FROM category 
WHERE LOWER(name) REGEXP "^[a|c]";
# Question 8
SELECT substr(name, 1, 3) as short 
FROM category;
# Question 9
SELECT REPLACE(UPPER(first_name), "A", "E"), last_name 
FROM actor 
ORDER BY last_name ASC;
# Question 10
SELECT title, lang.name 
FROM film 
INNER JOIN language lang ON lang.language_id = film.language_id 
LIMIT 10;
# Question 11
SELECT f.title, a.first_name, a.last_name, f.release_year 
FROM actor a 
INNER JOIN film_actor fa ON fa.actor_id = a.actor_id 
INNER JOIN film f ON f.film_id = fa.film_id 
WHERE UPPER(a.first_name) = "JENNIFER" AND UPPER(a.last_name) = "DAVIS" AND f.release_year = "2006";
# Question 12
SELECT c.first_name, c.last_name 
FROM film f 
INNER JOIN inventory iv ON iv.film_id = f.film_id 
INNER JOIN rental rt ON rt.inventory_id = iv.inventory_id 
INNER JOIN customer c ON c.customer_id = rt.customer_id 
WHERE f.title = "ALABAMA DEVIL";
# Question 13
SELECT DISTINCT(f.title) 
FROM city ct 
INNER JOIN address addr ON addr.city_id = ct.city_id 
INNER JOIN customer c ON c.address_id = addr.address_id 
INNER JOIN rental rt ON rt.customer_id = c.customer_id 
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id 
INNER JOIN film f ON f.film_id = iv.film_id 
WHERE ct.city = "Woodridge";
# Question 14
SELECT DISTINCT(f.title), rt.rental_date, rt.return_date, TIMEDIFF(rt.return_date, rt.rental_date) as duration 
FROM rental rt 
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id 
INNER JOIN film f ON f.film_id = iv.film_id 
WHERE rt.return_date IS NOT NULL 
ORDER BY duration ASC, f.title ASC 
LIMIT 10;
# Question 15
SELECT f.title, c.name 
FROM category c 
INNER JOIN film_category fc ON fc.category_id = c.category_id 
INNER JOIN film f ON f.film_id = fc.film_id
WHERE c.name = "Action" 
ORDER BY f.title ASC;
# Question 16
SELECT DISTINCT(f.title), rt.rental_date, rt.return_date, (timestampdiff(SECOND, rt.rental_date, rt.return_date) / 3600) as duration 
FROM rental rt 
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id 
INNER JOIN film f ON f.film_id = iv.film_id 
WHERE rt.return_date IS NOT NULL AND timestampdiff(HOUR, rt.rental_date, rt.return_date) < 48 
ORDER BY duration ASC, f.title ASC;

# Pour aller plus loin
# 1
SELECT c.first_name, c.last_name, f.title, st.store_id, addr.address, TIMEDIFF(rt.return_date, rt.rental_date) as duration
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id
INNER JOIN customer c ON c.customer_id = rt.customer_id
INNER JOIN store st ON st.store_id = iv.store_id
INNER JOIN address addr ON addr.address_id = st.address_id
ORDER BY duration DESC, c.last_name ASC
LIMIT 10;

# 2
SELECT c.first_name, c.last_name, sum(p.amount) as total_amount
FROM payment p
INNER JOIN customer c ON c.customer_id = p.customer_id
GROUP BY p.customer_id
ORDER BY c.last_name;

# 3
SELECT f.title, (AVG(timestampdiff(SECOND, rt.rental_date, rt.return_date)) / (3600 * 24)) as moyenne_duree
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id
WHERE rt.return_date IS NOT NULL
GROUP BY f.film_id
ORDER BY moyenne_duree DESC;
SELECT f.title, AVG(TIMEDIFF(rt.return_date, rt.rental_date)) as moyenne_duree
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id
WHERE rt.return_date IS NOT NULL
GROUP BY f.film_id
ORDER BY moyenne_duree DESC;
# 4a
SELECT * 
FROM film 
WHERE film_id NOT IN (
SELECT iv.film_id 
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
) 
ORDER BY title;

#4b
SELECT f.title, COUNT(rt.rental_id) as nb_rent
FROM inventory iv
RIGHT JOIN film f USING(film_id)
LEFT JOIN rental rt USING(inventory_id)
GROUP BY f.film_id
HAVING nb_rent = 0;


# 5
SELECT s.store_id, addr.address, COUNT(s.staff_id) as nb_employee
FROM staff s
INNER JOIN store st ON st.store_id = s.store_id
INNER JOIN address addr ON addr.address_id = st.address_id 
GROUP BY s.store_id;

# 6
SELECT ct.city_id, ct.city, COUNT(addr.address) as nb_store
FROM store st 
INNER JOIN address addr ON addr.address_id = st.address_id
INNER JOIN city ct ON ct.city_id = addr.city_id
GROUP BY ct.city_id
ORDER BY nb_store DESC 
LIMIT 10;

# 7 
SELECT f.title, f.length
FROM actor a
INNER JOIN film_actor fa ON fa.actor_id = a.actor_id
INNER JOIN film f ON f.film_id = fa.film_id
WHERE LOWER(a.first_name) = "johnny" AND LOWER(a.last_name) = "lollobrigida"
ORDER BY f.length DESC, f.title ASC 
LIMIT 1;

# 8
SELECT f.film_id, f.title, (AVG(timestampdiff(SECOND, rt.rental_date, rt.return_date)) / (3600 * 24)) as moyenne_location
FROM film f
INNER JOIN inventory iv ON iv.film_id = f.film_id
INNER JOIN rental rt ON rt.inventory_id = iv.inventory_id
WHERE LOWER(f.title) = "academy dinosaur" AND rt.return_date IS NOT NULL
GROUP BY f.film_id, f.title;

# 9a
SELECT * 
FROM (
SELECT iv.film_id, iv.store_id, f.title, COUNT(*) as nb_exemplaire
FROM inventory iv
INNER JOIN film f ON f.film_id = iv.film_id
GROUP BY iv.store_id, iv.film_id
) s2
WHERE s2.nb_exemplaire > 2;

# 9b
SELECT iv.film_id, iv.store_id, f.title, COUNT(*) as nb_exemplaire
FROM inventory iv
INNER JOIN film f ON f.film_id = iv.film_id
GROUP BY iv.store_id, iv.film_id
HAVING nb_exemplaire > 2;

# 10
SELECT * 
FROM film 
WHERE LOWER(title) REGEXP "din"
ORDER BY title ASC;

# 11
SELECT f.film_id, f.title, COUNT(rt.rental_id) as nb_rentals
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id 
GROUP BY f.film_id
ORDER BY nb_rentals DESC 
LIMIT 5;

# 12
SELECT * 
FROM film 
WHERE release_year IN (2003, 2005, 2006)
ORDER BY release_year ASC, title ASC;

# 13 
SELECT rt.rental_id, rt.rental_date, f.title, c.first_name, c.last_name
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id 
INNER JOIN customer c ON c.customer_id = rt.customer_id 
WHERE rt.return_date IS NULL
ORDER BY rt.rental_date ASC, f.title ASC
LIMIT 10;

# 14 
SELECT * 
FROM category c 
INNER JOIN film_category fc ON fc.category_id = c.category_id
INNER JOIN film f ON f.film_id = fc.film_id
WHERE LOWER(c.name) = "action"
ORDER BY f.title ASC;

# 15
SELECT DISTINCT(CONCAT(c.first_name, " ", c.last_name)) as customer_name
FROM film f
INNER JOIN inventory iv ON iv.film_id = f.film_id
INNER JOIN rental rt ON rt.inventory_id = iv.inventory_id 
INNER JOIN customer c ON c.customer_id = rt.customer_id 
WHERE f.rating = "NC-17" 
ORDER BY customer_name;

# 16a (langues originelles)
SELECT * 
FROM category c 
INNER JOIN film_category fc ON fc.category_id = c.category_id
INNER JOIN film f ON f.film_id = fc.film_id
INNER JOIN language lg ON lg.language_id = f.original_language_id
WHERE LOWER(c.name) = "animation" AND LOWER(lg.name) = "english";

# 16b (pour les langues pas originelles)
SELECT * 
FROM category c 
INNER JOIN film_category fc ON fc.category_id = c.category_id
INNER JOIN film f ON f.film_id = fc.film_id
INNER JOIN language lg ON lg.language_id = f.language_id
WHERE LOWER(c.name) = "animation" AND LOWER(lg.name) = "english";

# 17a
SELECT f.title
FROM actor a
INNER JOIN film_actor fa USING(actor_id)
INNER JOIN film f USING(film_id)
WHERE LOWER(a.first_name) = "jennifer"
ORDER BY f.title ASC;

# 17b1
SELECT * 
FROM actor a
INNER JOIN film_actor fa USING(actor_id)
INNER JOIN film f USING(film_id)
WHERE LOWER(a.first_name) = "johnny" AND f.film_id IN 
(
SELECT f.film_id
FROM actor a
INNER JOIN film_actor fa USING(actor_id)
INNER JOIN film f USING(film_id)
WHERE LOWER(a.first_name) = "jennifer"
);

# 17b2
SELECT f.film_id, f.title, IF(COUNT(*) = 2, "oui", "non") as is_duo
FROM actor a
INNER JOIN film_actor fa USING(actor_id)
INNER JOIN film f USING(film_id)
WHERE LOWER(a.first_name) IN ("jennifer", "johnny")
GROUP BY f.film_id
HAVING is_duo = "oui"
ORDER BY f.film_id;

# 18
SELECT c.name, COUNT(*) as nb_rental_by_cat
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN film f ON f.film_id = iv.film_id 
INNER JOIN film_category fc ON fc.film_id = f.film_id
INNER JOIN category c ON c.category_id = fc.category_id
GROUP BY c.category_id 
ORDER BY nb_rental_by_cat DESC 
LIMIT 3;

# 19
SELECT ct.city, COUNT(*) as nb_rental_by_cit
FROM rental rt
INNER JOIN inventory iv ON iv.inventory_id = rt.inventory_id
INNER JOIN store st ON st.store_id = iv.store_id 
INNER JOIN address addr ON addr.address_id = st.address_id
INNER JOIN city ct ON ct.city_id = addr.city_id
GROUP BY ct.city_id 
ORDER BY nb_rental_by_cit DESC 
LIMIT 10;

# 19b: version avec la ville des clients
SELECT ct.city, COUNT(*) as nb_rental_by_cit
FROM rental rt
INNER JOIN customer c ON c.customer_id = rt.customer_id
INNER JOIN address addr ON addr.address_id = c.address_id
INNER JOIN city ct ON ct.city_id = addr.city_id
GROUP BY ct.city_id 
ORDER BY nb_rental_by_cit DESC 
LIMIT 10;

# 20
SELECT a.actor_id, a.first_name, a.last_name, COUNT(*) as nb_movie_acted 
FROM film_actor fa
INNER JOIN actor a ON a.actor_id = fa.actor_id 
GROUP BY a.actor_id 
# HAVING nb_movie_acted >= 1 not necessary since film_actor only list association 
ORDER BY nb_movie_acted DESC, a.last_name ASC;

# 21 : Afficher les acteurs qui n'ont joué dans aucun film
SELECT * 
FROM actor 
WHERE actor_id NOT IN (
SELECT DISTINCT(fa.actor_id)
FROM film_actor fa
)
ORDER BY last_name ASC;

# 21 : Afficher les acteurs qui n'ont joué dans aucun film
SELECT * 
FROM actor a
LEFT JOIN film_actor fa USING(actor_id)
WHERE fa.actor_id IS NULL
ORDER BY a.last_name ASC;