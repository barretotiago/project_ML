from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with a acc
def test_get_inference_acc():

    person = {   
        "buying": 'vhigh',
        "maint": 'med',
        "doors": '3',
        "persons": 'more',
        "lug_boot": 'big',
        "safety": 'med',
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "acc"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_unacc():

    person = {
        "buying": 'vhigh',
        "maint": 'med',
        "doors": '4',
        "persons": '2',
        "lug_boot": 'small',
        "safety": 'low',
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "unacc"
    

def test_get_inference_good():

    person = {
        "buying": 'med',
        "maint": 'low',
        "doors": '2',
        "persons": '4',
        "lug_boot": 'med',
        "safety": 'high',
    } 

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "good"
    
    
def test_get_inference_vgood():

    person = {
        "buying": 'med',
        "maint": 'med',
        "doors": '5more',
        "persons": 'more',
        "lug_boot": 'big',
        "safety": 'high',
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "vgood"