from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://help.reed.edu/Dashboards/757/T-watcher")
    # login
    page.fill('input[name="login"]', "zhuyifang")
    page.fill('input[name="password"]', "***REMOVED***")
    page.click('body > div > div.panel.panel-default > div.panel-body > form > button')
    page.wait_for_load_state('networkidle')
#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0 > table > tbody:nth-child(2)
#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0 > table > tbody:nth-child(6)
    page.screenshot(path=f"screenshot.png")
    browser.close()


    