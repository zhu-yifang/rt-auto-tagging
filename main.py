from playwright.sync_api import sync_playwright
import auto_tag.regex_objects as reobj
import auto_tag.ticket as ticket
import auto_tag.rt_operations as ops

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Log In.
        page.wait_for_load_state('networkidle')
        # Get all tickets.
        # ticketIds = get_all_tickets(page)
        # The format of ticket is https://help.reed.edu/Ticket/Display.html?id=349233
        # Go to all tickets
        # for id in ticketIds:
        #     page.goto(f'https://help.reed.edu/Ticket/Display.html?id={id}')
        
        browser.close()


    