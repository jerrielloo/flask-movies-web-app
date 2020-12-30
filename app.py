from flask import Flask, render_template, redirect, url_for, request # maybe use *
import requests

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def show_landing_page():
    try:
        return render_template('landing-page.html', name= "Jerriel")
    except:
        return 'An error has occurred'

@app.route("/error")
def show_error_page():
    return render_template('error404.html')


@app.route('/watch/<video_id>')
def watch_video(video_id):
    return "Video ID: " + video_id

@app.route("/search", methods=['POST'])
def form_submit():
    user_query = request.form['search_query'] # matches name attribute of query string input (HTML)
    redirect_url = url_for('.search_imdb', query_string=user_query)  # match search_imdb function name (Python flask)
    return redirect(redirect_url)


@app.route("/search/<query_string>", methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": query_string}
    headers = {
        'x-rapidapi-key': "ca5e3212ccmsh565637e2c968ee0p113ca3jsn6b3dfcfaad56",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data=data)
    except:
        return render_template("error404.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
