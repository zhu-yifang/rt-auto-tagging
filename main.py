from playwright.sync_api import sync_playwright
import autoTag.regexObjects as reobj

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

def parse_a_ticket(id):
    page.goto(f'https://help.reed.edu/Ticket/Display.html?id={id}')
    # Get the email address of the requestor
    emailHandle = page.query_selector('.EmailAddress > .value')
    email = emailHandle.inner_text()
    
    # Get the title of the ticket
    subjectHandle = page.query_selector('h1')
    subject = subjectHandle.inner_text()[9:]
    # Get all the messages and quotes of the ticket
    page.wait_for_load_state('networkidle')
    messageHandles = page.query_selector_all('.messagebody')
    quoteHandles = page.query_selector_all('.message-stanza.closed')
    contents = ''
    for messageHandle in messageHandles:
        message = messageHandle.inner_text()
        # filter out the empty stirngs
        if message == '':
            continue
        # filter out the CUS auto-reply
        if reobj.autoReply[0].search(message):
            continue
        contents += message + '\n'
    for quoteHandle in quoteHandles:
        quote = quoteHandle.inner_text()
        # filter out the empty stirngs
        if quote != '':
            continue
        # filter out the CUS auto-reply
        if reobj.autoReply[0].search(quote):
            continue
        contents += quoteHandle.inner_text() + '\n'
    
    # Check if the support tag is chosen, if yes, which ones are chosen

    # decide which tag to choose

    # mass email
    for rule in reobj.massEmailSubject:
        if rule.search(subject):
            print(f'{id} is a mass email')
            return 'mass email'
    # thesis format
    
    # two factor
    # name change
    # no tag
    # phish
    # google drive
    # google group
    # library
    # virus
    # password reset
    for rule in reobj.passwordResetSubject:
        if rule.search(subject):
            print(f'{id} is a password reset')
            return 'password reset'
    for rule in reobj.passwordResetEmail:
        if rule.search(email):
            print(f'{id} is a password reset')
            return 'password reset'
    for rule in reobj.passwordResetContent:
        if rule.search(contents):
            print(f'{id} is a password reset')
            return 'password reset'
    # printing
    # hardware
    # microsoft
    for rule in reobj.microsoftSubject:
        if rule.search(subject):
            print(f'{id} is a microsoft')
            return 'microsoft'
    for rule in reobj.microsoftEmail:
        if rule.search(email):
            print(f'{id} is a microsoft')
            return 'microsoft'
    for rule in reobj.microsoftContent:
        if rule.search(contents):
            print(f'{id} is a microsoft')
            return 'microsoft'
    # network
    # reed account
    # software
    # else
    















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
    
    parse_a_ticket(349580)
    browser.close()


    