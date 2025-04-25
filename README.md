# LinkedIn Profile Scraper

This project is a LinkedIn profile scraper built using Python, Selenium, and Tkinter. It allows users to search LinkedIn for profiles based on a specific keyword, visit them, and save the profile URLs to a CSV file. The scraper can optionally use cookies to log in to LinkedIn, or it can log in using the user's credentials. The scraper also supports using a proxy server to anonymize the requests.

## Features

- **Search LinkedIn for profiles** based on a given keyword.
- **Visit profiles** and record their URLs.
- **Save profile URLs** to a CSV file.
- **Use cookie login** for easier re-login.
- **Support proxy servers** to mask your IP address.
- **Progress bar** to show the scraping progress.
- **Responsive UI** with Tkinter and ttkbootstrap.
- **Save cookies** for future login sessions.

## Requirements

- Python 3.6+
- Selenium
- ttkbootstrap
- ChromeDriver
- (Optional) Proxy server

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/LinkedIn-Profile-Scraper.git
cd LinkedIn-Profile-Scraper
```

### 2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Download ChromeDriver:

Ensure you have the appropriate version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) that matches your version of Chrome installed on your machine.

### 4. (Optional) Set up a proxy:

If you want to use a proxy server, you can provide the IP address and port in the "Proxy" input field in the GUI.

### 5. (Optional) Save cookies:

If you'd like to use cookie login, you can save your cookies by clicking the "Save Cookies" button after logging in manually once.

## Usage

1. **Start the app**: Run the `app.py` script.

```bash
python app.py
```

2. **Login**: Enter your LinkedIn email and password or use the cookie login feature.

3. **Set the search keyword**: Enter a keyword to search for profiles on LinkedIn.

4. **Set the max profiles**: Choose how many profiles you want to visit and scrape.

5. **Start scraping**: Click the "Start Scraping" button to begin the scraping process.

6. **View progress**: A progress bar will indicate the scraping status, and you can track how many profiles have been visited.

7. **Check saved profiles**: The scraped profile URLs will be saved in a CSV file on your desktop in a folder named "LinkedInProfiles."

## File Structure

```
LinkedIn-Profile-Scraper/
├── app.py                # Main application script
├── save_cookies.py       # Script to save LinkedIn cookies
├── requirements.txt      # Python dependencies
├── linkedin_cookies.pkl  # File to store LinkedIn cookies (if saved)
└── README.md             # Project README file
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Selenium](https://www.selenium.dev/) - Web scraping library.
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) - A modern and customizable theme for Tkinter.
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) - WebDriver for Chrome.
