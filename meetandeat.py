# -*- coding: utf-8 -*-
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

#foursquare_client_id = "P0ZAGLGKKXLD50RFY4AKJHWPPIL5NJWNVE1UHOJCGKZHLFUB"
#foursquare_client_secret = "FLLJ2TP3SKNSJQYGBSVURTTXCXJQCLVBGH3NUOMRY20ZXBIE"
#google_api_key = "AIzaSyAt-lQkLsGUVO1BnRQW03N-pgNJGne63Sk"

foursquare_client_id = "HDKI342V4TLFSDNYBD4FYTF2XL4CFS5SJDEEHJSX5F3L3V05"
foursquare_client_secret = "AN24WVRKBEFLF4QSLOOWK0G0BHAX2KFIUGLLEPBYNZOJVYPY"
google_api_key = "AIzaSyAyg4niY36q9ZH1tj_O9DLE87euCipEHEo"

def getGeocodeLocation(inputString):
    #Replace Spaces with '+' in URL
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    #print response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

#This function takes in a string representation of a location and cuisine type, geocodes the location, and then pass in the latitude and longitude coordinates to the Foursquare API
def findARestaurant(mealType, location):
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    if result['response']['venues']:
        #Grab the first restaurant
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id'] 
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        #Format the Restaurant Address into one string
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address
        
        #Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
        result = json.loads(h.request(url,'GET')[1])
        #Grab the first image
        #if no image available, insert default image url
        if result['response']['photos']['items']:
            firstpic = result['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + "300x300" + suffix
        else:
            imageURL = "http://runawayapricot.com/wp-content/uploads/2014/09/placeholder.jpg"

        restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
        #print "Restaurant Name: %s " % restaurantInfo['name']
        #print "Restaurant Address: %s " % restaurantInfo['address']
        #print "Image: %s \n " % restaurantInfo['image']
        return restaurantInfo
    else:
        #print "No Restaurants Found for %s" % location
        return "No Restaurants Found"


def getRestaurantInfo(mealType, location):
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    if result['response']['venues']:
        #Grab the first restaurant
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id'] 
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        #Format the Restaurant Address into one string
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address
        
        restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'lat':latitude, 'lon':longitude}
        #print "Restaurant Name: %s " % restaurantInfo['name']
        #print "Restaurant Address: %s " % restaurantInfo['address']
        #print "Image: %s \n " % restaurantInfo['image']
        return restaurantInfo
    else:
        #print "No Restaurants Found for %s" % location
        return "No Restaurants Found"


if __name__ == '__main__':
    print findARestaurant("sushi", "chaguanas")
    # findARestaurant("Tacos", "Jakarta, Indonesia")
    # findARestaurant("Tapas", "Maputo, Mozambique")
    # findARestaurant("Falafel", "Cairo, Egypt")
    # findARestaurant("Spaghetti", "New Delhi, India")
    # findARestaurant("Cappuccino", "Geneva, Switzerland") 
    # findARestaurant("Sushi", "Los Angeles, California")
    # findARestaurant("Steak", "La Paz, Bolivia")
    # findARestaurant("Gyros", "Sydney Austrailia")        