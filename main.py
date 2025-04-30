import undetected_chromedriver as uc

def main():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-background-networking')
    options.add_argument('--disable-default-apps')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-sync')
    options.add_argument('--disable-translate')
    options.add_argument('--metrics-recording-only')
    options.add_argument('--mute-audio')
    options.add_argument('--no-first-run')
    options.add_argument('--safebrowsing-disable-auto-update')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-software-rasterizer')

    driver = uc.Chrome(options=options, browser_executable_path="/opt/chrome/chrome")

    try:
        driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2Fproduct%2Fgornyy-velosiped-forward-sporting-sx-27-5-19-rost-1841072929")
        driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2Fproduct%2Fgornyy-velosiped-forward-sporting-sx-27-5-19-rost-1841072929")

        with open("output.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
