

from flask import Flask, request, jsonify, render_template
#import requests

app = Flask(__name__)

API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'No location provided'}), 400

    # Fetch weather data from OpenWeatherMap API
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
