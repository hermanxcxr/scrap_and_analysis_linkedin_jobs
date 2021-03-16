import pandas as pd

class FileMaker:

    def __init__(self,jobs_list,job,location,remote,last_week):
        self.jobs_list = jobs_list
        self.job = job
        self.location = location
        self.remote = str(remote)
        self.last_week = str(last_week)

    def df_2_file(self):
        df = pd.DataFrame()
        for i in range(len(self.jobs_list)):
            try:
                df.loc[i,"name"] = self.jobs_list[i]["name"]
            except:
                pass
            try:
                df.loc[i,'company'] = self.jobs_list[i]["company"]
            except:
                pass
            try:
                df.loc[i,'location'] = self.jobs_list[i]["location"]
            except:
                pass
            try:    
                df.loc[i,'distance_type'] = self.jobs_list[i]["type_0"]
            except:
                pass
            try:    
                df.loc[i,'functions'] = self.jobs_list[i]["Funciones laborales"]
            except:
                pass
            try:    
                df.loc[i,'job_type'] = self.jobs_list[i]["Tipo de empleo"]
            except:
                pass
            try:    
                df.loc[i,'sector'] = self.jobs_list[i]["Sector"]
            except:
                pass
            try:    
                df.loc[i,'experience_level'] = self.jobs_list[i]["Nivel de experiencia"]
            except:
                pass
            try:    
                df.loc[i,'wage'] = self.jobs_list[i]["wage"]
            except:
                pass
            try:    
                df.loc[i,'url'] = self.jobs_list[i]["url"]
            except:
                pass
            try:    
                df.loc[i,'description'] = self.jobs_list[i]["description"]
            except:
                pass
        df.to_excel('outputs/{}_{}_rmt_{}_lw_{}.xlsx'.format(self.job,self.location,self.remote,self.last_week),index_label="index")