from tkinter import Tk

from ui.add_torrent_widget import AddTorrentWidget
from ui.menu_bar import MenuBar
from torr_serve import TorrServe


class UI:
    def __init__(self, host: str, port: str = '8090'):
        self.master = None
        self.torr_serve = None
        self.menu_bar = None
        self.add_torrent_widget = None

        self.init_torr_serve(host, port)
        self.init_main_frame()

    def init_main_frame(self):
        self.master = Tk()
        self.master.title('TorrServeAdderApp')
        self.master.geometry('300x350')
        self.master.option_add('*tearOff', False)

        self.menu_bar = MenuBar(self.master, self.torr_serve)

        self.add_torrent_widget = AddTorrentWidget(
            self.master,
            self.torr_serve,
            row=1, column=0,
        )

        self.master.mainloop()

    def init_torr_serve(self, host: str, port: str = '8090'):
        self.torr_serve = TorrServe(host, port)
