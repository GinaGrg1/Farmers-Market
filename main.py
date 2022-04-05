import sqlite3

from kivymd.app import MDApp

from farmersmapview import FarmersMapView
from searchpopupmenu import SearchPopupMenu


class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        self.search_menu = SearchPopupMenu()


MainApp().run()
