import pandas as pd
d= pd.read_csv('nato_phonetic_alphabet.csv')
df = pd.DataFrame(d)
dict = {row['letter']:row['code'] for _,row in df.iterrows()}
word = input('Enter a word: ')
word1 = word.upper()
phonetic_words = [dict[i] for i in word1]
print(phonetic_words)

