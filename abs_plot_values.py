from abs_plotter import AbsPlotter

from collections import Counter

def values_dict(df,title):

  counter_dict = {}
  
  if df.loc[0,"freq_dist_key"] != '{}':
    dict_total_0 = df.loc[0,"freq_dist_key"]
    #print(dict_total_0)
    for key_1,value_1 in dict_total_0.items():
      counter_dict[[key_1][0]] = dict_total_0[key_1][3]

  for i in range(1,df.shape[0]):
    if df.loc[i,"freq_dist_key"] != '{}':
      main_dict = df.loc[i,"freq_dist_key"]
      #print(main_dict)
      temp_dict = {}
      for key_1,value_1 in main_dict.items():
        temp_dict[[key_1][0]] = main_dict[key_1][3]
      #print(temp_dict)
      counter_dict = dict(Counter(temp_dict)+Counter(counter_dict)) 
      #print(counter_dict)
      #print('*********')

  plotter_0 = AbsPlotter(counter_dict.keys(),counter_dict.values(),title,df.shape[0])
  plotter_0.plotting()