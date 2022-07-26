
import requests
import json
# import pprint

person = {
        "buying": high,
        "workclass": 'Private',
        "fnlwgt": 364548,
        "education": 'Bachelors',
        "education_num": 13,
        "marital_status": 'Divorced',
        "occupation": 'Sales',
        "relationship": 'Not-in-family',
        "race": 'White',
        "sex": 'Male',
        "capital_gain": 8614,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": 'United-States'
    }

#url = "http://127.0.0.1:8000"
url = "https://machine-learn2-app.herokuapp.com/"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n \n"\
      f" buying: {person['buying']}\n"\
      f" maint: {person['maint']}\n"\
      f" doors: {person['doors']}\n"\
      f" persons: {person['persons']}\n"\
      f" lug_boot: {person['lug_boot']}\n"\
      f" safety: {person['safety']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")
