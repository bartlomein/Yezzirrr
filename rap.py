import pyphen
from random import randint
import markovify
import pronouncing
import sys
import json


with open("rap.txt") as f:
    text = f.read()
dic = pyphen.Pyphen(lang='en')

text_model = markovify.Text(text)


# generate markov chain model
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()


def mainFunction(inputSentence):
    # check for space in inputs

    inputSentence = inputSentence.strip("'")

    if inputSentence == None:
        return "Empty string, try again homie"
    elif inputSentence.isspace():
        return "Empty string, try again homie"
    elif inputSentence == False:
        return "Empty string, try again homie"
    # passes input checks

    # check for rhymes with last word in the input sentence
    with_periods = inputSentence.strip('.')
    split_sentence = with_periods.split()
    try:
        last_word1 = split_sentence[-1]
    except IndexError:
        return "Can't pass me an weird string dog"
    word_that_rhyme = pronouncing.rhymes(last_word1)
    wordlist = list(word_that_rhyme)
    if len(wordlist) == 0:
        return "No Rhymes with this word in my library, try again homie"

    second_generate_no_rhyme = text_model.make_short_sentence(70)

    rhyme_word_of_first_sentence = wordlist[randint(0, len(wordlist) - 1)]
    old = second_generate_no_rhyme.rsplit(' ', 1)[0]

    # NEW SECOND SENTENCE
    new_second = old + " " + rhyme_word_of_first_sentence

    # THIRD SENTENCE
    third_sentence = text_model.make_short_sentence(70)

    # FOURTH SENTENCE
    fourth_sentence_no_rhyme = text_model.make_short_sentence(70)

    with_periods2 = third_sentence.strip('.')
    split_sentence2 = with_periods2.split()

    last_word2 = split_sentence2[-1].strip('.')
    word_that_rhyme2 = pronouncing.rhymes(last_word2)
    wordlist2 = list(word_that_rhyme2)
    if len(wordlist2) == 0:
        third_sentence = text_model.make_short_sentence(70)
        with_periods2 = third_sentence.strip('.')
        split_sentence2 = with_periods2.split()
        last_word2 = split_sentence2[-1].strip('.')
        word_that_rhyme2 = pronouncing.rhymes(last_word2)
        wordlist2 = list(word_that_rhyme2)

    random_word2 = wordlist2[randint(0, len(wordlist2) - 1)]

    old = fourth_sentence_no_rhyme.rsplit(' ', 1)[0]
    new = old + " " + random_word2

    return json.dumps({"1": inputSentence.strip('.'), "2": new_second.strip('.'), "3": third_sentence.strip('.'), "4": new.strip('.')})
