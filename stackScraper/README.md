## Overview
stackSraper can scrape questions from Stack Overflow based on different tabs (e.g., newest, active) and page numbers. It extracts information such as question title, number of answers, views, and votes and saves it to a CSV file

### Installation

Clone the repository 

Install the required Python packages
```python
pip install -r requirements.txt
```

### Troubleshooting 

You might get an error message indicating that there is an issue with SSL certificate verification due to python requests library being unable to verify the SSL certificate of the website. 

I just ignored SSL certificate verification but that is not recommeded though for security reasons 
```python
response = requests.get(url, verify=False)
```
Try this or update certifi which is a python package that provides Mozilla carefully curated collection of Root Certificates for validating the SSL certificates
```python
pip install --upgrade certifi
```
