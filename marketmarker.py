from kivy.garden.mapview import MapMarkerPopup

from locationpopupmenu import LocationPopupMenu


class MarketMarker(MapMarkerPopup):
    market_data = []

    def on_release(self):
        # Open up the LocationPopupMenu when clicked on the marker on the map
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()