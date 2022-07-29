import auto_tag.regex_objects as reobj
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

    async def goto_ticket(self):
        await self.page.goto(
            f'https://help.reed.edu/Ticket/Display.html?id={self.id}')
        await self.page.wait_for_load_state(state='networkidle')

    # Get the email address of the requestor
    async def get_requestor_email(self):
        email_handle = await self.page.query_selector('.EmailAddress > .value')
        self.requestor_email = await email_handle.inner_text()
        return self.requestor_email

    # Get the title of the ticket
    async def get_subject(self):
        subject_handle = await self.page.query_selector('h1')
        self.subject = (await subject_handle.inner_text())[9:]
        return self.subject

    # Get the tags of the ticket
    async def get_tags(self):
        tag_handles = await self.page.query_selector('#CF-354-ShowRow > .value'
                                                     )
        if tag_handles:
            tags = (await tag_handles.inner_text()).split('\n')
        else:
            tags = []
        for tag in tags:
            self.tags.add(tag)
        return self.tags

    # Get all the messages and quotes of the ticket
    async def get_contents(self):
        message_handles = await self.page.query_selector_all('.messagebody')
        quote_handles = await self.page.query_selector_all(
            '.message-stanza.closed')
        for message_handle in message_handles:
            message = await message_handle.inner_text()
            # filter out the empty stirngs
            if message == '':
                continue
            # filter out the CUS auto-reply
            if reobj.auto_reply[0].search(message):
                continue
            self.contents += message + '\n'
        for quote_handle in quote_handles:
            quote = await quote_handle.inner_text()
            # filter out the empty stirngs
            if quote == '':
                continue
            # filter out the CUS auto-reply
            if reobj.auto_reply[0].search(quote):
                continue
            self.contents += quote + '\n'
        return self.contents

    async def get_receiver_email(self):
        handle = await self.page.query_selector(
            'td.message-header-key:text-is("To:") + td')
        if not handle:
            return self.receiver_email
        if not await handle.inner_text():
            return self.receiver_email
        self.receiver_email.add(
            reobj.email_re.search(await handle.inner_text())[0])
        return self.receiver_email

    # get the ticket's subject, requestor email, receiver email, contents, tags
    async def get_info(self):
        await self.goto_ticket()
        await self.get_subject()
        await self.get_requestor_email()
        await self.get_receiver_email()
        await self.get_contents()
        await self.get_tags()

    # decide which tag to choose
    async def parse(self):
        # 100%确定的标签
        # mass email
        if await self.is_mass_email():
            return self.auto_tags
        # no tag
        if await self.is_no_tag():
            return self.auto_tags
        # phish
        if await self.is_phish():
            return self.auto_tags
        # 不是100%确定的标签
        # software
        await self.is_software()
        # thesis
        await self.is_thesis()
        # two-factor
        await self.is_two_factor()
        # user/name change
        await self.is_name_change()
        # google drive
        await self.is_google_drive()
        # google group
        await self.is_google_group()
        # virus/malware
        await self.is_virus()
        # password reset
        await self.is_password_reset()
        # printing
        await self.is_printing()
        # hardware
        await self.is_hardware()
        # microsoft
        await self.is_microsoft()
        # network
        await self.is_network()
        # reed account
        await self.is_reed_account()
        # library
        await self.is_library()
        if 'thesis' and 'microsoft' in self.auto_tags:
            self.auto_tags.remove('microsoft')
        if len(self.auto_tags) >= 3:
            return 'Needs manual tag'
        return self.auto_tags

    async def close(self):
        await self.page.close()

    async def scan(self):
        await self.get_info()
        await self.parse()
        await self.close()
        return await self.check_match()

    async def check_match(self):
        if self.tags == self.auto_tags:
            return True
        else:
            return False

    async def is_mass_email(self):
        for rule in reobj.mass_email_subject:
            if rule.search(self.subject):
                self.auto_tags.add('mass email')
                return True
        return False

    async def is_thesis(self):
        for rule in reobj.thesis_subject:
            if rule.search(self.subject):
                self.auto_tags.add('thesis')
                return True
        for rule in reobj.thesis_content:
            if rule.search(self.contents):
                self.auto_tags.add('thesis')
                return True
        return False

    async def is_two_factor(self):
        for rule in reobj.two_factor_subject:
            if rule.search(self.subject):
                self.auto_tags.add('two-factor')
                return True
        for rule in reobj.two_factor_content:
            if rule.search(self.contents):
                self.auto_tags.add('two-factor')
                return True
        return False

    async def is_name_change(self):
        for rule in reobj.name_change_subject:
            if rule.search(self.subject):
                self.auto_tags.add('user/name change')
                return True
        for rule in reobj.name_change_content:
            if rule.search(self.contents):
                self.auto_tags.add('user/name change')
                return True
        return False

    async def is_no_tag(self):
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

    async def is_phish(self):
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

    async def is_google_drive(self):
        for rule in reobj.google_drive_subject:
            if rule.search(self.subject):
                self.auto_tags.add('google drive')
                return True
        for rule in reobj.google_drive_content:
            if rule.search(self.contents):
                self.auto_tags.add('google drive')
                return True
        return False

    async def is_google_group(self):
        for rule in reobj.google_group_subject:
            if rule.search(self.subject):
                self.auto_tags.add('google group')
                return True
        for rule in reobj.google_group_content:
            if rule.search(self.contents):
                self.auto_tags.add('google group')
                return True

    async def is_library(self):
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

    async def is_virus(self):
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

    async def is_password_reset(self):
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

    async def is_printing(self):
        for rule in reobj.printing_subject:
            if rule.search(self.subject):
                self.auto_tags.add('printers/copiers')
                return True
        for rule in reobj.printing_content:
            if rule.search(self.contents):
                self.auto_tags.add('printers/copiers')
                return True
        return False

    async def is_hardware(self):
        for rule in reobj.hardware_subject:
            if rule.search(self.subject):
                self.auto_tags.add('hardware')
                return True
        for rule in reobj.hardware_content:
            if rule.search(self.contents):
                self.auto_tags.add('hardware')
                return True
        return False

    async def is_microsoft(self):
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

    async def is_network(self):
        for rule in reobj.network_subject:
            if rule.search(self.subject):
                self.auto_tags.add('network')
                return True
        for rule in reobj.network_content:
            if rule.search(self.contents):
                self.auto_tags.add('network')
                return True
        return False

    async def is_reed_account(self):
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

    async def is_software(self):
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
    pass