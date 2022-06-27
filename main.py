from playwright.sync_api import sync_playwright
import autotag.regex_objects as reobj

def login(page, username, password):
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

def parse_a_ticket(id):
    page.goto(f'https://help.reed.edu/Ticket/Display.html?id={id}')
    # Get the email address of the requestor
    email_handle = page.query_selector('.EmailAddress > .value')
    email = email_handle.inner_text()
    
    # Get the title of the ticket
    subject_handle = page.query_selector('h1')
    subject = subject_handle.inner_text()[9:]
    # Get all the messages and quotes of the ticket
    page.wait_for_load_state('networkidle')
    message_handles = page.query_selector_all('.messagebody')
    quote_handles = page.query_selector_all('.message-stanza.closed')
    contents = ''
    for message_handle in message_handles:
        message = message_handle.inner_text()
        # filter out the empty stirngs
        if message == '':
            continue
        # filter out the CUS auto-reply
        if reobj.autoReply[0].search(message):
            continue
        contents += message + '\n'
    for quote_handle in quote_handles:
        quote = quote_handle.inner_text()
        # filter out the empty stirngs
        if quote == '':
            continue
        # filter out the CUS auto-reply
        if reobj.autoReply[0].search(quote):
            continue
        contents += quote + '\n'
    
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


    