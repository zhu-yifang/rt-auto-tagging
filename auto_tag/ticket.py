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
        self.tags = {'mass email': False,
                     'thesis': False,
                     'two-factor': False,
                     'user/name change': False,
                     'no tag': False,
                     'phish report/fwd': False,
                     'google drive': False,
                     'google group': False,
                     'library related': False,
                     'virus/malware': False,
                     'password reset': False,
                     'printers/copiers': False,
                     'hardware': False,
                     'microsoft': False,
                     'network': False,
                     'reed accounts & access': False,
                     'software': False}
    
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
            self.tags[tag_handle.inner_text()] = True

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
    
    # decide which tag to choose
    def parse(self):
        pass
        # mass email
        if self.is_mass_email():
            return
        # thesis format
        elif self.is_microsoft():
            if self.is_thesis():
                return
            elif self.is_password_reset():
                return
        # two factor
        elif self.is_two_factor():
            return
        # name change
        elif self.is_name_change():
            return
        # no tag
        elif self.is_no_tag():
            return
        # phish
        elif self.is_phish():
            return
        # google drive
        elif self.is_google_drive():
            return
        # google group
        elif self.is_google_group():
            return
        # library
        elif self.is_library():
            return
        # virus
        elif self.is_virus():
            return
        # password reset
        elif self.is_password_reset():
            return
        # printing
        elif self.is_printing():
            return
        # hardware
        elif self.is_hardware():
            return
        # microsoft
        elif self.is_microsoft():
            return
        # network
        elif self.is_network():
            return
        # reed account
        elif self.is_reed_account():
            return
        # software
        elif self.is_software():
            return
        # else
        else:
            print(f'{self.id} needs to be tagged manually')
            
    def is_mass_email(self):
        for rule in reobj.mass_email_subject:
            if rule.search(self.subject):
                self.tag['mass email'] = True
                return True

    def is_thesis(self):
        for rule in reobj.thesis_subject:
            if rule.search(self.subject):
                self.tag['thesis'] = True
                return True
        for rule in reobj.thesis_content:
            if rule.search(self.email):
                self.tag['thesis'] = True
                return True
    
    def is_two_factor(self):
        for rule in reobj.two_factor_subject:
            if rule.search(self.subject):
                self.tag['two-factor'] = True
                return True
        for rule in reobj.two_factor_content:
            if rule.search(self.email):
                self.tag['two-factor'] = True
                return True

    def is_name_change(self):
        for rule in reobj.name_change_subject:
            if rule.search(self.subject):
                self.tag['name change'] = True
                return True
        for rule in reobj.name_change_content:
            if rule.search(self.email):
                self.tag['name_change'] = True
                return True

    def is_no_tag(self):
        for rule in reobj.no_tag_subject:
            if rule.search(self.subject):
                self.tag['no_tag'] = True
                return True
        for rule in reobj.no_tag_email:
            if rule.search(self.email):
                self.tag['no_tag'] = True
                return True
    
    def is_phish(self):
        for rule in reobj.phish_subject:
            if rule.search(self.subject):
                self.tag['phish'] = True
                return True
        for rule in reobj.phish_email:
            if rule.search(self.email):
                self.tag['phish'] = True
                return True
        for rule in reobj.phish_content:
            if rule.search(self.email):
                self.tag['phish'] = True
                return True


    def is_google_drive(self):
        for rule in reobj.google_drive_subject:
            if rule.search(self.subject):
                self.tag['google_drive'] = True
                return True
        for rule in reobj.google_drive_content:
            if rule.search(self.email):
                self.tag['google_drive'] = True
                return True
        
    def is_google_group(self):
        for rule in reobj.google_group_subject:
            if rule.search(self.subject):
                self.tag['google_group'] = True
                return True
        for rule in reobj.google_group_content:
            if rule.search(self.email):
                self.tag['google_group'] = True
                return True

    def is_library(self):
        for rule in reobj.library_subject:
            if rule.search(self.subject):
                self.tag['library'] = True
                return True
        for rule in reobj.library_email:
            if rule.search(self.email):
                self.tag['library'] = True
                return True
        for rule in reobj.library_content:
            if rule.search(self.email):
                self.tag['library'] = True
                return True

    def is_virus(self):
        for rule in reobj.virus_subject:
            if rule.search(self.subject):
                self.tag['virus'] = True
                return True
        for rule in reobj.virus_email:
            if rule.search(self.email):
                self.tag['virus'] = True
                return True
        for rule in reobj.virus_content:
            if rule.search(self.email):
                self.tag['virus'] = True
                return True

    def is_password_reset(self):
        for rule in reobj.password_reset_subject:
            if rule.search(self.subject):
                self.tag['password_reset'] = True
                return True
        for rule in reobj.password_reset_email:
            if rule.search(self.email):
                self.tag['password_reset'] = True
                return True
        for rule in reobj.password_reset_content:
            if rule.search(self.email):
                self.tag['password_reset'] = True
                return True

    def is_printing(self):
        for rule in reobj.printing_subject:
            if rule.search(self.subject):
                self.tag['printing'] = True
                return True
        for rule in reobj.printing_content:
            if rule.search(self.email):
                self.tag['printing'] = True
                return True
 
    def is_hardware(self):
        for rule in reobj.hardware_subject:
            if rule.search(self.subject):
                self.tag['hardware'] = True
                return True
        for rule in reobj.hardware_content:
            if rule.search(self.email):
                self.tag['hardware'] = True
                return True

    def is_microsoft(self):
        for rule in reobj.microsoft_subject:
            if rule.search(self.subject):
                self.tag['microsoft'] = True
                return True
        for rule in reobj.microsoft_email:
            if rule.search(self.email):
                self.tag['microsoft'] = True
                return True
        for rule in reobj.microsoft_content:
            if rule.search(self.email):
                self.tag['microsoft'] = True
                return True

    def is_network(self):
        for rule in reobj.network_subject:
            if rule.search(self.subject):
                self.tag['network'] = True
                return True
        for rule in reobj.network_content:
            if rule.search(self.email):
                self.tag['network'] = True
                return True

    def is_reed_account(self):
        for rule in reobj.account_subject:
            if rule.search(self.subject):
                self.tag['reed_account'] = True
                return True
        for rule in reobj.account_content:
            if rule.search(self.email):
                self.tag['reed_account'] = True
                return True
        for rule in reobj.account_email:
            if rule.search(self.email):
                self.tag['reed_account'] = True
                return True
    def is_software(self):
        for rule in reobj.software_subject:
            if rule.search(self.subject):
                self.tag['software'] = True
                return True
        for rule in reobj.software_content:
            if rule.search(self.email):
                self.tag['software'] = True
                return True
    
if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Log In.
        ops.login(page, 'zhuyifang', '***REMOVED***')
        ticket = Ticket(id='336601')
        ticket.get_info(page)
        for tag in ticket.tags:
            if ticket.tags[tag]:
                print(tag)
        