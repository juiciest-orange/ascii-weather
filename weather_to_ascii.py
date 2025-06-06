from ascii_magic import AsciiArt
from PIL import ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime as dt
import cv2
import os

print('[%s] Python Radar Weather Image to ASCII Conversion' %dt.now().strftime("%Y-%m-%d %H:%M:%S"))

# path to selenium server standalone jar, downloaded here:
# http://docs.seleniumhq.org/download/
# or a direct url:
# http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
# os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
# note: I've put this jar file in the same folder as this python file

# Start Webdriver for Chrome
cService = webdriver.ChromeService('/usr/bin/chromedriver')
browser = webdriver.Chrome(service = cService)
url = "https://www.weatherbug.com/weather-forecast/now/lake-tahoe-ca-95728"
browser.get(url)
path = os.getcwd()+'/scrape.png'
browser.implicitly_wait(5)
el = browser.find_element(By.TAG_NAME, 'map-widget')
el.screenshot(path)
# browser.save_screenshot(path)
browser.quit()

# Crop the scraped image
image = cv2.imread(path)
# Define the cropping coordinates (y_start:y_end, x_start:x_end)
y_start, y_end = 100, 500
x_start, x_end = 150, 350

# Crop the image
cropped_image = image[y_start:y_end, x_start:x_end]
# Save the cropped image
cv2.imwrite(os.getcwd()+'/cropped_image.png', cropped_image)

my_art = AsciiArt.from_image(os.getcwd()+'/cropped_image.png')
my_art.to_html_file('/var/www/html/ascii_art.html', columns=200, width_ratio=2,
                   additional_styles='font-size: 1;')

# Cleanup files
os.remove(os.getcwd()+'/cropped_image.png')
os.remove(os.getcwd()+'/scrape.png')
