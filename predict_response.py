#Text Data Preprocessing Lib
import nltk
# Model Load Lib
import tensorflow
from data_preprocessing import get_stem_words

import json
import pickle
import numpy as np
import random

ignore_words = ['?', '!',',','.', "'s", "'m"]

# Load model

# Load data files



def preprocess_user_input(user_input):

    input_word_token_1 = nltk.word_tokenize(user_input)
    input_word_token_2 = get_stem_words(input_word_token_1, ignore_words) 
    input_word_token_2 = sorted(list(set(input_word_token_2)))

    bag=[]
    bag_of_words = []
   
    # Input data encoding 
    

#def bot_class_prediction(user_input):

    

#def bot_response(user_input):

 