import matplotlib.pyplot as plt
import numpy as np

def suma_most_common_words_plotter(todos,maximo):
  most_common_group = todos.most_common(maximo)
  x_val = [x[0] for x in most_common_group]
  #y_val = [x[1] for x in most_common_group]
  y_val = []
  for x in most_common_group:
      y_val.append(x[1])
  plt.figure(figsize=(80,80))
  plt.xticks(rotation = 90, fontsize=32)
  plt.yticks(fontsize=32)
  #plt.xlabel(fontsize=24)
  plt.bar(x_val,y_val)
  plt.show()
  #return most_common_group
  return