import forecastio

# $ export FORECAST_TOKEN='xxxxxxxxxxx'
# FORECAST_TOKEN = os.environ.get('FORECAST_TOKEN')

FORECAST_TOKEN = "13519abeefd13d8b694f69aeda9ee2db"

def forecast(lat = 37.5124413, lng = 126.9540519):
    forecast = forecastio.load_forecast(FORECAST_TOKEN, lat, lng)
    byHour = forecast.hourly()
    return byHour.summary
