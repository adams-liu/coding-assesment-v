from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import timeit


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.crudemonitor.ca/crudes/dist.php?acr=MSY&time=recent")
celcius_btn = driver.find_elements_by_css_selector("label.btn-seconday")[0]
celcius_btn.click()


def test2():
    # locate temperature element using css_selector (fastes)
    temp = driver.find_elements_by_css_selector(
        "#tblData div.table-responsive td.celsius")
    tempLs = []

    for i in range(3, 39):
        if (i+1) % 3 == 1:
            tempLs.append(temp[i].text)

    print(tempLs)


t = timeit.timeit("test2()", setup="from __main__ import test2", number=1)
print(t)
