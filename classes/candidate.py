class Candidate(object):
    def __init__(self, name):
        self.name = name
        self.email = str()
        self.phone = int()
        self.website = str()
        self.github = str()
        self.linkedin = str()

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

