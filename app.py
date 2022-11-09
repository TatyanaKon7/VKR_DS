
import flask
from flask import render_template
import pickle
import sklearn
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def main():
    temp = 1
    pr_list = []

    if flask.request.method == 'GET':
        return render_template('main.html' )

    if flask.request.method == 'POST':
        loaded_model = pickle.load('model1')
        for i in range(1, 13, 1):
                 pr = flask.request.form.get(f'pr{i}')
                 pr_lst.append(float(pr))

        y_pred = loaded_model.predict([[pr_list]])
        return render_template('main.html', result = y_pred)         

if __name__ == '__main__':
    app.run()