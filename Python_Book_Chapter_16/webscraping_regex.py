# webscraping
from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page_contents = page.read().decode("utf-8")
# print(page_contents)

# extracting information

### string methods ###
title_index = page_contents.find("<title>")
start_index = title_index + len("<title>")
end_index = page_contents.find("</title>")
title = page_contents[start_index:end_index]

new_url = "http://olympus.realpython.org/profiles/poseidon"
new_page_contents = urlopen(new_url).read().decode("utf-8")
# print(new_page_contents)
new_title_index = new_page_contents.find("<title>")
new_start_index = new_title_index + len("<title")
new_end_index = new_page_contents.find("</title>")
new_title = new_page_contents[new_start_index:new_end_index]
# print(new_title)

# regular expressions


# * - stands for zero or more of what stands before *
# e.g. "a*bc" matches any substring that starts with a, ends with c and has zero or more instances of b

# .* - any character repeated any number of times
# e.g. a.*c - find every substring starting with a and ending with c regardless of what stands in between them
# . - stands for any single character in a regular expression
# *? - works the same as * but tries to match the shortes possible string

### RE.FINDALL
# re.findall(regex, test_string), returns a list of matches
# to make the search ignore case: re.findall(regex, test_string, re.IGNORECASE)
# e.g. re.findall("a*bc", "ac") # returns 'ac'

### RE.SEARCH
# re.search() returns a MatchObject
# calling .group() on a MatchObject returns the first and most inclusive result
# match_results = re.search("ab*c", "ABC", re.IGNORECASE).group()
# print(match_results)

### RE.SUB
# re.sub() - to replace text in a string that matches a regular expression with new text
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
# print(string) #Everything is ELEPHANTS.
# the regex "<.*>" replaces everything between the first < in <replaced> and the last > in <tags>.
# regular expressions are greedy - try to find the longest possible match when such expressions as * are used
# (use *? for non-greedy search pattern)
new_string = "Everything is <replaced> if it's in <tags>."
new_string = re.sub("<.*?>", "ELEPHANTS", new_string)
# print(new_string)

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE).group()
title = re.sub("<.*?>", "", match_results)
# print(title)

### REVIEW EXERCISES
"""(1) Write a program that grabs the full HTML from the web page http://olympus.realpython.org/profiles/dionysus"""
my_url = "http://olympus.realpython.org/profiles/dionysus"
html = urlopen(my_url).read().decode("utf-8")
print(html)

"""(2) Use the string .find() method to display the text following "Name:" and "Favorite Color:" (not including 
any leading spaces or trailing HTML tags that might appear on the same line)."""
name_tag_idx = html.find("<h2>")
name_start_idx = name_tag_idx + len("<h2>") + len("Name: ")
name_end_idx = html.find("</h2>")
name = html[name_start_idx: name_end_idx]
# print(name)

color_tag_idx = html.find("Favorite Color: ")
color_start_idx = color_tag_idx + len("Favorite Color: ")
color_end_idx = html.find("</center>")
color = html[color_start_idx: color_end_idx]
# print(color)

# model answer
# html_page = urlopen(url)
# html_text = html_page.read().decode("utf-8")
# for tag in ["Name: ", "Favorite Color: "]:
#     tag_start = html_text.find(tag) + len(tag)
#     tag_end = html_text[tag_start:].find("<")
#     # Remove extra spaces and newline padding
#     print(html_text[tag_start : tag_start + tag_end].strip(" \n"))

"""(3) Repeat the previous exercise using regula expressions"""
patterns = ["Name: .*?<", "Color:.*?\n"]
for pattern in patterns:
    text = re.findall(pattern, html, re.IGNORECASE)
    for item in text:
        clean_item = re.sub(".*: ", "", item).replace("<", "").strip()
        print(clean_item)

# model answer:
# Match anything up until a new line or HTML tag; non-greedy
for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html)
    # Remove the "Name: " or "Favorite Color: " label from first result
    result = re.sub(".*: ", "", match_results.group())
    # Remove extra spaces and newline padding along with opening HTML tag
    print(result.strip(" \n<"))