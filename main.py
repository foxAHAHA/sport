from flask import Flask, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/importance-of-sport')
def importance_of_sport():
    return render_template('importance_of_sport.html')


@app.route('/all-sports')
def all_sports():
    return render_template('sport_training_methods.html')


@app.route('/health-and-sport')
def health_and_sport():
    return render_template('health_and_sport.html')


if __name__ == '__main__':
    app.run(debug=True)
