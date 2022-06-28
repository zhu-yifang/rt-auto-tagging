from playwright.sync_api import sync_playwright
import regex_objects as reobj
import rt_operations as ops

'''
模块的说明文档
'''

class Ticket:
    def __init__(self, id):
        self.id = id
        self.subject = ''
        self.email = ''
        self.contents = ''
        self.tags = set()
        self.auto_tag = set()
    
    def __str__(self):
        return f'{self.id}: {self.subject}, {self.email}, {self.tags}, {self.auto_tag}'

    # get the ticket's subject, email, contents
    def get_info(self, page):
        page.goto(f'https://help.reed.edu/Ticket/Display.html?id={self.id}')
        # Get the email address of the requestor
        email_handle = page.query_selector('.EmailAddress > .value')
        self.email = email_handle.inner_text()
        
        # Get the title of the ticket
        subject_handle = page.query_selector('h1')
        self.subject = subject_handle.inner_text()[9:]

        # Get the tags of the ticket
        tag_handles = page.query_selector_all('#CF-354-ShowRow > .value')
        for tag_handle in tag_handles:
            self.tags.add(tag_handle.inner_text())

        # Get all the messages and quotes of the ticket
        page.wait_for_load_state('networkidle')
        message_handles = page.query_selector_all('.messagebody')
        quote_handles = page.query_selector_all('.message-stanza.closed')
        for message_handle in message_handles:
            message = message_handle.inner_text()
            # filter out the empty stirngs
            if message == '':
                continue
            # filter out the CUS auto-reply
            if reobj.auto_reply[0].search(message):
                continue
            self.contents += message + '\n'
        for quote_handle in quote_handles:
            quote = quote_handle.inner_text()
            # filter out the empty stirngs
            if quote == '':
                continue
            # filter out the CUS auto-reply
            if reobj.auto_reply[0].search(quote):
                continue
            self.contents += quote + '\n'
    
    def check_match(self):
        if self.tags == self.auto_tag:
            return True
        else:
            return False

    # decide which tag to choose
    def parse(self):
        # mass email
        if self.is_mass_email():
            return True
        # thesis format
        elif self.is_microsoft():
            if self.is_thesis():
                return True
            elif self.is_password_reset():
                return True
        # two factor
        elif self.is_two_factor():
            return True
        # name change
        elif self.is_name_change():
            return True
        # no tag
        elif self.is_no_tag():
            return True
        # phish
        elif self.is_phish():
            return True
        # google drive
        elif self.is_google_drive():
            return True
        # google group
        elif self.is_google_group():
            return True
        # library
        elif self.is_library():
            return True
        # virus
        elif self.is_virus():
            return True
        # password reset
        elif self.is_password_reset():
            return True
        # printing
        elif self.is_printing():
            return True
        # hardware
        elif self.is_hardware():
            return True
        # microsoft
        elif self.is_microsoft():
            return True
        # network
        elif self.is_network():
            return True
        # reed account
        elif self.is_reed_account():
            return True
        # software
        elif self.is_software():
            return True
        # else
        else:
            print(f'{self.id} needs to be tagged manually')
    
    def is_mass_email(self):
        for rule in reobj.mass_email_subject:
            if rule.search(self.subject):
                self.auto_tag.add('mass email')
                return True
        return False
    
    def is_thesis(self):
        for rule in reobj.thesis_subject:
            if rule.search(self.subject):
                self.auto_tag.add('thesis')
                return True
        for rule in reobj.thesis_content:
            if rule.search(self.email):
                self.auto_tag.add('thesis')
                return True
        return False

    def is_two_factor(self):
        for rule in reobj.two_factor_subject:
            if rule.search(self.subject):
                self.auto_tag.add('two-factor')
                return True
        for rule in reobj.two_factor_content:
            if rule.search(self.email):
                self.auto_tag.add('two-factor')
                return True
        return False

    def is_name_change(self):
        for rule in reobj.name_change_subject:
            if rule.search(self.subject):
                self.auto_tag.add('user/name change')
                return True
        for rule in reobj.name_change_content:
            if rule.search(self.email):
                self.auto_tag.add('user/name change')
                return True
        return False

    def is_no_tag(self):
        for rule in reobj.no_tag_subject:
            if rule.search(self.subject):
                self.auto_tag.add('no tag')
                return True
        for rule in reobj.no_tag_email:
            if rule.search(self.email):
                self.auto_tag.add('no tag')
                return True
        return False

    def is_phish(self):
        for rule in reobj.phish_subject:
            if rule.search(self.subject):
                self.auto_tag.add('phish report/fwd')
                return True
        for rule in reobj.phish_email:
            if rule.search(self.email):
                self.auto_tag.add('phish report/fwd')
                return True
        for rule in reobj.phish_content:
            if rule.search(self.email):
                self.auto_tag.add('phish report/fwd')
                return True
        return False

    def is_google_drive(self):
        for rule in reobj.google_drive_subject:
            if rule.search(self.subject):
                self.auto_tag.add('google drive')
                return True
        for rule in reobj.google_drive_content:
            if rule.search(self.email):
                self.auto_tag.add('google drive')
                return True
        return False

    def is_google_group(self):
        for rule in reobj.google_group_subject:
            if rule.search(self.subject):
                self.auto_tag.add('google group')
                return True
        for rule in reobj.google_group_content:
            if rule.search(self.contents):
                self.auto_tag.add('google group')
                return True

    def is_library(self):
        for rule in reobj.library_subject:
            if rule.search(self.subject):
                self.auto_tag.add('library related')
                return True
        for rule in reobj.library_email:
            if rule.search(self.email):
                self.auto_tag.add('library related')
                return True
        for rule in reobj.library_content:
            if rule.search(self.email):
                self.auto_tag.add('library related')
                return True
        return False

    def is_virus(self):
        for rule in reobj.virus_subject:
            if rule.search(self.subject):
                self.auto_tag.add('virus/malware')
                return True
        for rule in reobj.virus_email:
            if rule.search(self.email):
                self.auto_tag.add('virus/malware')
                return True
        for rule in reobj.virus_content:
            if rule.search(self.email):
                self.auto_tag.add('virus/malware')
                return True
        return False

    def is_password_reset(self):
        for rule in reobj.password_reset_subject:
            if rule.search(self.subject):
                self.auto_tag.add('password reset')
                return True
        for rule in reobj.password_reset_email:
            if rule.search(self.email):
                self.auto_tag.add('password reset')
                return True
        for rule in reobj.password_reset_content:
            if rule.search(self.email):
                self.auto_tag.add('password reset')
                return True
        return False

    def is_printing(self):
        for rule in reobj.printing_subject:
            if rule.search(self.subject):
                self.auto_tag.add('printers/copiers')
                return True
        for rule in reobj.printing_content:
            if rule.search(self.email):
                self.auto_tag.add('printers/copiers')
                return True
        return False

    def is_hardware(self):
        for rule in reobj.hardware_subject:
            if rule.search(self.subject):
                self.auto_tag.add('hardware')
                return True
        for rule in reobj.hardware_content:
            if rule.search(self.email):
                self.auto_tag.add('hardware')
                return True
        return False
    
    def is_microsoft(self):
        for rule in reobj.microsoft_subject:
            if rule.search(self.subject):
                self.auto_tag.add('microsoft')
                return True
        for rule in reobj.microsoft_email:
            if rule.search(self.email):
                self.auto_tag.add('microsoft')
                return True
        for rule in reobj.microsoft_content:
            if rule.search(self.email):
                self.auto_tag.add('microsoft')
                return True
        return False

    def is_network(self):
        for rule in reobj.network_subject:
            if rule.search(self.subject):
                self.auto_tag.add('network')
                return True
        for rule in reobj.network_content:
            if rule.search(self.email):
                self.auto_tag.add('network')
                return True
        return False

    def is_reed_account(self):
        for rule in reobj.account_subject:
            if rule.search(self.subject):
                self.auto_tag.add('reed accounts & access')
                return True
        for rule in reobj.account_content:
            if rule.search(self.email):
                self.auto_tag.add('reed accounts & access')
                return True
        for rule in reobj.account_email:
            if rule.search(self.email):
                self.auto_tag.add('reed accounts & access')
                return True
        return False

    def is_software(self):
        for rule in reobj.software_subject:
            if rule.search(self.subject):
                self.auto_tag.add('software')
                return True
        for rule in reobj.software_content:
            if rule.search(self.email):
                self.auto_tag.add('software')
                return True
        return False

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Log In.
        ops.login(page, 'zhuyifang', '***REMOVED***')
        
        ticket = Ticket(id='324298')
        ticket.get_info(page)
        ticket.parse()
        