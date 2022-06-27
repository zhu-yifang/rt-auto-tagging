class Ticket:
    def __init__(self, id, subject, email, contents):
        self.id = id
        self.subject = subject
        self.email = email
        self.contents = contents
        self.type = self.get_type()
        self.tags = self.get_tags()
    
    def 