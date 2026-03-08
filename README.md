# 🚀 Automated Job Hunter Bot

An automated Python-based web scraper that monitors specific company career boards for job openings and sends instant email notifications when a match is found. 

Designed to run for free using **GitHub Actions**, this bot "remembers" which jobs it has already seen to ensure you never get the same notification twice.

---

## ✨ Features
* **Multi-Company Support:** Monitor multiple Greenhouse-powered career boards simultaneously.
* **Keyword Filtering:** Only get notified for roles that match your specific criteria (e.g., "Software Engineer", "Product Manager").
* **Automated Scheduling:** Runs every day at a set time via GitHub Actions (no local server required).
* **Smart Memory:** Uses a `seen_jobs.txt` database to prevent duplicate email alerts.
* **Secure:** Uses GitHub Secrets to keep your email credentials private.

---

## 🛠️ Architecture


The bot follows a simple logic flow:
1. **Trigger:** GitHub Actions wakes up the script on a cron schedule.
2. **Scrape:** Python visits the defined job boards.
3. **Filter:** Matches found titles against your `TARGET_ROLE` and checks against `seen_jobs.txt`.
4. **Notify:** If new matches exist, an email is sent via SMTP.
5. **Commit:** The bot updates the "seen" list and pushes the change back to the repository.

---

## 🚀 Setup Instructions

### 1. Prerequisites
* A GitHub account.
* A Gmail account (or any SMTP-enabled email).

### 2. Configure Gmail (Security)
To allow the bot to send emails, you must generate an **App Password**:
1. Go to your [Google Account Security](https://myaccount.google.com/security).
2. Enable **2-Step Verification**.
3. Search for **"App Passwords"**.
4. Create a new app named "JobBot" and copy the 16-character code.

### 3. Repository Secrets
In your GitHub repository, go to **Settings > Secrets and variables > Actions** and add the following two secrets:
* `EMAIL_USER`: Your full Gmail address.
* `EMAIL_PASS`: The 16-character App Password you just generated.

### 4. Customization
Edit `scraper.py` to match your job search:
* **COMPANIES:** Add the Greenhouse URLs for the companies you want to track.
* **TARGET_ROLE:** Set the keyword for the position you are looking for.

### 5. Enable Permissions
Because the bot needs to update `seen_jobs.txt`, you must grant it write access:
1. Go to **Settings > Actions > General**.
2. Scroll to **Workflow permissions**.
3. Select **Read and write permissions** and click **Save**.

---

## 📈 Usage
The bot is set to run automatically at **9:00 AM UTC daily**. 

To test it immediately:
1. Go to the **Actions** tab in your repository.
2. Select **Job Hunter Bot** on the left.
3. Click the **Run workflow** dropdown and press the button.

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
