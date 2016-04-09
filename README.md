# Assg2_SFEN5004
The final project submission for Advanced Internet Technologies (SFEN5004) for UTT MSc. ICT
is a single page web application that uses customized API endpoints. 
To test the application, you must the run the __init__.py file. 
While the debugger is running, open a browser window and navigate to localhost:5000
The main menu on the top bar contains navigation links that would allow a user to browse to the Home page, a Registration page
and the View Open Requests Page.

The endpoints and their uses are defined as follows:

#@api {post} /login
#@apiName login_handler
#@apiGroup User
#@apiParam {int} id Users unique ID.
#@apiSuccess {String} ID, Email, Password of the User.
#@apiError {String} - Error Unable to retrieve person.
The /login Router routes to a login_handler() which is supposed to retrieve the users' email and password from the form.
It attempts to login the user, querying the User table, filtering the search by the users email and password.
The login function is incomplete. It does not route the user to their main page upon login.

#@api {get} /meetrequests
#@apiDescription - Retrieves all Meeting Requests from the DB to display on the Request List Template
Uses the all_requests_handler() endpoint and returns a Jsonified String of all 'OPEN' Request objects from the 
Request table in the database.

#@api {post} /meetrequests
#@apiDescription - Retrieves Meeting Request Details from the Form and Persists to the Request Table in DB. This API consumes both the Foursquare and Google Public APIs
#@apiName all_requests_handler
#@apiGroup User
#@apiParam {int} [requestorID]   ID of requestor (should be retrieved from session Auth Token)
#@apiParam {String} [location]   Preferred location for the meeting Request
#@apiParam {String} [mealType]   Preferred meal type for the meeting Request 
#@apiParam {String} [mealTime]   Preferred meal time for the meeting Request e.g. Dinner
#@apiSuccess {String} Jsonified String representing the Request.
#@apiError {String} - Error Meeting Request Has Not Been Saved.
Uses the all_requests_handler() endpoint. It's purpose is to retrieve all request details entered by the user on the
create Request form. It makes use of the both the Google and Foursquare public APIs to retreive the geo-location and 
restaurant name and address to save along with the other Request details.

#@api {get} /meetrequests/<:id>
#@apiName single_request_handler()
#@apiDescription -   Retrieves Information on a Specific Meeting Request 
#@apiSuccessExample  Success-Response:
#     HTTP/1.1 200 OK
#     {
#	       "firstname": "John",
#	       "lastname": "Doe"
#	     }
Uses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and retrieve the specific details of the Request from the database to display to the user

#@api {put} /meetrequests/<:id>
#@apiName single_request_handler()
#@apiDescription - Updates the Meeting Request that matches a specific ID
#@apiGroup User
Uses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and update the specific details of the Request from the database to display to the user

#@api {delete} /meetrequests/<:id>

#@apiName single_request_handler()
#@apiDescription - Deletes the Meeting Request that matches a specific ID
#@apiGroup UserUses the single_request_handler() endpoint. Its intent is to retrieve the data-id value of the Request selected 
from a list and delete the specific details of the Request from the database to display to the user

#@api {get} /restaurants
#@apiName all_restaurants_handler()
#@apiDescription - Retrieves all Restaurants from the DB to display in the Template
uses the all_restaurants_handler() endpoint and returns a Jsonified String of all Restaurants from the 
Restaurant table in the database.

#@api {post} /restaurants
#@apiName all_restaurants_handler()
#@apiDescription - Retrieves restaurant details from the form and persists to the Restaurant table in the DB
#@apiGroup User
#@apiParam {String} [location]   Location Preference
#@apiParam {String} [mealType]   Meal type Preference 
#@apiSuccess {String} Jsonified String representing the Restaurant.
#@apiError {String} - Error No Restaurant found for 'mealType' and 'location'.
uses the all_restaurants_handler() endpoint. It's purpose is to retrieve all restaurant details entered by the user on the
create Request form. It makes use of the both the Google and Foursquare public APIs to retreive the geo-location and 
restaurant name and address.

#@api {get} /restaurants/<:id>
#@apiName single_restaurant_handler()
#@apiDescription -   Retrieves Information on a Specific Restaurant 
#@apiSuccessExample  Success-Response:
#      HTTP/1.1 200 OK
#	     {
#	       "id" : "Id of Restaurant",
#	       "address": "Address of Restaurant returned from Public API",
#	       "image": "Pic of Restaurant returned from Public API",
#	       "name" : "Name of Restaurant"
#	     }
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restaurant selected 
from a list and retrieve the specific details of the Restaurant from the database to display to the user

#@api {put} /restaurants/<:id>
#@apiName single_restaurant_handler()
#@apiDescription - Updates the Restaurant that matches a specific ID
#@apiGroup User
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restaurant selected 
from a list and update the specific details of the Restaurant from the database to display to the user

#@api {delete} /restaurants/<:id>
#@apiName single_request_handler()
#@apiDescription - Deletes the Restaurant that matches a specific ID
#@apiGroup User
Uses the single_restaurant_handler() endpoint. Its intent is to retrieve the data-id value of the Restuarant selected 
from a list and delete the specific details of the Restaurant from the database to display to the user

#@api {get} /userlist
#@apiName all_users_handler()
#@apiDescription - Retrieves all Users from the DB to display in the Template
uses the all_users_handler() endpoint and returns a Jsonified String of all 'Users from the 
user table in the database.

#@api {post} /userlist
#@apiName all_users_handler()
#@apiDescription - Retrieves New User details from the form and persists to the Restaurant table in the DB
#@apiGroup User
#@apiParam {String} [alias]      Alias for the new user
#@apiParam {String} [password]   Password for the new user which will be hashed and stored in the DB
#@apiParam {String} [email]      Email for the new user 
#@apiSuccess {String} Jsonified String representing the new User.
uses the all_users_handler() endpoint. It's purpose is to retrieve all user details entered by the user in the 
Registration form.

#@api {get} /userlist/<:id>
#@apiName single_user_handler()
#@apiDescription -   Retrieves Information on a Specific User 
#@apiSuccessExample  Success-Response:
#	      HTTP/1.1 200 OK
#	     {
#	       "id" : "Id of User",
#	       "alias": "User Alias",
#	       "password": "User Hashed Password",
#	       "email" : "Email of User"
#	     }
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and retrieve the specific details of the User from the database to display to the user

#@api {put} /userlist/<:id>
#@apiName single_restaurant_handler()
#@apiDescription - Updates the User that matches a specific ID
#@apiGroup User
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and update the specific details of the User from the database to display to the user

#@api {delete} /userlist/<:id>
#@apiName single_request_handler()
#@apiDescription - Deletes the User that matches a specific ID
#@apiGroup User
Uses the single_user_handler() endpoint. Its intent is to retrieve the data-id value of the User selected 
from a list and delete the specific details of the user from the database to display to the user


