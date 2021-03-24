from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import TimeoutException

import json
import time

def each_job(jobs_list,driver,delay):
    '''
    1. captura la lista de trabajos en el driver y los xpaths
    2. detecta elemento por elemento en cada trabajo
    '''
    with open('xpaths.json','r',encoding='utf-8') as f:
        xpaths = json.load(f)
    
    found_jobs=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["found_jobs"])))
    jobs = found_jobs.find_elements_by_xpath('li')

    for num,job in enumerate(jobs):
        dict = {}
        
        try:
            except_delay = 30
            job_name = WebDriverWait(job,except_delay).until(EC.presence_of_element_located((By.XPATH,'.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]'))).text
        except:
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
        print(job_name)    
        
        try:
            #job_name = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]').text
            job_link = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]').get_attribute('href')
            job_obj = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')
            job_obj.click()

            description = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["description"]))).text
            subcats = driver.find_elements_by_xpath(xpaths["subcats"])            
            
            if job_name:
                dict["name"] = job_name
            else:
                dict["name"] = "null"
            #job features
            for sub_obj in subcats:
                key = sub_obj.find_element_by_xpath("./h3").text
                try:
                    value = sub_obj.find_element_by_xpath("./p").text
                except:
                    values = sub_obj.find_elements_by_xpath(".//li")
                    temp_lista = []
                    for val in values:
                        temp_lista.append(val.text)
                    value =  temp_lista
                dict["{}".format(key)] = value
                                    
        except:
            pass
        try:   
            salary = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["salary"]))).text
            if salary:
                dict["wage"] = salary
            else:
                dict["wage"] = "null"
        except:
            pass
        try:   
            #job_inc = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,''))).text
            job_inc = job.find_element_by_xpath('.//a[@class="job-card-container__link job-card-container__company-name ember-view"]').text
            if job_inc:
                dict["company"] = job_inc
            else:
                dict["company"] = "null"
        except:
            pass
        try:
            job_geo = WebDriverWait(job,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["job_geo"]))).text
            if job_geo:
                dict["location"] = job_geo
            else:
                dict["location"] = False
        except:
            pass
        try:
            job_type = WebDriverWait(job,delay).until(EC.presence_of_element_located((By.XPATH,xpaths["job_type"]))).text
            if job_type:
                dict["type_0"] = job_type
            else:
                dict["type_0"] = False
        except:
            pass
        try:
            dict["url"] = job_link
            dict["description"] = description 
        except:
            pass
        finally:       
            print("********{}".format(num+1))
            jobs_list.append(dict)
    return jobs_list