from tkinter import Menu
from torr_serve import TorrServe
from tkinter.messagebox import showinfo
from settings import DEFAULT_TORRENT_FILE_PATH

class MenuBar:
    def __init__(self, master, torr: TorrServe):
        self.master = master
        self.torr = torr
        self.menu_bar = Menu(self.master)
        self.master['menu'] = self.menu_bar

        self.menu_settings = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_settings, label='Settings')

        # self.submenu_settings = Menu(self.menu_settings)
        # self.menu_settings.add_cascade(menu=self.submenu_settings, label='ShowURL')

        self.menu_settings.add_command(label='Show URL', command=self.set_ip_address)
        self.menu_settings.add_command(label='Show default folder', command=self.show_default_folder)

    def set_ip_address(self):
        showinfo('TorrServe URL', self.torr.get_base_url())

    def set_port(self):
        print('set port')

    def show_default_folder(self):
        showinfo('Default .torrent path', DEFAULT_TORRENT_FILE_PATH)