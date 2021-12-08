from classes.application import Application


class JobBoard(Application):
    available_job_boards = ['otta']

    def __init__(self, name, job_board_name):
        super().__init__(job_board_name)
        self.name = name

    def set_job_board(self, name):
        if name in self.available_job_boards:
            self.name = name

    def fill_greenhouse_board(self):
        return
