from tracemalloc import start
from playwright.sync_api import sync_playwright
import regex_objects as reobj
import rt_operations as ops
import time

'''
模块的说明文档
'''

class Ticket:
    def __init__(self, id, page):
        self.id = id
        self.subject = ''
        self.requestor_email = ''
        self.receiver_email = set()
        self.contents = ''
        self.page = page
        self.tags = set()
        self.auto_tags = set()
    
    def __str__(self):
        return f'{self.id}: {self.tags}, {self.auto_tags}'

    def goto_ticket(self):
        self.page.goto(f'https://help.reed.edu/Ticket/Display.html?id={self.id}')
        self.page.wait_for_load_state(state='networkidle')

    # Get the email address of the requestor
    def get_requestor_email(self):
        email_handle = self.page.query_selector('.EmailAddress > .value')
        self.requestor_email = email_handle.inner_text()
        return self.requestor_email
    
    # Get the title of the ticket
    def get_subject(self):      
        subject_handle = self.page.query_selector('h1')
        self.subject = subject_handle.inner_text()[9:]
        return self.subject
    
    # Get the tags of the ticket
    def get_tags(self):
        tag_handles = self.page.query_selector('#CF-354-ShowRow > .value')
        if tag_handles:
            tags = tag_handles.inner_text().split('\n')
        else:
            tags = []
        for tag in tags:
            self.tags.add(tag)
        return self.tags
    
    # Get all the messages and quotes of the ticket
    def get_contents(self):
        message_handles = self.page.query_selector_all('.messagebody')
        quote_handles = self.page.query_selector_all('.message-stanza.closed')
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
        return self.contents
    
    def get_receiver_email(self):
        handle = self.page.query_selector('td.message-header-key:text-is("To:") + td')
        if not handle:
            return self.receiver_email
        if not handle.inner_text():
            return self.receiver_email
        self.receiver_email.add(reobj.email_re.search(handle.inner_text())[0])
        return self.receiver_email

    # get the ticket's subject, requestor email, receiver email, contents, tags
    def get_info(self):
        self.get_subject()
        self.get_requestor_email()
        self.get_receiver_email()
        self.get_contents()
        self.get_tags()
    
    def check_match(self):
        if self.tags == self.auto_tags:
            return True
        else:
            return False

    # decide which tag to choose
    def parse(self):
        # 100%确定的标签
        # mass email
        if self.is_mass_email():
            return self.auto_tags
        # no tag
        if self.is_no_tag():
            return self.auto_tags
        # phish
        if self.is_phish():
            return self.auto_tags
        # 不是100%确定的标签
        # software
        self.is_software()
        # thesis
        self.is_thesis()
        # two-factor
        self.is_two_factor()
        # user/name change
        self.is_name_change()
        # google drive
        self.is_google_drive()
        # google group
        self.is_google_group()
        # virus/malware
        self.is_virus()
        # password reset
        self.is_password_reset()
        # printing
        self.is_printing()
        # hardware
        self.is_hardware()
        # microsoft
        self.is_microsoft()
        # network
        self.is_network()
        # reed account
        self.is_reed_account()
        # library
        self.is_library()
        if 'thesis' and 'microsoft' in self.auto_tags:
            self.auto_tags.remove('microsoft')
        if len(self.auto_tags) >= 3:
            return 'Needs manual tag'
        return self.auto_tags

    def is_mass_email(self):
        for rule in reobj.mass_email_subject:
            if rule.search(self.subject):
                self.auto_tags.add('mass email')
                return True
        return False

    
    def is_thesis(self):
        for rule in reobj.thesis_subject:
            if rule.search(self.subject):
                self.auto_tags.add('thesis')
                return True
        for rule in reobj.thesis_content:
            if rule.search(self.contents):
                self.auto_tags.add('thesis')
                return True
        return False

    def is_two_factor(self):
        for rule in reobj.two_factor_subject:
            if rule.search(self.subject):
                self.auto_tags.add('two-factor')
                return True
        for rule in reobj.two_factor_content:
            if rule.search(self.contents):
                self.auto_tags.add('two-factor')
                return True
        return False

    def is_name_change(self):
        for rule in reobj.name_change_subject:
            if rule.search(self.subject):
                self.auto_tags.add('user/name change')
                return True
        for rule in reobj.name_change_content:
            if rule.search(self.contents):
                self.auto_tags.add('user/name change')
                return True
        return False

    def is_no_tag(self):
        # notification emails
        for rule in reobj.no_tag_subject:
            if rule.search(self.subject):
                # self.auto_tags.add('no tag')
                return True
        for rule in reobj.no_tag_email:
            if rule.search(self.requestor_email):
                # self.auto_tags.add('no tag')
                return True
         # mass email release
        if self.receiver_email:
            email = self.receiver_email.pop()
            for rule in reobj.mass_email_release:
                if rule.search(email):
                    return True
        return False

    def is_phish(self):
        for rule in reobj.phish_subject:
            if rule.search(self.subject):
                self.auto_tags.add('phish report/fwd')
                return True
        for rule in reobj.phish_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('phish report/fwd')
                return True
        for rule in reobj.phish_content:
            if rule.search(self.contents):
                self.auto_tags.add('phish report/fwd')
                return True
        return False

    def is_google_drive(self):
        for rule in reobj.google_drive_subject:
            if rule.search(self.subject):
                self.auto_tags.add('google drive')
                return True
        for rule in reobj.google_drive_content:
            if rule.search(self.contents):
                self.auto_tags.add('google drive')
                return True
        return False

    def is_google_group(self):
        for rule in reobj.google_group_subject:
            if rule.search(self.subject):
                self.auto_tags.add('google group')
                return True
        for rule in reobj.google_group_content:
            if rule.search(self.contents):
                self.auto_tags.add('google group')
                return True

    def is_library(self):
        for rule in reobj.library_subject:
            if rule.search(self.subject):
                self.auto_tags.add('library related')
                return True
        for rule in reobj.library_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('library related')
                return True
        for rule in reobj.library_content:
            if rule.search(self.contents):
                self.auto_tags.add('library related')
                return True
        return False

    def is_virus(self):
        for rule in reobj.virus_subject:
            if rule.search(self.subject):
                self.auto_tags.add('virus/malware')
                return True
        for rule in reobj.virus_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('virus/malware')
                return True
        for rule in reobj.virus_content:
            if rule.search(self.contents):
                self.auto_tags.add('virus/malware')
                return True
        return False

    def is_password_reset(self):
        for rule in reobj.password_reset_subject:
            if rule.search(self.subject):
                self.auto_tags.add('password reset')
                return True
        for rule in reobj.password_reset_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('password reset')
                return True
        for rule in reobj.password_reset_content:
            if rule.search(self.contents):
                self.auto_tags.add('password reset')
                return True
        return False

    def is_printing(self):
        for rule in reobj.printing_subject:
            if rule.search(self.subject):
                self.auto_tags.add('printers/copiers')
                return True
        for rule in reobj.printing_content:
            if rule.search(self.contents):
                self.auto_tags.add('printers/copiers')
                return True
        return False

    def is_hardware(self):
        for rule in reobj.hardware_subject:
            if rule.search(self.subject):
                self.auto_tags.add('hardware')
                return True
        for rule in reobj.hardware_content:
            if rule.search(self.contents):
                self.auto_tags.add('hardware')
                return True
        return False
    
    def is_microsoft(self):
        for rule in reobj.microsoft_subject:
            if rule.search(self.subject):
                self.auto_tags.add('microsoft')
                return True
        for rule in reobj.microsoft_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('microsoft')
                return True
        for rule in reobj.microsoft_content:
            if rule.search(self.contents):
                self.auto_tags.add('microsoft')
                return True
        return False

    def is_network(self):
        for rule in reobj.network_subject:
            if rule.search(self.subject):
                self.auto_tags.add('network')
                return True
        for rule in reobj.network_content:
            if rule.search(self.contents):
                self.auto_tags.add('network')
                return True
        return False

    def is_reed_account(self):
        for rule in reobj.account_subject:
            if rule.search(self.subject):
                self.auto_tags.add('reed accounts & access')
                return True
        for rule in reobj.account_email:
            if rule.search(self.requestor_email):
                self.auto_tags.add('reed accounts & access')
                return True
        for rule in reobj.account_content:
            if rule.search(self.contents):
                self.auto_tags.add('reed accounts & access')
                return True
        return False

    def is_software(self):
        for rule in reobj.software_subject:
            if rule.search(self.subject):
                self.auto_tags.add('software')
                return True
        for rule in reobj.software_content:
            if rule.search(self.contents):
                self.auto_tags.add('software')
                return True
        return False

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Log In.
        ops.login(page, 'zhuyifang', '***REMOVED***')

        start_time = time.time()
        
        ticket = Ticket(336618, page)
        ticket.goto_ticket()
        ticket.get_info()
        ticket.parse()
        print(ticket)
        
        
        
        
        
        
        
        # ids = ops.get_tickets(page)
        # wrong_count = 0
        # manual_count = 0
        # for id in ids:
        #     ticket = Ticket(id, page)
        #     ticket.goto_ticket()
        #     ticket.get_info()
        #     if ticket.parse() == 'Needs manual tag':
        #         manual_count += 1
        #         print(f'{ticket.id} needs manual tag, {ticket.tags}, {ticket.auto_tags}')
        #     elif not ticket.check_match():
        #         wrong_count += 1
        #         print(ticket)
        # end_time = time.time()
        # # percentage of wrong tags
        # print(f'{wrong_count / len(ids) * 100}% of tickets have wrong tags')
        # # percentage of manual tags
        # print(f'{manual_count / len(ids) * 100}% of tickets need manual tag')
        # print(f'{end_time - start_time} seconds')
        