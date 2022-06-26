from playwright.sync_api import sync_playwright
import autoTag.regexConstants as rc

def login(page_, username, password):
    page_.fill('input[name="login"]', username)
    page_.fill('input[name="password"]', password)
    page_.click('body > div > div.panel.panel-default > div.panel-body > form > button')

# Returns a list of tickets ids
def get_all_tickets(page):
    # Get the unresolved twatch tickets
    twatchHandle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0')
    twatchTickets = twatchHandle.query_selector_all('tbody.list-item')
    twatchIDs = []
    for ticket in twatchTickets:
        twatchIDs.append(ticket.get_attribute('data-record-id'))
    # Get the unresolved cus tickets
    cusHandle = page.query_selector('#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBDVVMgVGlja2V0cw__---0')
    cusTickets = cusHandle.query_selector_all('tbody.list-item')
    cusIDs = []
    for ticket in cusTickets:
        cusIDs.append(ticket.get_attribute('data-record-id'))
    return twatchIDs + cusIDs

def parse_a_ticket():
    page.goto('https://help.reed.edu/Ticket/Display.html?id=349273')
    # Get the affliation of the requestor
    primaryAffiliationHandle = page.query_selector('.CustomField__Primary_Affiliation_ > .value')
    print(primaryAffiliationHandle.inner_text())
    # Get the email address of the requestor
    emailHandle = page.query_selector('.EmailAddress > .value')
    print(emailHandle.inner_text())
    # Get the title of the ticket
    titleHandle = page.query_selector('h1')
    print(titleHandle.inner_text()[9:])
    # Get all the messages and quotes of the ticket
    page.wait_for_load_state('networkidle')
    messageHandles = page.query_selector_all('.messagebody')
    quoteHandles = page.query_selector_all('.message-stanza.closed')
    texts = ''
    for messageHandle in messageHandles:
        # filter out the empty stirngs
        if messageHandle.inner_text() == '':
            continue
        # filter out the CUS auto-reply
        if rc.autoReply in messageHandle.inner_text():
            continue
        texts += messageHandle.inner_text() + '\n'
    for quoteHandle in quoteHandles:
        # filter out the empty stirngs
        if quoteHandle.inner_text() != '':
            continue
        # filter out the CUS auto-reply
        if rc.autoReply in quoteHandle.inner_text():
            continue
        texts += quoteHandle.inner_text() + '\n'
    
    print(texts)
    # Check if the affliation tag is chosen, if yes, which one is chosen
    
    # Check if the support tag is chosen, if yes, which ones are chosen

















with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://help.reed.edu/Dashboards/757/T-watcher")
    # Log In.
    login(page, 'zhuyifang', '***REMOVED***')
    page.wait_for_load_state('networkidle')
    # Get all tickets.
    # ticketIds = get_all_tickets(page)
    # The format of ticket is https://help.reed.edu/Ticket/Display.html?id=349233
    # Go to all tickets
    # for id in ticketIds:
    #     page.goto(f'https://help.reed.edu/Ticket/Display.html?id={id}')
    
    parse_a_ticket()
    browser.close()


    