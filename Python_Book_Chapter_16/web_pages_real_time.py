import mechanicalsoup
import time

url = "http://olympus.realpython.org/dice"
browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get(url)
    tag = page.soup.select("#result")[0]
    time_tag = page.soup.select("#time")[0]
    result = tag.text
    result_time = time_tag.text
    print(f"The result of your dice roll is: {result} at {result_time}")
    if i < 3:
        time.sleep(10)

