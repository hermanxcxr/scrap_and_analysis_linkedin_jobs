from job_info import each_job
from validator import Validate
from file_maker import FileMaker

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import TimeoutException

import time
import json
             
def on_going(jobs_list,last_value,xpath,driver,delay):
    
    if last_value == 1:        
        each_job(jobs_list,driver,delay) #programa que descarga la información jobs
        print('identificador: {1},i: {1}')
    elif last_value > 1: 
        botones = []
        i= 2
        three_points = "…"
        while i <= 20 and i <= last_value+1: #MAX 20 páginas 
            
            each_job(jobs_list,driver,delay) #programa que descarga la información
            
            paginas = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpath)))
            botones = paginas.find_elements_by_xpath('.//li')
            for boton in botones:
                try:
                    identificador = boton.find_element_by_xpath('./button/span').text
                    if identificador == three_points and i < 10:
                        boton.click()
                    elif int(identificador) == i:
                        boton.click()
                except:
                    pass
            print('identificador: {},i: {}'.format(identificador,i))
            i += 1
    return jobs_list

def dos(job="python",location="colombia",remote=False,last_week=True):

    with open('personal_info.json','r',encoding='utf-8') as f:
        p_info = json.load(f)

    with open('xpaths.json','r',encoding='utf-8') as f:
        xpaths = json.load(f)

    '''
    #Ejecución en primer plano
    options = webdriver.ChromeOptions() #Instanciar driver
    driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=options)
    '''
    #Ejecución en segundo plano
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=chrome_options)
    
    
    #INTERACTIVIDAD
    delay = 10
    #INGRESO A LINKEDIN, quitar datos personales para subir a GITHUB
    driver.maximize_window() #Ejecución en primer plano
    driver.get('https://www.linkedin.com/login/')
    time.sleep(0.01)
    username_box = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["username_box"])))
    username_box.send_keys(p_info["name"])
    time.sleep(0.01)
    passw_box = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["passw_box"])))
    passw_box.send_keys(p_info["password"])
    start_button_0 = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["start_button_0"])))
    start_button_0.click()
    #INGRESO A LINKEDIN/JOBS
    driver.get('https://www.linkedin.com/jobs/')
    job_box=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["job_box"])))
    job_box.send_keys(job)
    location_box=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["location_box"])))
    location_box.send_keys(location)
    location_box.send_keys(Keys.ENTER)
        
    #CONFIGURACIÓN PARA SCRAPEAR LOS TRABAJOS
    #remotamente, REMOTAMENTE.CLICK, CHECK_REMOTAMENTE.CLICK, MOSTRAR
    if remote:
        time.sleep(0.5)
        remote_button=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["remote_button"])))
        remote_button.click()
        remote_check=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["remote_check"])))
        remote_check.click()
        remote_rbutton=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["remote_rbutton"])))
        remote_rbutton.click()
    #semana pasada
    if last_week:
        time.sleep(0.5)
        pub_time_button=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["pub_time_button"])))
        pub_time_button.click()
        pub_time_check=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["pub_time_check"])))
        pub_time_check.click()
        pub_time_rbutton=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["pub_time_button"])))
        pub_time_rbutton.click()                       
    
    #deteccion de la cantidad de paginas
    try:
        time.sleep(1)
        paginas = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["paginas"])))
        cant = paginas.find_elements_by_xpath('.//li')
        value = len(cant)-1
        last_value = int(cant[value].find_element_by_xpath('./button/span').text) #Cant. páginas
        print("cant. págs: {}".format(last_value))
    #si sólo hay una página
    except:
        last_value = 1
        print("No hay trabajos relacionados o sólo hay una página")

    #avanzar a lo largo de las páginas
    jobs_list = []
    on_going(jobs_list,last_value,xpaths["paginas"],driver,delay)
    #print(jobs_list)
    excel_file = FileMaker(jobs_list,job,location,remote,last_week)
    excel_file.df_2_file()

if __name__ == "__main__":
    job = input("Trabajo: ")
    location = input("Ubicación: ")
    if len(job) == 0:
        job = "python"
    if len(location) == 0:
        location = "colombia"
    remote_flag = False
    while remote_flag == False:
        remote = input("Remoto, presione Y/N: ")
        remote_val = Validate(remote,remote_flag)
        remote, remote_flag = remote_val.validation()

    last_week_flag = False
    while last_week_flag == False:
        last_week = input("Última semana, presione Y/N: ")
        last_week_val = Validate(last_week,last_week_flag)
        last_week, last_week_flag = last_week_val.validation()
    
    dos(job,location,remote,last_week)