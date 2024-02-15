from flask import Flask, render_template
import urllib.request, json
import ssl

app = Flask(__name__)


@app.route('/characters')
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()  
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict['results'])

@app.route('/character/<id>')
def get_character(id):
    url = "https://rickandmortyapi.com/api/character/"+id #+id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("character_id.html", character=dict)

@app.route('/locations')
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location/"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("locations.html", locations=dict['results'])

@app.route('/location/<id>')
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/"+id #+id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("location_id.html", location=dict)

if __name__ == '__main__':
    app.run(debug=True)
