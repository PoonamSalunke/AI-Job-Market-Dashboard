# scrape_jobs.py
# Example script to scrape AI job postings (demo only).

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://example-job-portal.com/jobs?q=AI&start={}"

def scrape_jobs(pages=1):
    jobs = []
    for page in range(pages):
        print(f"Scraping page {page+1}...")
        url = BASE_URL.format(page * 10)
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch page")
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        postings = soup.find_all("div", class_="job-posting")
        for post in postings:
            title = post.find("h2").get_text(strip=True)
            company = post.find("span", class_="company").get_text(strip=True)
            location = post.find("span", class_="location").get_text(strip=True)
            salary = post.find("span", class_="salary")
            salary = salary.get_text(strip=True) if salary else "Not disclosed"
            jobs.append({
                "job_title": title,
                "company": company,
                "location": location,
                "salary": salary
            })
        time.sleep(2)
    return pd.DataFrame(jobs)

if __name__ == "__main__":
    df = scrape_jobs(pages=3)
    df.to_csv("data/scraped_ai_jobs.csv", index=False)
    print("Scraped data saved to data/scraped_ai_jobs.csv")
