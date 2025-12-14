import os.path

from settings import DEFAULT_TORRENT_FILE_PATH, GRID_DEFAULT_PARAMS
from torr_serve import TorrServe
from tkinter import (
    LabelFrame, Label, Button, filedialog as fd, Entry, StringVar, PhotoImage
)


class AddTorrentWidget:
    def __init__(self, master, torr: TorrServe, row: int, column: int):
        self.master = master
        self.torr_serve = torr
        self.file_path: str | None = None
        self.default_path: str | None = None
        self.display_name: StringVar = StringVar()

        self.set_default_path()

        # main frame
        self.lframe = LabelFrame(
            self.master,
            text='Добавить торрент  ',
        )
        self.lframe.grid(row=row, column=column, **GRID_DEFAULT_PARAMS)

        # select .torrent button
        self.open_img = PhotoImage(file='./ui/images/folder.png')
        self.select = Button(
            self.lframe,
            text='Выберите .torrent',
            command=self.select_file,
            image=self.open_img,
            compound='left',
        )
        self.select.grid(row=0, column=0, **GRID_DEFAULT_PARAMS)

        # show selected filename frame
        self.selected_lframe = LabelFrame(
            self.lframe,
            text='Выбранный торрент:  ',
        )
        self.selected_lframe.grid(row=1, column=0, **GRID_DEFAULT_PARAMS)

        self.show_selected_torrent = Label(
            self.selected_lframe,
            text='-',
        )
        self.show_selected_torrent.grid(row=0, column=0)

        # set name frame
        self.set_name_lframe = LabelFrame(
            self.lframe,
            text='Задайте имя:  ',
        )
        self.set_name_lframe.grid(row=2, column=0, **GRID_DEFAULT_PARAMS)
        self.set_name_w = Entry(
            self.set_name_lframe,
            textvariable=self.display_name,
        )
        self.set_name_w.grid(row=0, column=0, **GRID_DEFAULT_PARAMS)

        # send button
        # The image object can then be used wherever an image option
        # is supported by some widget (e.g. labels, buttons, menus).
        # In these cases, Tk will not keep a reference to the image.
        # When the last Python reference to the image object is deleted,
        # the image data is deleted as well,
        # and Tk will display an empty box wherever the image was used.
        self.img_send = PhotoImage(file='./ui/images/send2_32x32.png', master=self.lframe)
        self.add_torrent_button = Button(
            self.lframe,
            text='Добавить на сервер',
            command=self.add_torrent,
            image=self.img_send,
            compound='left',
        )

        self.add_torrent_button.grid(row=3, column=0, **GRID_DEFAULT_PARAMS)

        # status frame
        self.status_lframe = LabelFrame(
            self.lframe,
            text='Статус:  '
        )
        self.status_lframe.grid(row=4, column=0, **GRID_DEFAULT_PARAMS)
        self.status_w = Label(
            self.status_lframe,
            text=''
        )
        self.status_w.grid(row=0, column=0)

    def set_default_path(self):
        self.default_path = DEFAULT_TORRENT_FILE_PATH

    def get_choosen_filename(self) -> str:
        if not self.file_path:
            return ''
        file_name = os.path.basename(self.file_path)
        if len(file_name) > 20:
            return file_name[:20] + '...'
        else:
            return file_name

    def select_file(self):
        filetypes = (
            ('torrent files', '*.torrent'),
        )
        self.file_path = fd.askopenfilename(
            title='Choose .torrent',
            initialdir=self.default_path,
            filetypes=filetypes)

        self.show_selected_torrent.config(text=self.get_choosen_filename())

    def add_torrent(self):
        warning_color = 'orange'
        if not self.file_path:
            self.status_w.config(text='Выберите .torrent-файл', background=warning_color)
            return
        if not self.set_name_w.get():
            self.status_w.config(text='Задайте отображемое имя', background=warning_color)
            return
        res = self.torr_serve.add_torrent(self.file_path, self.set_name_w.get())
        self.status_w.config(text=res, background='green' if res == 'OK' else warning_color)
