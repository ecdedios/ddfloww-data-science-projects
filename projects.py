from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-science-projects/domestic-violence-1')
def show_domestic_violence_1():
    return render_template('/domestic-violence-2019/index.html')

@app.route('/data-science-projects/datathon-2019')
def show_datathon_2019():
    return render_template('/datathon-2019/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
