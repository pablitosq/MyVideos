from flask import Flask, request, render_template, jsonify, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    
    if request.method == 'POST':
             
        if request.form['opcion'] == "pelicula":
                
            if request.form['search'] == "":
                message = "No has introducido ningún dato en la búsqueda"
                return render_template('app/index.html', message=message)
                
            else:    
                _search = request.form['search']    
                
                url = f"https://api.themoviedb.org/3/search/movie?query={_search}&include_adult=false&language=en-US&page=1"

                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
                }

                response = requests.get(url, headers=headers)
                
                response = response.json()
                
            return render_template('app/search.html', response=response)
        
        elif request.form['opcion'] == "serie":
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/tv?query={_search}&include_adult=false&language=en-US&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }

            response = requests.get(url, headers=headers)

            response = response.json()
            
            return render_template('app/search.html', response=response)
            
        else:
            message = "Por favor ingrese el título de una película"
            return render_template('app/index.html', message=message)    
    else:
        message = "Por favor ingrese el título de una película"
        return render_template('app/index.html', message=message)



if __name__ == '__main__':
    app.run(debug=True)
