import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'http://testphp.vulnweb.com/'
VECTOR = '<script>alert("kikoo")</script>'
ELEMENT_NAME = 'searchFor'

# Instanciates a Firefox webdriver browser
driver = webdriver.Firefox()

# Connect to the audited URL
driver.get(URL)

# Focus on appropriate element
element = driver.find_element_by_name(ELEMENT_NAME)

# Clear all previously information in the element
element.clear()

# Press keys to inject the XSS vector
element.send_keys(VECTOR)

# Press ENTER key
element.send_keys(Keys.ENTER)

# Have to sleep to be sure the DOM is fully generated
time.sleep(4)

try:
	# Try to focus to an alert window
    current_alert = driver.switch_to_alert()
    # Try to grab text within the alert window, if any
    alert = current_alert.text
    # Means that XSS is present
    print('[-] FAILED')
except Exception as e:
	# Means that XSS is NOT present
    print('[+] PASSED')

driver.quit()