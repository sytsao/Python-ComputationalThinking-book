#e8-4-1 利用Google map API查詢
from googleplaces import GooglePlaces, types, lang
YOUR_API_KEY = '從8.4.1獲得的API_Key'
google_places = GooglePlaces(YOUR_API_KEY)
query_result = google_places.nearby_search(location='Tokyo, Japan', keyword='Fish', radius=400, types=[types.TYPE_FOOD])
for place in query_result.places:
    print(place.name)
    print(place.geo_location)
    place.get_details()
    print(place.local_phone_number)
    print(place.website)
    print('------------------------------------------')
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(pagetoken=query_result.next_page_token)
