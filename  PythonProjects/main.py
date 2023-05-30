import requests
host = 'https://pokemonbattle.me:9104' 
token = 'a226d220394e379c87b65548045bd665'

answer = requests.post(f'{host}/trainers/confirm_email', json= 
{
    "trainer_token": token
}, headers= {"Content-Type" : "application/json"}) 

print(answer.text)

pokemons= requests.post(f'{host}/pokemons' , json= 
{
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers= {"Content-Type" : "application/json", "trainer_token" : token} ) 

print(pokemons.text)

pokemon_name= requests.put(f'{host}/pokemons', json= 
{
    "pokemon_id" : "12538",
    "name": "Карамба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers= {"Content-Type" : "application/json", "trainer_token" : token} )

print(pokemon_name.text)

add_pokebol= requests.post(f'{host}/trainers/add_pokeball', json=
{
    "pokemon_id": "12538"
}, headers= {"Content-Type" : "application/json", "trainer_token" : token} )
print(add_pokebol.text)