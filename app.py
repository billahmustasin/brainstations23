from flask import Flask, jsonify
import platform
import datetime
import requests

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@app.route('/api/hello', methods=['GET'])
def hello():
    hostname = platform.node()

    current_datetime = datetime.datetime.now().strftime('%y%m%d%H%M')

    version = "1.0"

    weather_data = get_weather_data('Dhaka')

    response = {
        'hostname': hostname,
        'datetime': current_datetime,
        'version': version,
        'weather': {
            'dhaka': {
                'temperature': weather_data['main']['temp'],
                'temp_unit': 'C'
            }
        }
    }

    return jsonify(response)

def get_weather_data(city):
    api_key = 'fd0dd7a2a173cdace121681a058e031f'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
