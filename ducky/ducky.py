#! /usr/bin/python

import warnings
import wikipedia
import datetime
from translate import Translator

LEADING_MESSAGE = "ducky: "

def wikipedia_ref(phrase):
     return wikipedia.summary(phrase)

while True:
    user_input = input("ducky>>>").strip()
    if user_input == "date":
        print("{} Da date is: {}".format(LEADING_MESSAGE, datetime.date.today()))
    
    elif "wiki" in user_input:
        try:
            replaced_user_input = user_input.replace("wiki", "")
            print("{} Here is your article: {}".format(LEADING_MESSAGE, wikipedia_ref(replaced_user_input)))        
        
        except wikipedia.exceptions.DisambiguationError:
            print("{} That is not a wikipedia page, here are some suggestions: {}".format(LEADING_MESSAGE, wikipedia.search(replaced_user_input, suggestion=True)))            
   
    elif "tra" in user_input:
        replaced_user_input = user_input.replace("tra", "")
        list_of_args = replaced_user_input.split()
        arg_1 = list_of_args[0]
        arg_2 = list_of_args[1]
        translator = Translator(to_lang=arg_2)
        translation = translator.translate(arg_1)
        print("{} Translation: {} to {}".format(LEADING_MESSAGE, arg_1, translation))
         
    elif "bye" in user_input:
       break 
