# Assg2_SFEN5004
The final project submission for Advanced Internet Technologies (SFEN5004) for UTT MSc. ICT
is a single page web application that uses customized API endpoints. 
To test the application, you must the run the __init__.py file. 
While the debugger is running, open a browser window and navigate to localhost:5000
The main menu on the top bar contains navigation links that would allow a user to browse to the Home page, a Registration page
and the View Open Requests Page.

The endpoints and their uses are defined as follows:

#@api {post} /login
The /login Router routes to a login_handler() which is supposed to retrieve the users' email and password from the form.
It attempts to login the user, querying the User table, filtering the search by the users email and password.
The login function is incomplete. It does not route the user to their main page upon login.

#@api {get} /meetrequests
uses the all_requests_handler() endpoint and returns a Jsonified String of all 'OPEN' Request objects from the 
Request table in the database.

#@api {post} /meetrequests
uses the all_requests_handler() endpoint. It's purpose is to retrieve all request details entered by the user on the
create Request form. It makes use of the both the Google and Foursquare public APIs to retreive the geo-location and 
restaurant name and address to save along with the other Request details.

#@api {get} /meetrequests/<:id>
Uses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and retrieve the specific details of the Request from the database to display to the user

#@api {put} /meetrequests/<:id>
Uses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and update the specific details of the Request from the database to display to the user

#@api {delete} /meetrequests/<:id>
Uses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and delete the specific details of the Request from the database to display to the user

#@api {get} /restaurants
uses the all_restaurants_handler() endpoint and returns a Jsonified String of all Restaurants from the 
Restaurant table in the database.

#@api {post} /restaurants
uses the all_restaurants_handler() endpoint. It's purpose is to retrieve all restaurant details entered by the user on the
create Request form. It makes use of the both the Google and Foursquare public APIs to retreive the geo-location and 
restaurant name and address.

#@api {get} /restaurants/<:id>
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restaurant selected 
from a list and retrieve the specific details of the Restaurant from the database to display to the user

#@api {put} /restaurants/<:id>
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restaurant selected 
from a list and update the specific details of the Restaurant from the database to display to the user

#@api {delete} /restaurants/<:id>
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restuarant selected 
from a list and delete the specific details of the Restaurant from the database to display to the user

#@api {get} /userlist
uses the all_users_handler() endpoint and returns a Jsonified String of all 'Users from the 
user table in the database.

#@api {post} /userlist
uses the all_users_handler() endpoint. It's purpose is to retrieve all user details entered by the user in the 
Registration form.

#@api {get} /userlist/<:id>
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and retrieve the specific details of the User from the database to display to the user

#@api {put} /userlist/<:id>
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and update the specific details of the User from the database to display to the user

#@api {delete} /userlist/<:id>
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and delete the specific details of the user from the database to display to the user


