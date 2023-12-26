from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the path to your ChromeDriver executable
serv_obj=Service("C:\z.selenium drivers\chromedriver-win64\chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

time.sleep(4)
# URL
url = 'https://jqueryui.com/droppable/'
driver.get(url)

# Switch to the frame containing the draggable elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame'))

time.sleep(4)
# Locate the draggable and droppable elements
draggable_element = driver.find_element(By.ID, 'draggable')
droppable_element = driver.find_element(By.ID, 'droppable')

time.sleep(4)
# Perform the drag and drop operation using Action Chains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable_element, droppable_element).perform()

print("Drag and drop Operation Completed!")

time.sleep(4)
# Close the browser
driver.close()
