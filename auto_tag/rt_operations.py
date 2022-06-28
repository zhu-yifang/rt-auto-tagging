def login(page, username, password):
    page.goto("https://help.reed.edu/Dashboards/757/T-watcher")
    page.fill('input[name="login"]', username)
    page.fill('input[name="password"]', password)
    page.click('body > div > div.panel.panel-default > div.panel-body > form > button')

# Returns a list of tickets ids
def get_all_tickets(page):
    # Get the unresolved twatch tickets
    twatch_handle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0')
    twatch_tickets = twatch_handle.query_selector_all('tbody.list-item')
    twatch_ids = []
    for ticket in twatch_tickets:
        twatch_ids.append(ticket.get_attribute('data-record-id'))
    # Get the unresolved cus tickets
    cus_handle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBDVVMgVGlja2V0cw__---0')
    cus_tickets = cus_handle.query_selector_all('tbody.list-item')
    cus_ids = []
    for ticket in cus_tickets:
        cus_ids.append(ticket.get_attribute('data-record-id'))
    return twatch_ids + cus_ids