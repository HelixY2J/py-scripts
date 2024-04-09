import requests

target_sites =  ["http://books.toscrape.com/catalogue/category/books/romance_8/index.html",
                 "http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
                 "http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
                 "http://books.toscrape.com/catalogue/category/books/art_25/index.html",
                 "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html"]

count = 0


with open("./valid_proxies.txt") as file:
    proxies = file.read().split("\n")



for site in target_sites:
    try:
        print(f"Using this proxy: {proxies[count]}")
        res = requests.get(site,proxies={"http":proxies[count],"https":proxies[count]})
        print(res.status_code)
        print(res.text)
    except:
        print("Operation failed")
    finally:
        count += 1
        count % len(proxies) # if we more sites to scrape than proxies




