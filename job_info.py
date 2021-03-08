from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

def printer(a):
    print(a)

def each_job(jobs_list,driver,delay):
    
    found_jobs=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,'//ul[starts-with(@class,"jobs-search-results")]')))
    jobs = found_jobs.find_elements_by_xpath('li')
    
    for num,job in enumerate(jobs):
        dict = {}
        try:
            job_name = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]').text
            job_link = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]').get_attribute('href')
            job_obj = job.find_element_by_xpath('.//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')
            job_obj.click()

            description = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,'//div[@id="job-details"]/span'))).text
            subl = driver.find_elements_by_xpath('.//div[@class="jobs-box__group"]')
            
            #job features
            for sub_obj in subl:
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

            if job_name:
                dict["name"] = job_name  
            else:
                dict["name"] = False
        except:
            pass
        try:   
            salary = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.XPATH,'//div[starts-with(@class,"artdeco-card")]/p/span'))).text
            if salary:
                dict["wage"] = salary
            else:
                dict["wage"] = "null"
        except:
            pass
        try:   
            job_inc = job.find_element_by_xpath('.//a[@class="job-card-container__link job-card-container__company-name ember-view"]').text
            if job_inc:
                dict["company"] = job_inc
            else:
                dict["company"] = "null"
        except:
            pass
        try:
            job_geo = job.find_element_by_xpath('.//li[@class="job-card-container__metadata-item"]').text
            if job_geo:
                dict["location"] = job_geo
            else:
                dict["location"] = False
        except:
            pass
        try:
            job_type = job.find_element_by_xpath('.//li[@class="job-card-container__metadata-item"][2]').text
            if job_type:
                dict["type_0"] = job_type
            else:
                dict["type_0"] = False
        except:
            pass
        finally:
            dict["url"] = job_link
            dict["description"] = description        
            print("********{}".format(num+1))
            jobs_list.append(dict)
    return jobs_list