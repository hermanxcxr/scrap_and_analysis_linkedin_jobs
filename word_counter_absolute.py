from validator import Validate
from abs_plot_values import values_dict

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
    for key_2,value_2 in distribution_dict.items():
      pattern = re.compile(value_1)
      result = re.search(pattern,key_2)
      if result is not None:
        #print("Palabra clave: {}, coincidencia: {}, cantidad: {}".format(key_1,key_2,value_2))
        key_dist_dict[key_2] = (key_1,key_2,value_2,1)
  return key_dist_dict

def word_frequency_distribution(texto):
  
  #detecta el lenguaje del texto
  language = detect(texto)
  
  if language == 'en':
      language = "english"
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
  
  '''
  
  with open("inputs\description_regex_tokens.json","r") as file:
    key_regexs = json.load(file)
  file.close()

  df["frequency_dist"] = df["description"].apply(lambda x: word_frequency_distribution(x))
  df["freq_dist_key"] = df["frequency_dist"].apply(lambda x: keyword_frequency_distribution(x,key_regexs))  
  df = df.reset_index()
  df = df.drop(columns=['index'])
  return df

def one(language,file_root):
  '''
  Convierte un archivo de excel creado con caller.py en otro, que contiene la
  frecuencia de las palabras clave especificadas en "description_regex_tokens"
  en cada vacante, luego grafica con que frecuencia cada habilidad es requerida 
  en la totalidad de los vacantes
  DF + Lang  => MCSN ^ Regexs => DF_rel a Regex y  SUMA(lista de palabras)
  '''

  df = pd.read_excel(file_root, index_col='index')
  df["language"] = df["description"].apply(lambda x: detect(x))
  total_rows = df.shape[0]
  if language == 'es' or language == "en":
    df = df[df["language"] == language]
    df = df.reset_index()
  
  df = most_common_suma_name(df)
  
  filtered_rows = df.shape[0]  
  jobs_percentage = round(filtered_rows / total_rows * 100,2)
  print('{} de {} vacantes en {},equivalente al {}%'.format(filtered_rows,total_rows,language,jobs_percentage))

  file_name_a = re.search(re.compile('[\w\d]{10,}.xlsx'),file_root)

  df.to_excel('outputs/{}_AWC.xlsx'.format(file_name_a[0]),index_label="index")
  values_dict(df,file_name_a[0])

if __name__ == "__main__":
    
  file_root = tkinter.filedialog.askopenfilename()

  language_flag = False
  while language_flag == False:
      language = input("Contar por idioma?, ingrese es/en/none: ")
      lang_validator = Validate(language,language_flag)
      language, language_flag = lang_validator.lang_validation()
  
  one(language,file_root)