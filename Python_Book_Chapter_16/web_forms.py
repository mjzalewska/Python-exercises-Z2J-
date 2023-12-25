import mechanicalsoup

browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# login_page = browser.get(url)
# print(page) # yields response code
# print(page.soup) # print the html contents
# login_html = login_page.soup
#
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"
# profiles_page = browser.submit(form, login_page.url)
# print(profiles_page.url)
# links = profiles_page.soup.select("a")
# base_url = "http://olympus.realpython.org"
# for link in links:
#     address = base_url + link["href"]
#     text = link.text
#     print(f"{text}: {address}")


url = "http://olympus.realpython.org/login"
# return to the previous page
previous_page = browser.get(url)
# post incorrect login credentials
login_page_html = previous_page.soup
form = login_page_html.select("form")[0]
form.select("input")[0]["value"] = "aphrodite"
form.select("input")[1]["value"] = "BeautifulMama"
next_page = browser.submit(form, previous_page.url)
next_page_text = next_page.soup.get_text()
if "Wrong" in next_page_text:
    print("Login failed!")
else:
    print("Login succeeded!")
