import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")
## HTML tag
print('\n---------搜尋第一個符合條件的 HTML tag，傳入要搜尋的 tag 名稱----------\n')
result = soup.find("h3")
print(result)

print('\n---------搜尋網頁中所有符合條件的 HTML tag，傳入要搜尋的 HTML tag名稱----------\n')
result = soup.find_all("h3", itemprop="headline", limit=3)
print(result)

print('\n---------同時搜尋多個 HTML tag----------\n')
result = soup.find_all(["h3", "p"], limit=2)
print(result)

print('\n---------搜尋單個 HTML 子元素----------\n')
result = soup.find("h3", itemprop="headline")
print(result.select_one("a"))

print('\n---------搜尋多個 HTML 子元素----------\n')
result = soup.find("h3", itemprop="headline")
print(result.select("a"))

## CSS attribute
print('\n---------搜尋第一個符合條件的 HTML tag 及 css attribute----------\n')
titles = soup.find("p", class_="summary")
print(titles)

print('\n---------搜尋所有符合條件的 HTML tag 及 css attribute----------\n')
titles = soup.find_all("p", class_="summary", limit=3)
print(titles)

print('\n---------單純透過 css  attribute 進行搜尋----------\n')
titles = soup.select(".summary", limit=3)
print(titles)

print('\n---------搜尋 parent node----------\n')
result = soup.find("a", itemprop="url")
parents = result.find_parents("h3")
print(parents)

print('\n---------搜尋同一層前一個節點----------\n')
result = soup.find("h3", itemprop="headline")
previous_node = result.find_previous_siblings("a")
print(previous_node)

print('\n---------搜尋同一層後一個節點----------\n')
result = soup.find("h3", itemprop="headline")
next_node = result.find_next_siblings("p")
print(next_node)

print('\n----------取得 href attribute---------\n')
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").get("href"))

print('\n---------取得 a tag 的連結文字----------\n')
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())