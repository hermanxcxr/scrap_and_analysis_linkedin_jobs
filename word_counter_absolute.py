from validator import Validate

from langdetect import detect
import pandas as pd 
import numpy as np
import json
import re

import tkinter.filedialog

import nltk

from nltk import FreqDist
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def keyword_frequency_distribution(distribution_list,regexs_dictionary):
  distribution_dict = dict(distribution_list)
  key_dist_dict = {}
  for key_1, value_1 in regexs_dictionary.items():
  #for word in i:
    for key_2,value_2 in distribution_dict.items():
      pattern = re.compile(value_1)
      result = re.search(pattern,key_2)
      if result is not None:
        #print("Palabra clave: {}, coincidencia: {}, cantidad: {}".format(key_1,key_2,value_2))
        key_dist_dict[key_2] = (key_1,key_2,value_2,1)
  return key_dist_dict

def word_frequency_distribution(texto):
  
  #detecta el lenguaje del texto
  #if language == "none":
  language = detect(texto)
  
  if language == 'en':
      language = "english"
  #if language == 'es':
  else:
      language = "spanish"
  #print(language)

  #elimina signos de puntuación y TOKENIZA
  tokenizer = RegexpTokenizer(r'\w+')
  texto = tokenizer.tokenize(texto) 
  
  #elimina stopwords
  content = []
  stopwd = stopwords.words(language)
  for word in texto:
      if word.lower() not in stopwd: 
          content.append(word.lower()) 
  distribucion = FreqDist(content)
  return distribucion

def most_common_suma_name(df): 
  '''
  column_flag = False
  while column_flag == False:
    column = input("Filtrar por nombre(N) o descripción(D): ")
    column_validator = Validate(column,column_flag)
    column, column_flag = column_validator.column_validation()
  if column == "description":
    df = df.loc[df.description.str.contains(word),:] #contains,startswith #Test if pattern or regex is contained
  else:
    df = df.loc[df.name.str.contains(word),:]
  '''
  with open("inputs\description_regex_tokens.json","r") as file:
    key_regexs = json.load(file)
  file.close()

  df["frequency_dist"] = df["description"].apply(lambda x: word_frequency_distribution(x))
  df["freq_dist_key"] = df["frequency_dist"].apply(lambda x: keyword_frequency_distribution(x,key_regexs))
  
  df = df.reset_index()

  '''
  try:
    #print(df.shape)
    #df.shape
    suma = df.loc[0,"frequency_dist"]
    #df.head()
    for i in range(1,df.shape[0]):
        suma = suma + df.loc[i,"frequency_dist"]
  except  UnboundLocalError as e:
    print(e)
    print("no hay coincidencias con el filtro, {}".format(e))
  except KeyError as e:
    print("no hay coincidencias con el filtro, {}".format(e))
  '''
  return df

def one(language,file_root):
  '''
  DF + Lang  => MCSN ^ Regexs => DF_rel a Regex y  SUMA(lista de palabras)
  '''
  #print(language)
  #se debe poder escoger el archivo a evaluar y df
  #print(file_root)
  #print(type(file_root))
  df = pd.read_excel(file_root, index_col='index')
  '''
  python_colombia_rmt_False_lw_False.xlsx
  odontologo_colombia_rmt_False_lw_True.xlsx
  '''
  #df = pd.read_excel("outputs/python_colombia_rmt_False_lw_False.xlsx", index_col='index')
  df["language"] = df["description"].apply(lambda x: detect(x))
  if language == 'es' or language == "en":
    df = df[df["language"] == language]
    df = df.reset_index()
  
  total_rows = df.shape[0]
  #se debe poder escoger la regex de filtrado
  #word = input("RegEx para filtrar (entre corchetes): ")
  #suma, df = most_common_suma_name(df,word,language)
  df = most_common_suma_name(df)

  filtered_rows = df.shape[0]
  jobs_percentage = round(filtered_rows / total_rows * 100,2)

  file_name_a = re.search(re.compile('[\w\d]{10,}.xlsx'),file_root)

  df.to_excel('outputs/{}_FD.xlsx'.format(file_name_a[0],index_label="index"))
  
 
  #print("Cantidad de palabras detectadas: {}".format(len(suma)))
  #twenty_percent = round(0.2 * len(suma))
  #print('{} empleos de {} vacantes,equivalente al {}%'.format(filtered_rows,total_rows,jobs_percentage))
  #print(suma.most_common(twenty_percent))
  #file_name_b = re.sub("[^\w]","",word)
  #file_name = file_name_a[0] + file_name_b
  #print(file_name)
  #with open('outputs/{}.json'.format(file_name_a),'w') as outfile:
    #value = dict(suma)
  #  value = dict(suma.most_common(twenty_percent))
  #  json.dump(value,outfile)
  
  #suma_most_common_words_plotter(suma,twenty_percent)

if __name__ == "__main__":
    
  file_root = tkinter.filedialog.askopenfilename()

  language_flag = False
  while language_flag == False:
      language = input("Contar por idioma?, ingrese es/en/none: ")
      lang_validator = Validate(language,language_flag)
      language, language_flag = lang_validator.lang_validation()
  
  one(language,file_root)