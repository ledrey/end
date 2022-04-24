import pandas as pd

data = pd.read_csv('data.tsv', sep = '\t', keep_default_na = False)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

wordsToDel = stopwords.words('english')
wordsToDel.extend(['.',',',':',';'])
wordsToDel

data['tokenized'] = data['Abstract'].apply(word_tokenize)
data['tokenized'] = [word for word in data['tokenized'] if not word in wordsToDel]

data.head(5)