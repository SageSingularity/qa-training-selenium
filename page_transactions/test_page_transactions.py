from selenium import webdriver
from selenium.webdriver.common.by import By
from guara.transaction import AbstractTransaction, Application
from guara import it


# Transaction for navigating to the weather page and interacting with the temperature
class WeatherPageTransaction(AbstractTransaction):
    def do(self, **kwargs):
        # Navigate to the weather page
        self._driver.get("https://weathershopper.pythonanywhere.com/")

        # Get the element that houses the temperature value
        temperature = self._driver.find_element(By.ID, "temperature").text

        # Extract the temperature value
        temperature_value_only = temperature[0]

        # Check temperature and click corresponding button
        if int(temperature_value_only) > 19:
            buy_sunscreens_button = self._driver.find_element(
                By.XPATH, "//button[contains(text(), 'Buy sunscreens')]"
            )
            buy_sunscreens_button.click()
        else:
            buy_moisturizers_button = self._driver.find_element(
                By.XPATH, "//button[contains(text(), 'Buy moisturizers')]"
            )
            buy_moisturizers_button.click()

        return self._driver.current_url


# Assertion to verify if the URL matches the expected ones for the sunscreen or moisturizer page
class VerifyWeatherPage(it.IAssertion):
    def asserts(self, result, expected_url):
        assert result == expected_url, f"Expected: {expected_url}, but got: {result}"


# Example of using Guará to validate the framework's capabilities
def test_weathershopper_temperature(browser):
    app = Application(browser)

    # Run the weather page transaction
    app.at(WeatherPageTransaction).asserts(
        it.Contains(),
        "https://weathershopper.pythonanywhere.com",
    )
