import requests
import pytest

host = 'https://pokemonbattle.me:9104' 
token = 'a226d220394e379c87b65548045bd665'

def test_status_code():
    answer= requests.get(f'{host}/trainers', params= {'trainer_id' : 4615} )
    assert answer.status_code == 200

def test_name():
    test_name= requests.get(f'{host}/trainers', params= {'trainer_id' : 4615}) 
    assert test_name.json()['trainer_name']== 'stas'