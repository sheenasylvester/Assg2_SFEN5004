from meetandeat import findARestaurant, getRestaurantInfo
from models import Base, Restaurant, User, Request, Proposal, MealDate
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)



engine = create_engine('sqlite:///meetup.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__, static_url_path = "")

@app.route('/')
def root():
  return app.send_static_file("index.html")

'''
@api {post} /login Authenticates a User, Retrieves Email and Password from the POST
@apiName login_handler
@apiGroup User

@apiParam {} id Users unique ID.

@apiSuccess {String} ID, Email, Password of the User.
@apiError {String} - Error Unable to retrieve person.
'''
@app.route('/login', methods = ['POST'])
def login_handler():
  
  # 1. RETRIEVE FORM DETAILS OF THE REQUEST
  loginEmail = request.json['email']
  loginPassword = request.json['password']
  thePerson = None
    
  # 2. CHECK IF PERSON EXISTS WITH LOGIN CREDENTIALS
  thePerson = session.query(User).filter_by(email = loginPassword, password_hash = pwd_context.encrypt(loginPassword)).one()

  # 3. CHECK IF LOGIN SUCCESSFUL
  if thePerson is not None:
    return jsonify(thePerson = thePerson.serialize)
  else:
    return jsonify({"error":"Unable to retrieve person" })
  


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
@app.route('/meetrequests', methods = ['GET', 'POST'])
def all_requests_handler():
  if request.method == 'GET':
    # RETURN ALL REQUESTS IN DATABASE
    allrequests = session.query(Request).filter_by(filled = 'Open').all()
    return jsonify(allrequests = [i.serialize for i in allrequests])

  elif request.method == 'POST':
    # MAKE A NEW REQUEST AND STORE IT IN DATABASE

    # 1. RETRIEVE FORM DETAILS OF THE REQUEST
    requestor = request.json['requestor']
    location = request.json['location']
    mealType = request.json['mealType'] 
    mealTime = request.json['mealTime']
    filled = "Open" #SET TO 'OPEN' BY DEFAULT

    
    # 2. USE PUBLIC API TO RETRIEVE GEO LOCATION AND RESTAURANT DETAILS FOR THE REQUEST
    restaurant_info = getRestaurantInfo(mealType, location)

    # 3. CHECK THE restaurant_info STRING RETURNED FROM THE meetandeat.py MODULE TO DETERMINE WHETHER TO CONTINUE PROCESSING
    if restaurant_info != "No Restaurants Found":
      
      # 4. CREATE REQUEST INSTANCE AND PERSIST TO THE request TABLE IN DB     
      theRequest = Request(mealType = unicode(mealType), 
                           mealTime = unicode(mealTime), 
                           location = unicode(location), 
                           restaurant_name = unicode(restaurant_info['name']), 
                           restaurant_address = unicode(restaurant_info['address']), 
                           latitude = unicode(restaurant_info['lat']), 
                           longitude = unicode(restaurant_info['lon']), 
                           filled = unicode(filled), 
                           user_id = unicode(requestor))

      if theRequest is not None:
        session.add(theRequest)
        session.commit() 
        return jsonify(theRequest = theRequest.serialize)
      else:
        return jsonify({"error":"Meeting Request Has Not Been Saved." })


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
@app.route('/meetrequests/<int:id>', methods = ['GET','PUT', 'DELETE'])
def single_request_handler(id):
  #RETRIEVE REQUEST MATCHING ID
  aRequest = session.query(Request).filter_by(id = id).one()

  if request.method == 'GET':
    #RETURN A SPECIFIC REQUEST
    return jsonify(aRequest = aRequest.serialize)

  elif request.method == 'DELETE':
    #DELETE A SPECFIC USER
    session.delete(aRequest)
    session.commit()
    return "Request Deleted"


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
@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
  if request.method == 'GET':
  	# RETURN ALL RESTAURANTS IN DATABASE
  	restaurants = session.query(Restaurant).all()
  	return jsonify(restaurants = [i.serialize for i in restaurants])

  elif request.method == 'POST':
  	# MAKE A NEW RESTAURANT AND STORE IT IN DATABASE

    location = request.json['location']
    mealType = request.json['mealType']    
    restaurant_info = findARestaurant(mealType, location)
    if restaurant_info != "No Restaurants Found":
      restaurant = Restaurant(restaurant_name = unicode(restaurant_info['name']), restaurant_address = unicode(restaurant_info['address']), restaurant_image = restaurant_info['image'])
      session.add(restaurant)
      session.commit() 
      return jsonify(restaurant = restaurant.serialize)
    else:
      return jsonify({"error":"No Restaurants Found for %s in %s" % (mealType, location)})


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
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def single_restaurant_handler(id):
  restaurant = session.query(Restaurant).filter_by(id = id).one()
  if request.method == 'GET':
  	#RETURN A SPECIFIC RESTAURANT
  	return jsonify(restaurant = restaurant.serialize)
  elif request.method == 'PUT':
  	#UPDATE A SPECIFIC RESTAURANT
  	address = request.args.get('address')
  	image = request.args.get('image')
  	name = request.args.get('name')
  	if address:
  		restaurant.restaurant_address = address
  	if image:
  		restaurant.restaurant_image = image
  	if name:
  		restaurant.restaurant_name = name
  	session.commit()
  	return jsonify(restaurant = restaurant.serialize)

  elif request.method == 'DELETE':
  	#DELETE A SPECFIC RESTAURANT
  	session.delete(restaurant)
  	session.commit()
  	return "Restaurant Deleted"


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
@app.route('/userlist', methods = ['GET', 'POST'])
def all_users_handler():
  if request.method == 'GET':
    # RETURN ALL USERS IN DATABASE
    users = session.query(User).all()
    return jsonify(users = [i.serialize for i in users])

  elif request.method == 'POST':
    # ADD A NEW USER AND STORE IT IN THE USER TABLE IN DATABASE

    alias = request.json['alias']
    password = request.json['password']
    email = request.json['email']    
    user = User(user_alias = unicode(alias), password_hash = unicode(password), email = unicode(email))
    user.hash_password(password)
    session.add(user)
    session.commit() 
    return jsonify(user = user.serialize)


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
@app.route('/userlist/<int:id>', methods = ['GET','PUT', 'DELETE'])
def single_user_handler(id):
  #RETRIEVE USER MATCHING ID
  aUser = session.query(User).filter_by(id = id).one()

  if request.method == 'GET':
    #RETURN A SPECIFIC USER
    return jsonify(aUser = aUser.serialize)

  elif request.method == 'PUT':
    #UPDATE A SPECIFIC USER
    alias = request.args.get('alias')
    password = request.args.get('password')
    email = request.args.get('email')
    if alias:
      aUser.user_alias = alias
    if password:
      aUser.password_hash = password
    if email:
      aUser.email = email
    session.commit()
    return jsonify(aUser = aUser.serialize)

  elif request.method == 'DELETE':
    #DELETE A SPECFIC USER
    session.delete(aUser)
    session.commit()
    return "User Deleted"

   

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)