from enum import unique
import pandas as pd

data = pd.read_csv('data.tsv', sep='\t')
data_to_models = pd.read_csv('data_to_model.csv', sep='\t')

print(set(data.source_title.unique()) - set(data_to_models.source_title.unique()))