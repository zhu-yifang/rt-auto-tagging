from playwright.sync_api import sync_playwright

def login(page_, username, password):
    page_.fill('input[name="login"]', username)
    page_.fill('input[name="password"]', password)
    page_.click('body > div > div.panel.panel-default > div.panel-body > form > button')

# returns a list of tickets ids
def get_all_tickets(page):
    # get the unresolved twatch tickets
    twatchHandle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0')
    twatchTickets = twatchHandle.query_selector_all('tbody.list-item')
    twatchIDs = []
    for ticket in twatchTickets:
        twatchIDs.append(ticket.get_attribute('data-record-id'))
    # get the unresolved cus tickets
    cusHandle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBDVVMgVGlja2V0cw__---0')
    cusTickets = cusHandle.query_selector_all('tbody.list-item')
    cusIDs = []
    for ticket in cusTickets:
        cusIDs.append(ticket.get_attribute('data-record-id'))
    return twatchIDs + cusIDs

def parse_a_ticket():
    page.goto('https://help.reed.edu/Ticket/Display.html?id=349159')
    # get the affliation of the requestor
    primaryAffiliation = page.query_selector('.CustomField__Primary_Affiliation_ > .value')
    print(primaryAffiliation.inner_html())
    # get the title of the ticket
    title = page.query_selector()
    # get all the emails of the ticket

    # check if the affliation tag is chosen, if yes, which one is chosen

    # check if the support tag is chosen, if yes, which ones are chosen
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://help.reed.edu/Dashboards/757/T-watcher")
    # login
    login(page, 'zhuyifang', '***REMOVED***')
    page.wait_for_load_state('networkidle')
    # get all tickets
    # ticketIds = get_all_tickets(page)
    # the format of ticket is https://help.reed.edu/Ticket/Display.html?id=349233
    # go to all tickets
    # for id in ticketIds:
    #     page.goto(f'https://help.reed.edu/Ticket/Display.html?id={id}')
    parse_a_ticket()
    browser.close()


    