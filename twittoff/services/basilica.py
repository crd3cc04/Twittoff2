#twittoff/services/basilica.py

import basilica

import os

from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection)) 

breakpoint()
embedding = connection.embed_sentence("Hey this is a cool tweet", model='twitter')

#if __name__ == "__main__":

#    print(type(connection))
#    sentences = ("Hey this is a cool tweet!")
#    embeddings = connection.embed_sentences(sentences)
    
#    print(list(embeddings)) # [[0.8556405305862427, ...], ...]