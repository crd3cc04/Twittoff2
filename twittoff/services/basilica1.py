#twittoff/services/basilica.py

import basilica 
#import os
from decouple import config
from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables

BASILICA = basilica.Connection(config('BASILICA_API_KEY'))

#connection = basilica.config(BASILICA_API_KEY)
#print(type(connection)) 

#breakpoint()
embedding = BASILICA.embed_sentence("Hey this is a cool tweet", model='twitter')
print(embedding)
# > a list of 768 numbers

#breakpoint()
# Also helpful when having mulitple sentences or tweets to create a for loop....
tweets = ["Samuari slice that like button", "artificial intelligence", "Makeup is life"]
embeddings = BASILICA.embed_sentences(tweets, model="twitter")
for embed in embeddings:
    print("-----")
    print(len(embed))




#if __name__ == "__main__":

#    print(type(connection))
#    sentences = ("Hey this is a cool tweet!")
#    embeddings = connection.embed_sentences(sentences)
    
#    print(list(embeddings)) # [[0.8556405305862427, ...], ...]