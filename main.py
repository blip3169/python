from selenium import webdriver
import time

def main():
    # Initialize the WebDriver and specify the path to chromedriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Navigate to the URL
    driver.get('https://kick.com/internetentourage')

    # Optional: Simulate some interactions
    # For example, to click a button with the ID 'playButton':
    # driver.find_element_by_id('playButton').click()

    # Wait for a few seconds
    time.sleep(5)

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
