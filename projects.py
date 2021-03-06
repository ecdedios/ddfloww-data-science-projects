import domestic_violence_2019
import datathon_2019
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data-science-projects/domestic-violence-2019')
def show_domestic_violence_2019():
    return render_template('/domestic-violence-2019/index.html')

@app.route('/data-science-projects/datathon-2019')
def show_datathon_2019():
    return render_template('/datathon-2019/index.html')

@app.route('/data-science-projects/natural-language-processing-app')
def show_nlp_app():
    return render_template('/natural-language-processing-app/index.html')

@app.route('/data-science-projects/domestic-violence-2019/submit', methods=['GET', 'POST'])
def submit_domestic_violence_2019():
    error = None
    if request.method == 'POST':
        if request.form['q1'] == 'x':
            error = 'Missing answer.'
        else:
            feature1 = int(float(request.form['q1']))
            feature2 = int(float(request.form['q2']))
            feature3 = int(float(request.form['q3']))
            feature4 = int(float(request.form['q4']))
            feature5 = int(float(request.form['q5']))
            feature6 = int(float(request.form['q6']))
            feature7 = int(float(request.form['q7']))
            feature8 = int(float(request.form['q8']))
            feature9 = int(float(request.form['q9']))
            prediction = domestic_violence_2019.predictorizer(feature1,
                                                feature2,
                                                feature3,
                                                feature4,
                                                feature5,
                                                feature6,
                                                feature7,
                                                feature8,
                                                feature9)
            return render_template('/domestic-violence-2019/submit.html',
                                    prediction=prediction,
                                    feature1=feature1,
                                    feature2=feature2,
                                    feature3=feature3,
                                    feature4=feature4,
                                    feature5=feature5,
                                    feature6=feature6,
                                    feature7=feature7,
                                    feature8=feature8,
                                    feature9=feature9,)        
        return render_template('/domestic-violence-2019/index.html', error=error)

@app.route('/data-science-projects/datathon-2019/submit', methods=['GET', 'POST'])
def submit_datathon_2019():
    error = None
    if request.method == 'POST':
        if request.form['q1'] == 'x':
            error = 'Missing answer.'
        else:
            feature1 = int(float(request.form['q1']))
            feature2 = int(float(request.form['q2']))
            feature3 = int(float(request.form['q3']))
            feature4 = int(float(request.form['q4']))
            feature5 = int(float(request.form['q5']))
            feature6 = int(float(request.form['q6']))
            feature7 = int(float(request.form['q7']))
            feature8 = int(float(request.form['q8']))
            feature9 = int(float(request.form['q9']))
            feature10 = int(float(request.form['q10']))
            prediction = datathon_2019.predictorizer(feature1,
                                                feature2,
                                                feature3,
                                                feature4,
                                                feature5,
                                                feature6,
                                                feature7,
                                                feature8,
                                                feature9,
                                                feature10)
            return render_template('/datathon-2019/submit.html',
                                    prediction=prediction,
                                    feature1=feature1,
                                    feature2=feature2,
                                    feature3=feature3,
                                    feature4=feature4,
                                    feature5=feature5,
                                    feature6=feature6,
                                    feature7=feature7,
                                    feature8=feature8,
                                    feature9=feature9,
                                    feature10=feature10,)       
        return render_template('/datathon-2019/index.html', error=error)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
