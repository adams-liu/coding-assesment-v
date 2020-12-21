from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import timeit


# load up a chrome driver object
def load_chrome_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


# run selenium to get the most recent oil distillation temperataures (in C)
def get_distillation_temps(driver, url):

    try:
        driver.get(url)
        celcius_btn = driver.find_elements_by_css_selector(
            "label.btn-seconday")[0]
        celcius_btn.click()

        # scrape all celcius temperature values in the distallation table using selenium's css_selector
        temps = driver.find_elements_by_css_selector(
            "#tblData div.table-responsive td.celsius")

        # parse through the scraped data and return a list of the all the temperatures for the first column (recent data)
        temp_list = []
        for i in range(3, 39):
            if (i+1) % 3 == 1:
                if temps[i].text == '-':
                    temp_list.append(float("NaN"))
                else: 
                    temp_list.append(float(temps[i].text))
        return temp_list

    except:
        print("**Error: invalid url or invalid driver module**")
        return []


# url = "https://www.crudemonitor.ca/crudes/dist.php?acr=MSY&time=recent"
# driver = load_chrome_driver()
# temp = get_distillation_temps(driver, url)
# print(temp)
