from flask import Flask, render_template, request
import pickle
import numpy as np


def input_lister(url: str):
    inp = []

    # having ip
    if url.__contains__('0x') or url.count(':') > 1:
        inp.append(-1)
    else:
        inp.append(1)

    # url length
    if len(url) <= 54:
        inp.append(1)
    else:
        inp.append(-1)

    # shortening
    if 'bit.ly' in url:
        inp.append(-1)
    else:
        inp.append(1)

    # having @
    if '@' in url:
        inp.append(-1)
    else:
        inp.append(1)

    # double slash
    if '//' in url[7:]:
        inp.append(-1)
    else:
        inp.append(1)

    # prefix_suffix
    if '-' in url:
        inp.append(-1)
    else:
        inp.append(1)

    return inp


model = pickle.load(open('probability_checker.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('opening.html')


@app.route('/predictor', methods=['POST'])
def predictor():
    url = request.form['url']
    favicon = request.form['favicon']
    if favicon!=-1 and favicon!=1:
        favicon = 1
    remaining_inp = input_lister(url)+[favicon]
    remaining_inp = np.array([remaining_inp])
    p = model.predict(remaining_inp)
    return render_template('predictor.html', data=[url, p])


if __name__ == "__main__":
    app.run(debug=True)
