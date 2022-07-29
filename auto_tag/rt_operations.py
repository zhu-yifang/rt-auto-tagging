async def login(page, username, password):
    await page.goto("https://help.reed.edu/Dashboards/757/T-watcher")
    await page.fill('input[name="login"]', username)
    await page.fill('input[name="password"]', password)
    await page.click(
        'body > div > div.panel.panel-default > div.panel-body > form > button'
    )


# Get all unsolved tickets in the twatch queue and the cus queue
# Returns a list of tickets ids
async def get_unsolved_tickets(page):
    # Get the unresolved twatch tickets
    twatch_handle = await page.query_selector(
        '#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBUd2F0Y2ggVGlja2V0cw__---0'
    )
    twatch_tickets = await twatch_handle.query_selector_all('tbody.list-item')
    twatch_ids = []
    for ticket in twatch_tickets:
        twatch_ids.append(ticket.get_attribute('data-record-id'))
    # Get the unresolved cus tickets
    cus_handle = await page.query_selector(
        '#TitleBox--_Dashboards_dhandler------VW5yZXNvbHZlZCBDVVMgVGlja2V0cw__---0'
    )
    cus_tickets = await cus_handle.query_selector_all('tbody.list-item')
    cus_ids = []
    for ticket in cus_tickets:
        cus_ids.append(ticket.get_attribute('data-record-id'))
    return twatch_ids + cus_ids


# this is a test function
async def get_tickets(page):
    await page.goto(
        "https://help.reed.edu/Search/Results.html?Format=%27%3Cb%3E%3Ca%20href%3D%22__WebPath__%2FTicket%2FDisplay.html%3Fid%3D__id__%22%3E__id__%3C%2Fa%3E%3C%2Fb%3E%2FTITLE%3A%23%27%2C%0A%27%3Cb%3E%3Ca%20href%3D%22__WebPath__%2FTicket%2FDisplay.html%3Fid%3D__id__%22%3E__Subject__%3C%2Fa%3E%3C%2Fb%3E%2FTITLE%3ASubject%27%2C%0AStatus%2C%0AQueueName%2C%0AOwner%2C%0APriority%2C%0A%27__NEWLINE__%27%2C%0A%27__NBSP__%27%2C%0A%27%3Csmall%3E__Requestors__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__CreatedRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__ToldRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__LastUpdatedRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__TimeLeft__%3C%2Fsmall%3E%27&Order=ASC%7CASC%7CASC%7CASC&OrderBy=id%7C%7C%7C&Query=Queue%20%3D%20%27cus%27%20AND%20Created%20%3C%20%272022-03-01%27%20AND%20Created%20%3E%20%272022-01-31%27%20AND%20id%20%3C%20337918&RowsPerPage=0&SavedChartSearchId=new&SavedSearchId=new"
    )
    ticket_handles = await page.query_selector_all('.list-item')
    ids = []
    for handle in ticket_handles:
        ids.append(await handle.get_attribute('data-record-id'))
    return ids
