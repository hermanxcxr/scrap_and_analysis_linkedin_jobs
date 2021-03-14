from validator import Validate
from word_freq_dist import word_frequency_distribution

from langdetect import detect
import pandas as pd 
import numpy as np

def most_common_suma_name(df,word,language):
  df = df.loc[df.name.str.contains(word),:] #contains,startswith
  df["frequency_dist"] = df["name"].apply(lambda x: word_frequency_distribution(x,language))
  df = df.reset_index()
  suma = df.loc[0,"frequency_dist"]
  for i in range(1,df.shape[0]):
      suma = suma + df.loc[i,"frequency_dist"]
  return suma, df

def one(language):
    
    #se debe poder escoger el archivo a evaluar y df
    df = pd.read_excel('outputs/python_colombia_rmt_False_lw_False.xlsx', index_col='index')
    df["language"] = df["description"].apply(lambda x: detect(x))
    df = df[df["language"] == language]
    df = df.reset_index()
    total_rows = df.shape[0]
    #se debe poder escoger la regex de filtrado
    word = r'[ana|ANA|dat|DAT]{3}'
    suma, df = most_common_suma_name(df,word,language)
    filtered_rows = df.shape[0]

    print('{}/{}'.format(filtered_rows,total_rows))
    print(suma.most_common(50))

if __name__ == "__main__":
    
    language_flag = False
    while language_flag == False:
        language = input("Idioma, ingrese es/en: ")
        lang_validator = Validate(language,language_flag)
        language, language_flag = lang_validator.lang_validation()
    
    one(language)