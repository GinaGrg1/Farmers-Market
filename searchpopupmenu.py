from urllib import parse

from kivymd.uix.dialog import MDInputDialog
from kivy.network.urlrequest import UrlRequest
from kivy.app import App


class SearchPopupMenu(MDInputDialog):
    title = "Search by Address"
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.5, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lan_lon(address)

    def geocode_get_lan_lon(self, address):

        email = 'gina524286@gmail.com'
        url = f'https://nominatim.openstreetmap.org/search/{parse.quote(address)}?format=json&email={email}'
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    @staticmethod
    def success(urlrequest, result):
        """
        urlrequest :  <UrlRequest(Thread-1, started daemon 123145640013824)>
        result : [{'place_id': 283961542, 'licence': 'Data © OpenStreetMap contributors,
                    ODbL 1.0. https://osm.org/copyright', 'osm_type': 'relation', 'osm_id': 119557,
                    'boundingbox': ['33.647808', '33.886823', '-84.551068', '-84.28956'], 'lat': '33.7489924',
                    'lon': '-84.3902644', 'display_name': 'Atlanta, Fulton County, Georgia, United States',
                    'class': 'boundary', 'type': 'administrative', 'importance': 0.8908028207926617,
                    'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png'},
                    ]

        :param urlrequest:
        :param result:
        :return:
        """
        print(f"Success : {result}")
        try:
            result = result[0]
            latitude = float(result.get('lat'))
            longitude = float(result.get('lon'))

            app = App.get_running_app()
            mapview = app.root.ids.mapview  # root refers to BoxLayout in main.kv
            mapview.center_on(latitude, longitude)

        except IndexError:
            pass

    @staticmethod
    def failure(urlrequest, result):
        print(f"Failed : {result}")

    @staticmethod
    def error(urlrequest, result):
        print(f"Errored : {result}")
