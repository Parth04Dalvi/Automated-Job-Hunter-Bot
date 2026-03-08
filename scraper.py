import requests
from bs4 import BeautifulSoup
import smtplib
import os
from email.message import EmailMessage

# --- CONFIGURATION ---
URLS = [
    "https://boards.greenhouse.io/airbnb", 
    "https://boards.greenhouse.io/stripe"
]
TARGET_ROLE = "Engineer"
MY_EMAIL = os.environ.get('EMAIL_USER')
MY_PASSWORD = os.environ.get('EMAIL_PASS')
DB_FILE = "seen_jobs.txt"

def get_seen_jobs():
    if not os.path.exists(DB_FILE):
        return set()
    with open(DB_FILE, "r") as f:
        return set(line.strip() for line in f)

def save_new_jobs(job_links):
    with open(DB_FILE, "a") as f:
        for link in job_links:
            f.write(link + "\n")

def scrape():
    seen_jobs = get_seen_jobs()
    new_jobs_found = []
    
    for url in URLS:
        print(f"Searching {url}...")
        try:
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            for job in soup.find_all('div', class_='opening'):
                title = job.find('a').text.strip()
                link = "https://boards.greenhouse.io" + job.find('a')['href']
                
                if TARGET_ROLE.lower() in title.lower() and link not in seen_jobs:
                    new_jobs_found.append(f"{title} - {link}")
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    return new_jobs_found

def send_email(jobs):
    msg = EmailMessage()
    msg.set_content("\n".join(jobs))
    msg['Subject'] = f"🚨 {len(jobs)} New Job Openings Found!"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(MY_EMAIL, MY_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    new_hits = scrape()
    if new_hits:
        send_email(new_hits)
        save_new_jobs([line.split(" - ")[1] for line in new_hits])
        print(f"Success! Notified about {len(new_hits)} jobs.")
    else:
        print("No new jobs found.")
