import pyphen
from random import randint
import markovify
import pronouncing
import sys
import json


with open("newPoetry.txt") as f:
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

    if number == "4":
        return json.dumps([first_sentence, second_sentence,  third_sentence,  fourth_sentence])

    elif number == "8":
        return json.dumps([first_sentence, second_sentence,  third_sentence, fourth_sentence, fifth_sentence,  sixth_sentence,  seventh_sentence,  eight_sentence])

    else:
        return json.dumps([first_sentence,  second_sentence,  third_sentence,  fourth_sentence,  fifth_sentence,  sixth_sentence, seventh_sentence,  eight_sentence, ninth_sentence,  tenth_sentence, eleventh_sentence,  twelth_sentence,  thirtheenth_sentence, fourteenth_sentence])
