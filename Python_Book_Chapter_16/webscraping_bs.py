from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text().replace("\n", " ")
# print(text)
image_urls = soup.find_all("img")
# for item in image_urls:
#     print(type(item))
# for item in image_urls:
#     print(item.name) # tag name
#     print(item["src"])# tag attribute
# print(soup.title) # get the title with tags
# print(soup.title.string) # get the title string only

# search for a specific tag with a specific attribute
# print(soup.find_all("img", src="/static/dionysus.jpg"))

### REVIEW EXERCISES

"""(1) Write a program that grabs the full HTML from the web page http://olympus.realpython.org/profiles"""
url = "http://olympus.realpython.org/profiles"
html = urlopen(url).read().decode("utf-8")
# print(html)

"""(2) Using Beautiful Soup, parse out a list of all the links on the page by looking for HTML tags with the name
a and retrieving the value taken on by the href attribute of each tag"""
soup = BeautifulSoup(html, "html.parser")
links = [link["href"] for link in soup.find_all("a")]
# print(links)

"""(3) Get the HTML of each of the pages in the list by adding the full path to the file name, and 
display the text (without HTML tags) on each page using Beautiful Soup's .get_text() method"""
main_page = "http://olympus.realpython.org"
full_paths = [(main_page + link) for link in links]
print(full_paths)
for path in full_paths:
    html_contents = urlopen(path).read().decode("utf-8")
    soup = BeautifulSoup(html_contents, "html.parser")
    print(soup.get_text().replace("\n", " "))


