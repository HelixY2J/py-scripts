# Overview

If we have multiple proxy servers that we use to connect to a certain resource for  web scraping or web crawling or to just get some information to send some requests to the API the problem is that we might get banned sooner or later as our IP address is going to get blocked on certain websites.They can recognize that we are always sending the requests from the same IP address and they might not have an interest in us web scraping their content

## Rotating proxy
We can use a rotating proxy here so we can have multiple proxy servers and can connect first with one proxy server then send the next request with the second one so that we can use a different IP address for different requests and we are not sending all the requests from the same IP address,This is the idea of  basic proxy rotation that is being shown by this program

We will use free proxy servers https://free-proxy-list.net/ for the task

A lot of these free proxy servers did not work for me, did not respond at all,some of them responded with a with an error code,
So we have a separate script to see which of those free proxies actually works

We can use this script with a web scraping program, here we will use just a book scraping webite http://books.toscrape.com/catalogue/category/books_1/index.html which is just a simple scraping source


