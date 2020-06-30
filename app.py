# This application is using color from https://colorhunt.co/

import requests
from flask import Flask, render_template,request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        error = None
        if request.method == 'POST':
            text = request.form['city']
            city_name = text.upper()
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8f5ca370c7041d066e0026e9af47526f'
            response = requests.get(url.format(city_name)).json()
            temperature_in_degree = "{:10.2f}".format(((response['main']['temp']) - 273.15))
            weather_of_city = {
                'city' : city_name,
                'temperature' : temperature_in_degree,
                'description' : response['weather'][0]['description'],
                'icon' : response['weather'][0]['icon'],
            }
            print(weather_of_city)
            return render_template('index.html', weather = weather_of_city, error=error)
    except:
            return render_template('404.html')
        
    else: 
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8f5ca370c7041d066e0026e9af47526f'
        city_name = 'Lucknow'
        response = requests.get(url.format(city_name)).json()
        temperature_in_degree = "{:10.2f}".format(((response['main']['temp']) - 273.15))
        weather_of_city = {
            'city' : city_name,
            'temperature' : temperature_in_degree,
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }
        print(weather_of_city)
        return render_template('index.html', weather = weather_of_city, error=error)


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)