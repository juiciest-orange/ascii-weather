# ascii-weather
Convert radar weather images of Lake Tahoe to fun ascii art and host on my Raspberry Pi web server as a html file.

How it works:
Use Selenium and Chromium webdriver to take a screenshot of this weather site: https://www.weatherbug.com/weather-forecast/now/lake-tahoe-ca-95728

The screenshot is then cropped to just the relevant area I want (of Lake Tahoe! Lol).

The cropped screenshot is converted to ascii art via a Python package called ascii-magic. 

The ascii art is saved in an html page, which I then host on my own Raspberry Pi web server.

Example:
<img width="977" alt="Screenshot 2025-04-18 at 11 17 22 PM" src="https://github.com/user-attachments/assets/ce9fdb09-c68d-4a73-b792-f2fdf7b7f9c1" />
