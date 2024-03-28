from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint
import json

def build_url(tab="newest", page=1):
    base_url = "https://stackoverflow.com/questions"
    return f"{base_url}?tab={tab}&page={page}"

def scrape_page(url,page=1):
    response = requests.get(build_url(page=page))
    page_questions = []
    soup = BeautifulSoup(response.text, "html.parser")
    question_summary = soup.find_all("div", class_="question-summary")
    

    for summary in question_summary:
        question = summary.find(class_="question-hyperlink").text
        vote_count = summary.find(class_="vote-count-post").find("strong").text
        answers_count = summary.find(class_="status").find("strong").text
        view_count = summary.find(class_="views").text.split()[0]
        page_questions.append({
            "question":  question,
            "answers": answers_count,
            "views": view_count,
            "votes": vote_count
        })
    page_ques = json.dumps(page_questions)
    return page_ques

def scrape(tab, page_limit):
    questions = []
    for page in range(1, page_limit + 1):
        url = build_url(tab, page)
        page_questions = scrape_page(url,page_limit)
        questions.extend(page_questions)
    return questions

def export_data(questions):
    with open("data.csv", "w", newline="", encoding="utf-8") as data_file:
        fieldnames = ["answers", "question", "views", "votes"]
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        data_writer.writeheader()
        print("Questions:", questions) 
        for d in questions:

            row_data = {
                fieldnames[0]:d[0],fieldnames[1]:d[1],fieldnames[2]:d[2]
                # "answers": d.get("answers", ""),  # Use get method to handle missing keys
                # "question": d.get("question", ""),
                # "views": d.get("views", ""),
                # "votes": d.get("votes", "")
            }
            data_writer.writerow(row_data)
            
        print("Data exported to data.csv")

if __name__ == "__main__":
    tab = input("Enter the tab (newest, active etc): ")
    page_limit = int(input("Enter the number of pages to scrape: "))
    questions = scrape(tab, page_limit) 
    export_data(questions)#pprint("data:",d)

    
