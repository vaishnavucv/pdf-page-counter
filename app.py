from selenium import webdriver
import json

# Initialize WebDriver (Example with Chrome)
# Replace '/path/to/chromedriver' with the actual path to your ChromeDriver executable
driver = webdriver.Chrome("D:\X-CLASS\code\tryhackme\chromedriver.exe")

# Navigate to the website (replace 'https://www.example.com' with the actual URL)
driver.get("https://tryhackme.com/dashboard")

# Cookies JSON String (Replace this with your actual cookie JSON)
cookie_json = '[{"name": "_csrf", "value": "-aKi4W1DXmkOmg6bUfM6DZ-B"}, {"name": "intercom-id-pgpbhph6", "value": "03a13a2d-7052-4e10-b565-034994b4cb2b"}, {"name": "intercom-device-id-pgpbhph6", "value": "abd425f4-bbeb-4719-abe3-bbd26ec87a61"}, {"name": "logged-in-hint", "value": "true"}, {"name": "cookieconsent_status", "value": "dismiss"}, {"name": "AMP_d09a34bd2d", "value": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI2YTViZTRjZi03YThiLTQ3ZGUtODA4YS00MjA2M2YwMDRkNTQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjk5OTg5NjcwNjk1JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlN0Q="}, {"name": "AWSALB", "value": "lvo8mGXK++/uBZ6EpM9CC0WM2yPrpUvuFJQo8fQXgppnUFEpB7LMIbxGnKtSWrA2D8yfndAXmUah81Uf/4jG9rwH5sudmo0rdt7jgWKoMqy1jHBO8STb4AnSWIKL"}, {"name": "intercom-session-pgpbhph6", "value": "N3pDNWt5VDRGQlRyWjZpMjhaRzRSRUIycGh2SSs3WjBnaXlwVnZPOUU3eXhLZHN6bHNXNzRXMlMwZ1N5Q0VrcS0tL0RLeVVxbHJva3h2VW5jTjQ5UmZZZz09--f0ac4d7d7b3c53ad6d5e5606af1830f68f8b03615c"}]'

# Load cookies
cookies = json.loads(cookie_json)
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to apply cookies
driver.refresh()

# Now you can interact with the page as a logged-in user
# ...

# Close the driver when done
driver.quit()
