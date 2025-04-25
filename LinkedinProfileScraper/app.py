import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading, time, csv, os, random, pickle
from pathlib import Path
import subprocess
import sys

# Function to start the scraper
def start_scraper_thread():
    threading.Thread(target=start_scraper, daemon=True).start()

def start_scraper():
    keyword = entry_keyword.get().strip()
    proxy = entry_proxy.get().strip() if use_proxy.get() else None
    use_cookie_login = cookie_toggle.get()

    try:
        max_profiles = int(entry_limit.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for Max Profiles.")
        return

    if not keyword:
        messagebox.showerror("Missing Keyword", "Please enter a keyword to search.")
        return

    if not use_cookie_login and (not entry_email.get().strip() or not entry_pass.get().strip()):
        messagebox.showerror("Login Required", "Please enter your email and password.")
        return

    btn_start.config(state="disabled")
    status.set("🔄 Launching browser...")

    desktop = Path.home() / "Desktop"
    save_folder = desktop / "LinkedInProfiles"
    save_folder.mkdir(parents=True, exist_ok=True)
    file_path = save_folder / "profiles.csv"

    options = webdriver.ChromeOptions()
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.linkedin.com/")
        time.sleep(2)

        if use_cookie_login:
            status.set("🍪 Loading saved cookies...")
            try:
                cookies = pickle.load(open("linkedin_cookies.pkl", "rb"))
                for cookie in cookies:
                    driver.add_cookie(cookie)
                driver.get("https://www.linkedin.com/feed/")
                time.sleep(3)
            except Exception as e:
                messagebox.showerror("Cookie Error", f"Failed to load cookies.\n\n{e}")
                driver.quit()
                return
        else:
            driver.get("https://www.linkedin.com/login")
            driver.find_element(By.ID, "username").send_keys(entry_email.get().strip())
            driver.find_element(By.ID, "password").send_keys(entry_pass.get().strip())
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(3)

        driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keyword}")
        time.sleep(5)

        profile_urls = set()
        visited = 0

        while visited < max_profiles:
            links = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')]")
            for link in links:
                url = link.get_attribute("href")
                if url and "/in/" in url and url not in profile_urls:
                    profile_urls.add(url)
                    visited += 1
                    status.set(f"👁 Viewing Profile [{visited}/{max_profiles}]")
                    driver.get(url)

                    wait_sec = random.randint(60, 180)
                    for i in range(wait_sec):
                        time.sleep(1)
                        progress["value"] = (i / wait_sec) * 100
                        status.set(f"⏳ Waiting {wait_sec - i}s before next...")

                    if visited >= max_profiles:
                        break

            driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keyword}")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        with open(file_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Profile URL"])
            for url in profile_urls:
                writer.writerow([url])

        status.set(f"✅ Finished! Saved to: {file_path}")
    except Exception as e:
        status.set(f"❌ Error: {e}")
    finally:
        driver.quit()
        btn_start.config(state="normal")
        progress["value"] = 0

# Function to save cookies
def save_cookies():
    script_path = os.path.join(sys._MEIPASS, "save_cookies.py") if hasattr(sys, '_MEIPASS') else "save_cookies.py"
    subprocess.Popen([sys.executable, script_path])

# --- GUI Setup ---
app = tb.Window(themename="darkly")  # Try: darkly, superhero, flatly
app.title("🔎 LinkedIn Profile Scraper  By Web3Elite Academy")
app.geometry("540x600")
app.resizable(False, False)

frame = tb.Frame(app, padding=15)
frame.pack(fill='both', expand=True)

def create_label(text):
    return tb.Label(frame, text=text, font=("Segoe UI", 11, "bold"), anchor="w")

# Keyword
create_label("🔍 Search Keyword").pack(fill="x", pady=(10, 0))
entry_keyword = tb.Entry(frame, font=("Segoe UI", 11))
entry_keyword.pack(fill="x", pady=(0, 10))

# Max profiles
create_label("📊 Max Profiles to Visit").pack(fill="x")
entry_limit = tb.Entry(frame, font=("Segoe UI", 11))
entry_limit.insert(0, "1000")
entry_limit.pack(fill="x", pady=(0, 10))

# Cookie login toggle
cookie_toggle = tk.BooleanVar()
tb.Checkbutton(frame, text="🍪 Use Cookie Login", variable=cookie_toggle, bootstyle="info-round-toggle").pack(anchor='w', pady=5)

# Email
create_label("📧 LinkedIn Email").pack(fill="x")
entry_email = tb.Entry(frame, font=("Segoe UI", 11))
entry_email.pack(fill="x", pady=(0, 10))

# Password
create_label("🔐 LinkedIn Password").pack(fill="x")
entry_pass = tb.Entry(frame, show="*", font=("Segoe UI", 11))
entry_pass.pack(fill="x", pady=(0, 10))

# Proxy toggle
use_proxy = tk.BooleanVar()
tb.Checkbutton(frame, text="🌍 Use Proxy Server", variable=use_proxy, bootstyle="info-round-toggle").pack(anchor='w', pady=5)

# Proxy input
create_label("🔁 Proxy (IP:Port)").pack(fill="x")
entry_proxy = tb.Entry(frame, font=("Segoe UI", 11))
entry_proxy.insert(0, "123.45.67.89:8080")
entry_proxy.pack(fill="x", pady=(0, 10))

# Start Button
btn_start = tb.Button(frame, text="🚀 Start Scraping", bootstyle="success-outline", width=25, command=start_scraper_thread)
btn_start.pack(pady=15)

# Progress + Status
progress = tb.Progressbar(frame, bootstyle="info-striped", length=400, mode='determinate')
progress.pack(fill="x", pady=5)

status = tk.StringVar(value="💤 Idle and ready")
tb.Label(frame, textvariable=status, font=("Segoe UI", 10), foreground="lightgray").pack(fill="x", pady=(10, 0))

# Add Save Cookies Button
tb.Button(frame, text="💾 Save Cookies", command=save_cookies).pack(pady=10)

app.mainloop()
