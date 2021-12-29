import requests
# import json
import pickle

data=requests.get('https://www.loremipzum.com/en/text-generator').text
list=data.split('\n')

# pickling
with open("Exerc10.pkl",'wb') as f:
    pickle.dump(list,f)
    f.close()

# open the pickle file
with open("Exerc10.pkl",'rb') as f:
    print(pickle.load(f))

ki