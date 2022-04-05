from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App

from marketmarker import MarketMarker


class FarmersMapView(MapView):

    getting_markets_timer = None
    market_names = {*()}

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view

        try:
            self.getting_markets_timer.cancel()
        except Exception:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        """
        get_bbox() returns the co-ordinates of the current screen.
        Eg :
            (33.40676198714542, -84.94931640625, 34.091869576843884, -83.85068359375)
        :param args:
        :return:
        """
        # Get reference to the main app
        app = App.get_running_app()  # this is MainApp in main.py

        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        statement = f"SELECT * FROM markets WHERE x > {min_lon} AND x < {max_lon} AND y > {min_lat} AND y < {max_lat}"

        app.cursor.execute(statement)
        markets = app.cursor.fetchall()

        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        lat, lon = market[21], market[20]
        marker = MarketMarker(lat=lat, lon=lon, source="marker.png")
        marker.market_data = market

        self.add_widget(marker)  # this is inherited from MapView

        name = market[1]
        self.market_names.add(name)
