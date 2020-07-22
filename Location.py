'''
Create a script called location that return the location parameters of any location you
want.
'''
from opencage.geocoder import OpenCageGeocode
def location():
    key = 'b109193b45cf4444b0115e2f16e911f1'
    geocoder = OpenCageGeocode(key)
    query = input("Enter location(ex:-delhi,punjab,hyd):")
    results = geocoder.geocode(query)
    return results
results=location()
print(f"Latitude : {results[0]['geometry']['lat']}")
print(f"Longitude : {results[0]['geometry']['lng']}")
print(f"Country Code:{results[0]['components']['country_code']}")
print(f"Time zone Name: {results[0]['annotations']['timezone']['name']}")
