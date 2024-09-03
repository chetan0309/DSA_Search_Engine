from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service('chromedriver.exe')

# Instantiate the webdriver
driver = webdriver.Chrome(service=s)

# The base URL for the pages to scrape
page_URL = "https://codeforces.com/problemset/page/"

def get_a_tags(url):
    # Load the URL in the browser
    driver.get(url)
    # Wait for 7 seconds to ensure the page is fully loaded
    time.sleep(7)
    # Find all the 'a' elements on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []
    # Iterate over each 'a' element
    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problem/" in i.get_attribute("href"):
                # If it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass
    # Remove duplicate links using set
    ans = list(set(ans))
    return ans

# def get_a_tags(url):
#     driver.get(url)
#     # Wait for the page to be fully loaded
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
#     links = driver.find_elements(By.TAG_NAME, "a")
#     ans = []
#     for i in links:
#         try:
#             if "/problem/" in i.get_attribute("href"):
#                 ans.append(i.get_attribute("href"))
#         except:
#             pass
#     ans = list(set(ans))
#     return ans

# List to store the final list of links
my_ans = []
# Loop through the pages you're interested in (in this case, pages 1-54)
for i in range(1, 85):
    # Call the function to get the 'a' tags from each page and append the results to your list
    my_ans += (get_a_tags(page_URL+str(i)))

# Remove any duplicates that might have been introduced in the process
# my_ans = list(set(my_ans))


# Open a file to write the results to
with open('cf.txt', 'a') as f:
    # Iterate over each link in your final list
    for j in my_ans:
        # Write each link to the file, followed by a newline
        f.write(j+'\n')

# Clear the my_ans list for the next page
my_ans.clear()

# Print the total number of unique links found
print(len(my_ans))

# Close the browser
driver.quit()