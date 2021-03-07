class Validate:
    
    def __init__(self,feature,flag):
        self.x = feature
        self.flag = flag
    
    def validation(self):
        if self.x == "Y" or self.x == "y":
            self.flag = True
            self.value = True
            return self.value, self.flag
        elif self.x == "N" or self.x == "n":
            self.flag = True
            self.value = False
            return self.value, self.flag
        else:
            self.flag = False
            self.value = 0
            return self.value, self.flag
