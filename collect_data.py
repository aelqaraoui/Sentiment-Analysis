import requests
import json

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

headers = {'Authorization':'Bearer FHKjNSKNxiHSjk7Ov94lD2FQ9Vv-zp9rM0eXQgKWCDi0qwHr2GPGaqNYY3xGkj52PMtuU4rYWyhLZgjYrNM725w1E79pasAlKBO4AszgGeXpqA2i1WjS6FHRRWwAYHYx'}

reviews = []

for state in states:
    try:
        x = requests.get('https://api.yelp.com/v3/businesses/search?location=' + state, headers=headers)
        data = x.json()
        for i in range(int(data['total']/50)):
            x = requests.get('https://api.yelp.com/v3/businesses/search?location=' + state + '&limit=50&offset=' + str(i*50), headers=headers)
            data = x.json()
            try:
                for business in data['businesses']:
                    print(business['id'])
                    x = requests.get('https://api.yelp.com/v3/businesses/' + business['id'] + '/reviews', headers=headers)
                    for review in x.json()['reviews']:
                        reviews.append({'text':review['text'], 'rating':review['rating']})
            except:
                break
    except:
        continue

print(len(reviews))

with open('reviews.json', 'w') as fout:
    json.dump(reviews, fout)
