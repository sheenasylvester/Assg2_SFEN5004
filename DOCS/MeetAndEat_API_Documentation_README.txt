THE LOGIN ENDPOINT WAS DESIGNED TO AUTHENTICATE A USER AND TAKES BOTH EMAIL AND PASSWORD CREDENTIALS FROM THE POST
AND CHECKS THE DATABASE TO SEE IF A USER EXISTS THAT MATCHES THE CREDENTIALS SUPPLIED.
'''
	@api {post} /login Authenticates a User, Retrieves Email and Password from the POST
	@apiName login_handler
	@apiGroup User

	@apiParam {} id Users unique ID.

	@apiSuccess {String} ID, Email, Password of the User.
	@apiError {String} - Error Unable to retrieve person.
'''


THE MEETREQUESTS {GET} ENDPOINT WAS DESIGNED TO RETREIVE ALL OPEN MEETING REQUESTS FROM THE DATABASE. 
THE REQUEST TABLE IS QUERIED AND FILTERED BY FILLED='OPEN' TO PULL ONLY REQUESTS THAT HAVE NOT BEEN FILLED
ALL OPEN REQUESTS ARE DISPLAYED BELOW THE MAKE THE REQUEST FORM

THE MEETREQUESTS {POST} ENDPOINT WAS DESIGNED TO RETRIEVE ALL NEW MEETING REQUEST DATA FROM THE FORM
AND COMMIT THE NEW REQUEST DATA TO THE REQUEST TABLE IN THE DATABASE.
'''
	@api {get} /meetrequests 
	@apiDescription - Retrieves all Meeting Requests from the DB to display on the Request List Template

	@api {post} /meetrequests 
	@apiDescription - Retrieves Meeting Request Details from the Form and Persists to the Request Table in DB. This API consumes both the Foursquare and Google Public APIs
	@apiName all_requests_handler
	@apiGroup User

	@apiParam {int} [requestorID]   ID of requestor (should be retrieved from session Auth Token)
	@apiParam {String} [location]   Preferred location for the meeting Request
	@apiParam {String} [mealType]   Preferred meal type for the meeting Request 
	@apiParam {String} [mealTime]   Preferred meal time for the meeting Request e.g. Dinner

	@apiSuccess {String} Jsonified String representing the Request.
	@apiError {String} - Error Meeting Request Has Not Been Saved.
'''


THE MEETREQUESTS/:ID {GET} ENDPOINT WAS CREATED TO RETRIEVE INFORMATION ON A SPECIFIC MEETING REQUEST FOR DISPLAY TO THE USER
THE MEETREQUESTS/:ID {PUT} ENDPOINT WAS CREATED TO ALLOW A USER TO UPDATE INFORMATION ON A SPECIFIC MEETING REQUEST
THE MEET REQUEST/:ID {DELETE} ENDPOINT WAS CREATED TO ALLOW A USER TO DELETE A SPECIFIC MEETING REQUEST MATCHING THE ID
'''
	@api {get} /meetrequests/:id 
	@apiName single_request_handler()
	@apiDescription -   Retrieves Information on a Specific Meeting Request 
	@apiSuccessExample  Success-Response:
	      HTTP/1.1 200 OK
	     {
	       "firstname": "John",
	       "lastname": "Doe"
	     }

	@api {put} /meetrequests /:id
	@apiName single_request_handler()
	@apiDescription - Updates the Meeting Request that matches a specific ID
	@apiGroup User

	@api {delete} /meetrequests /:id
	@apiName single_request_handler()
	@apiDescription - Deletes the Meeting Request that matches a specific ID
	@apiGroup User
'''


THE RESTAURANTS {GET} ENDPOINT WAS CREATED TO RETRIEVE ALL RESTAURANTS AND DISPLAY TO THE USER
THE RESTAURANTS {POST} ENDPOINT WAS CREATED TO RETRIEVE ALL DETAILS FOR A NEW RESTAURANT FROM THE FORM
AND COMMIT THE DETAILS TO THE RESTAURANT TABLE IN THE DATABASE
'''
	@api {get} /restaurants 
	@apiName all_restaurants_handler()
	@apiDescription - Retrieves all Restaurants from the DB to display in the Template

	@api {post} /restaurants 
	@apiName all_restaurants_handler()
	@apiDescription - Retrieves restaurant details from the form and persists to the Restaurant table in the DB
	@apiGroup User

	@apiParam {String} [location]   Location Preference
	@apiParam {String} [mealType]   Meal type Preference 

	@apiSuccess {String} Jsonified String representing the Restaurant.
	@apiError {String} - Error No Restaurant found for 'mealType' and 'location'.
'''


THE RESTAURANTS/:ID {GET} ENDPOINT WAS CREATED TO RETRIEVE INFORMATION ON A SPECIFIC RESTAURANTS FOR DISPLAY TO THE USER
THE RESTAURANTS/:ID {PUT} ENDPOINT WAS CREATED TO ALLOW A USER TO UPDATE INFORMATION ON A SPECIFIC RESTAURANTS
THE RESTAURANTS/:ID {DELETE} ENDPOINT WAS CREATED TO ALLOW A USER TO DELETE A SPECIFIC RESTAURANTS MATCHING THE ID
'''
	@api {get} /restaurants/:id 
	@apiName single_restaurant_handler()
	@apiDescription -   Retrieves Information on a Specific Restaurant 
	@apiSuccessExample  Success-Response:
	      HTTP/1.1 200 OK
	     {
	       "id" : "Id of Restaurant",
	       "address": "Address of Restaurant returned from Public API",
	       "image": "Pic of Restaurant returned from Public API",
	       "name" : "Name of Restaurant"
	     }

	@api {put} /restaurants/:id
	@apiName single_restaurant_handler()
	@apiDescription - Updates the Restaurant that matches a specific ID
	@apiGroup User

	@api {delete} /restaurants/:id
	@apiName single_request_handler()
	@apiDescription - Deletes the Restaurant that matches a specific ID
	@apiGroup User
'''   


THE USERLIST {GET} ENDPOINT WAS CREATED TO RETRIEVE ALL USERS IN THE DATABASE AND DISPLAY TO THE USER
THE USERLIST {POST} ENDPOINT WAS CREATED TO RETRIEVE ALL DETAILS FOR A NEW USER FROM THE FORM
AND COMMIT THE DETAILS TO THE USER TABLE IN THE DATABASE
'''
	@api {get} /userlist 
	@apiName all_users_handler()
	@apiDescription - Retrieves all Users from the DB to display in the Template

	@api {post} /userlist 
	@apiName all_users_handler()
	@apiDescription - Retrieves New User details from the form and persists to the Restaurant table in the DB
	@apiGroup User

	@apiParam {String} [alias]      Alias for the new user
	@apiParam {String} [password]   Password for the new user which will be hashed and stored in the DB
	@apiParam {String} [email]      Email for the new user 

	@apiSuccess {String} Jsonified String representing the new User.
'''

THE USERLIST/:ID {GET} ENDPOINT WAS CREATED TO RETRIEVE INFORMATION ON A SPECIFIC USER FOR DISPLAY TO THE USER
THE USERLIST/:ID {PUT} ENDPOINT WAS CREATED TO ALLOW A USER TO UPDATE INFORMATION ON A SPECIFIC USER
'''
	@api {get} /userlist/:id 
	@apiName single_user_handler()
	@apiDescription -   Retrieves Information on a Specific User 
	@apiSuccessExample  Success-Response:
	      HTTP/1.1 200 OK
	     {
	       "id" : "Id of User",
	       "alias": "User Alias",
	       "password": "User Hashed Password",
	       "email" : "Email of User"
	     }

	@api {put} /userlist/:id
	@apiName single_restaurant_handler()
	@apiDescription - Updates the User that matches a specific ID
	@apiGroup User

	@api {delete} /userlist/:id
	@apiName single_request_handler()
	@apiDescription - Deletes the User that matches a specific ID
	@apiGroup User
''' 

