#import requests

#query = 'https://jsonplaceholder.typicode.com/todos/1'

#response = requests.get(query)

#print(response)
#print(response.json()


#import requests

#url = 'https://bored-api.appbrewery.com/random/1'

#response = requests.get(url)

#print(response)
#print(response)


def pokedex():
    search = input("would you like to search pokemon")
    while search =='Y':
        pokename = input("please enter a pokemon name: ")
        query = V