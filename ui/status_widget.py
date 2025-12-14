from tkinter import LabelFrame, Label, Button, W
from torr_serve import TorrServe
from settings import GRID_DEFAULT_PARAMS

class StatusWidget:
    def __init__(self, master, torr: TorrServe, row: int, column: int):
        self.master = master
        self.torr_serve = torr

        self.lframe = LabelFrame(
            self.master,
            text='Соединение:',
            width=40,
            height=5,
        )
        self.lframe.grid(row=row, column=column)

        self.status_header = Label(
            self.lframe,
            text='Статус:',
        )
        # self.status_header.grid(row=0, column=0, sticky='e')

        self.status_result = Label(
            self.lframe,
            text='-',
            background='yellow'
        )
        self.status_result.grid(row=0, column=1, **GRID_DEFAULT_PARAMS)

        self.but = Button(
            self.lframe,
            text='Test conn',
            command=self.test_conn
        )
        self.but.grid(row=1, column=0, **GRID_DEFAULT_PARAMS)

    def test_conn(self):
        cases = {
            True: {'text': 'OK', 'background': 'green'},
            False: {'text': 'not OK', 'background': 'orange'}
        }
        is_conn_ok = self.torr_serve.check_connection()
        self.status_result.config(**cases[is_conn_ok])