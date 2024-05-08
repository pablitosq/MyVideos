from flask import Flask, request, render_template, jsonify, redirect, url_for
from os.path import basename
import requests
import os
import ntpath
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app/index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    
    if request.method == 'POST':
        
        if request.form['opcion'] == "pelicula" or request.form['opcion'] == "serie" and request.form['search'] == "":
            
            message = "No has introducido ningún dato en la búsqueda"
            
        if request.form['opcion'] == "pelicula" and request.form['search'] != "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/movie?query={_search}&include_adult=false&language=en-US&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response = requests.get(url, headers=headers)
            response = response.json()
            
            return render_template('app/search.html', response=response)
        
        if request.form['opcion'] == "serie" and request.form['search'] == "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/tv?query={_search}&include_adult=false&language=en-US&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }

            response = requests.get(url, headers=headers)

            response = response.json()
            
            return render_template('movie/add-movie.html', response=response)
            
    return render_template('app/index.html', message=message,)


@app.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        
        if request.form['search'] == "":
            
            message = "No has introducido ningún dato en la búsqueda"
            return render_template('movies/add-movie.html', message=message)
            
        if request.form['search'] != "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/movie?query={_search}&include_adult=false&language=es-ES&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response = requests.get(url, headers=headers)
            response = response.json()
            
            print(response)
            
            return render_template('movies/add-movie.html', _search=_search ,response=response)
            
    return render_template('movies/add-movie.html')

@app.route('/add-movie-select', methods=['GET', 'POST'])
def add_movie_select():
    if request.method == 'POST':
        
        if request.form['id']:
            
            id = request.form['id']
            #print(movie_id)
            
            url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response_movie = requests.get(url, headers=headers)
            response_movie = response_movie.json()
            
            print(response_movie)

            for genres in response_movie['genres']:
                print(genres['name'])
            
            #Créditos
                
            url2 = f"https://api.themoviedb.org/3/movie/{id}/credits?language=es-ES"

            response_movie_credits = requests.get(url2, headers=headers)

            response_movie_credits = response_movie_credits.json()
            print("\n\n")
            
#                print("Nombre:" , credit['name'])
#            for credit in response_movie_credits['cast']:
#                print("Profesión:", credit['character'])
#                print("Imágen: ", credit['profile_path'])
#                print("\n") 

            
            return render_template('movies/add-movie.html', response_movie=response_movie, response_movie_credits=response_movie_credits, id=id)

    return render_template('movies/add-movie.html')            


@app.route('/add-movie-rec/', methods=['GET', 'POST'])
def add_movie_rec():
    
    if request.method == 'POST':
        if request.form['movie_id']:
            id = request.form['movie_id']

            url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response_movie = requests.get(url, headers=headers)
            response_movie = response_movie.json()
                        
        
    return render_template('movies/add-movie-rec.html', id=id, response_movie=response_movie)

@app.route('/add-movie-record', methods=['GET', 'POST'])
def add_movie_record():
    
    if request.method == 'POST':

        id = request.form['movie_id']
        url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
        
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
        }
            
        response_movie = requests.get(url, headers=headers)
        response_movie = response_movie.json()
             
                        
        file_video = request.files['file']
        filename = secure_filename(file_video.filename)

        extension = os.path.splitext(filename)[1]
        nuevoNombre = response_movie['title'] + extension
        
        
        
        print(nuevoNombre)
        
        
    return redirect("/") 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>No se encuentra esta página</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)

