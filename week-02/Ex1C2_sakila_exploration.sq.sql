/*
a)
*/
/*
a) In the actors table it consist of the actorID, frist and last names, and dates that are last updated 
b) In the film table it consist of the title of the movies, the description, when the movies were released, how many rented the movies, what rates the movies gotten, movie rating, and special features 
c) The film_actor table have both columns for actor_ID and film_ID
d) the rental table is simple to read, the information the table gives the rental_ID number, the date start and end date rental, the custmore ID numder, inventory ID number,and staff ID number
e) The inventory table includes the inventory_ID, the film ID, the store ID, and last updated 
f) To find the names of all films rentend on a specific date i would need to use the rental, inventory, and film tables. The rental tables contains the renatl dates which allows you to filter by what date you are interested in, it also has the inventory_ID which connctes to the iventory table. The inventory table tells you what what copy of the films are rented and has the film_ID, the film_ID conncets to the film table the film names are stored. the rental conncets to the inventory table using inventory_ID, and the inventory table conncets to the film table by using the film_ID.  

SELECET rental_date, inventory_ID FROM rental;
SELECT inventory_id, film_ID from inventory; 
SELECT film_ID, title FROM film;
