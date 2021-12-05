class JobBoard(object):
    available_job_boards = ['otta']

    def __init__(self, name):
        self.name = name

    def set_job_board(self, name):
        if name in self.available_job_boards:
            self.name = name




