import pandas as pd
d= pd.read_csv('nato_phonetic_alphabet.csv')
df = pd.DataFrame(d)
dict = {row['letter']:row['code'] for _,row in df.iterrows()}
def NATO():
    word = input('Enter a word: ')
    try:
        word1 = word.upper()
        phonetic_words = [dict[i] for i in word1]
    except :
        print('Please enter alphabets only')
        NATO()
    else:
        print(phonetic_words)

NATO()

