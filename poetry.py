import pyphen
from random import randint
import markovify
import pronouncing
import sys
import json


with open("poetry.txt") as f:
    text = f.read()
dic = pyphen.Pyphen(lang='en')

text_model = markovify.Text(text)


# generate markov chain model
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()


def poetryFunction(number):

    first_sentence = text_model.make_short_sentence(90)
    second_sentence = text_model.make_short_sentence(90)
    third_sentence = text_model.make_short_sentence(90)
    fourth_sentence = text_model.make_short_sentence(90)
    fifth_sentence = text_model.make_short_sentence(90)
    sixth_sentence = text_model.make_short_sentence(90)
    seventh_sentence = text_model.make_short_sentence(90)
    eight_sentence = text_model.make_short_sentence(90)
    ninth_sentence = text_model.make_short_sentence(90)
    tenth_sentence = text_model.make_short_sentence(90)
    eleventh_sentence = text_model.make_short_sentence(90)
    twelth_sentence = text_model.make_short_sentence(90)
    thirtheenth_sentence = text_model.make_short_sentence(90)
    fourteenth_sentence = text_model.make_short_sentence(90)

    if number == 4:
        return json.dumps({"1": first_sentence, "2": second_sentence, "3": third_sentence, "4": fourth_sentence})

    elif number == 8:
        return json.dumps({"1": first_sentence, "2": second_sentence, "3": third_sentence, "4": fourth_sentence, "5": fifth_sentence, "6": sixth_sentence, "7": seventh_sentence, "8": eight_sentence})

    else:
        return json.dumps({"1": first_sentence, "2": second_sentence, "3": third_sentence, "4": fourth_sentence, "5": fifth_sentence, "6": sixth_sentence, "7": seventh_sentence, "8": eight_sentence, "9": ninth_sentence, "10": tenth_sentence, "11": eleventh_sentence, "12": twelth_sentence, "13": thirtheenth_sentence, "14": fourteenth_sentence})
