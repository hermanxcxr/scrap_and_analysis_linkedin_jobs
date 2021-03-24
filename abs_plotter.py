import matplotlib.pyplot as plt

class AbsPlotter:

    def __init__(self,x,y,DF_name,df_shape_0):
        self.x = x
        self.y = y
        self.DF_name = DF_name
        self.df_shape_0 = df_shape_0

    def plotting(self):
  
        plt.figure(figsize=[40,10])
        plt.title("Habs. requeridas: {}".format(self.DF_name), fontsize=24)
        bars = plt.bar(list(self.x),height = list(self.y))
        plt.xticks(rotation = 85, fontsize=18)
        plt.yticks(rotation = 85, fontsize=18)
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x(),
                    yval+.05,
                    "{}/{}\n{}%".format(yval,self.df_shape_0,round(yval*100/self.df_shape_0,1)),
                    rotation=45,
                    fontsize=10
                    )
        plt.show()