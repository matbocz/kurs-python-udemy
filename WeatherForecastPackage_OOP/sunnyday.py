import requests


class Weather:
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:
    # Get your own apikey from: openweathermap.org

    # Create a weather object using a city name:
    >>> weather = Weather(apikey="apikey", city="Warsaw")

    # Create a weather object using a lat and lon coordinates:
    >>> weather = Weather(apikey="apikey", lat=5.1, lon=10.9)

    # Get complete weather data for the next 12 hours:
    >>> weather.next_12h()

    # Get simplified weather data for the next 12 hours:
    >>> weather.next_12h_simplified()
    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            req = requests.get(url)
            self.data = req.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            req = requests.get(url)
            self.data = req.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
        Returns 3-hour data for the next 12 hours as a dict.
        """

        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        Returns date, temperature and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples.
        """

        simple_data = []
        for item in self.data['list'][:4]:
            simple_data.append((item['dt_txt'], item['main']['temp'], item['weather'][0]['description']))

        return simple_data
