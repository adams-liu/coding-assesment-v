from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# options.headless = True
driver.get("https://www.crudemonitor.ca/crudes/dist.php?acr=MSY&time=recent")
celcius_btn = driver.find_elements_by_xpath(
    "//label[@class='btn btn-seconday']")[0]
celcius_btn.click()
print(celcius_btn)
