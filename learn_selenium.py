from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup():
    # Configure Firefox options
    options = Options()
    options.add_argument('--headless')

    # Initialize the Firefox driver
    return webdriver.Firefox(options=options)

def test_python_website():
    driver = setup()

    # Connect to the website under test
    driver.get("http://www.python.org")

    # Make an assertion (true/false)
    assert "Python" in driver.title

    # Get the Searchbar
    elem = driver.find_element(By.NAME, "q")

    # Clear the Searchbar
    elem.clear()

    # Simulate pressing the p, y, c, o, n keys on the keyboard
    elem.send_keys("pycon")

    # Simulate hitting the Enter key on the keyboard
    elem.send_keys(Keys.RETURN)

    # Make an assertion (true/false)
    assert "No results found." not in driver.page_source

    print('Python Website Test Successful')

    # Close the browser
    driver.close()
    driver.quit()

def test_weathershopper_temperature():
    driver = setup()

    url = "https://weathershopper.pythonanywhere.com/"
    driver.get(url)
    print(f"\nStarting at: {url}")

    # Get the element that houses the temperature value using its IDE
    temperature = driver.find_element(By.ID, "temperature").text

    # Get the temperature string value from the element
    print(f"The temperature is {temperature}.")

    # Remove celsius from the string so we can convert it to an integer
    temperatureValueOnly = temperature[0]
    print(f"The temperature value is {temperatureValueOnly}.")

    # int() converts a string into an integer, i.e. string(19) -> int(19)
    if int(temperatureValueOnly) > 19:
        print('Temperature was ABOVE 19 C: Clicking the Sunscreens button')
        # XPATH is one of the most reliable ways to find Elements
        buySunscreensButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Buy sunscreens')]")
        buySunscreensButton.click()
    else:
        print('Temperature was BELOW 19 C: Clicking the Moisturizers button')
        # XPATH is one of the most reliable ways to find Elements 
        buyMoisturizersButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Buy moisturizers')]")
        buyMoisturizersButton.click()

    print(f'Current webpage: {driver.current_url}.')
    assert driver.current_url == "https://weathershopper.pythonanywhere.com/sunscreen" or driver.current_url == "https://weathershopper.pythonanywhere.com/moisturizer"

    print('Weather Shopper Landing Page Test Successful')

    # Close the browser
    driver.close()
    driver.quit()

def test_weathershopper_sunscreen_page():
    driver = setup()

    url = "https://weathershopper.pythonanywhere.com/sunscreen"
    driver.get(url)
    print(f"\nStarting at: {url}")

    # Retrieve all sunscreen cards
    sunscreens = driver.find_elements(By.CLASS_NAME, "col-4")

    # Variables to store the least expensive SPF-50 and SPF-30 details
    cheapest_spf50_button = None
    cheapest_spf50_price = float("inf")
    cheapest_spf30_button = None
    cheapest_spf30_price = float("inf")

    # Loop through each sunscreen card
    for sunscreen in sunscreens:
        name = sunscreen.find_element(By.TAG_NAME, "p").text
        print(f"Sunscreen name: {name}")
        price_text = sunscreen.find_elements(By.TAG_NAME, "p")[1].text
        price = int(price_text.split(" ")[-1].strip())
        print(f"Price: {price}")
        button = sunscreen.find_element(By.TAG_NAME, "button")

        if "SPF-50" in name and price < cheapest_spf50_price:
            cheapest_spf50_price = price
            cheapest_spf50_button = button
        elif "SPF-30" in name and price < cheapest_spf30_price:
            cheapest_spf30_price = price
            cheapest_spf30_button = button

    # Add the least expensive SPF-50 sunscreen to the cart
    if cheapest_spf50_button:
        cheapest_spf50_button.click()

    # Add the least expensive SPF-30 sunscreen to the cart
    if cheapest_spf30_button:
        cheapest_spf30_button.click()

    print(f"The least expensive SPF-50 sunscreen is: {cheapest_spf50_price}")
    print(f"The least expensive SPF-30 sunscreen is: {cheapest_spf30_price}")

    # Click on the Cart button
    print('\nAdding them to the Cart.')
    cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Cart')]")
    cart_button.click()
    
    # Close the browser
    driver.close()
    driver.quit()

# Use this to print out the HTML of the web page you
# are writing a test for. Useful for identifying how you 
# will fetch specific elements etc.
def show_me_the_html(url):
    driver.get(url)
    print(driver.page_source)
    driver.close()

# Run the tests
test_python_website()
test_weathershopper_temperature()
test_weathershopper_sunscreen_page()