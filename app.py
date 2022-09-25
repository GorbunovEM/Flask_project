from flask import Flask, render_template, request
from methods import Methods
from web_page import Web_page
from pandas.core.common import flatten
from get_analog import get_analog
from function import id_and_geo
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/newmos_aparts', methods=['POST', 'GET'])
def newmos_aparts():
    try:
        data = pd.read_csv('new_moscow_aparts.csv', sep=";", encoding='utf-8')
        page = Web_page(data)
        template_context = page.form_dict()

        if request.method == 'POST':
            out = Methods.get_dict()
            if not out:
                template_context = page.form_dict()
            else:
                template_context = page.refresh_page(out)

        return render_template('newmoscow.html', **template_context)
    except:
        return render_template('error.html')


@app.route('/<id_project>', methods=['POST', 'GET'])
def mf_charts(id_project):
    i = 0
    data_type = pd.read_csv('id.csv', sep=";", encoding='utf-8')
    type_project = []

    for element in list(data_type.id):
        if id_project == element:
            type_project = list(data_type.Type)[i]
        i = i + 1

    data = pd.DataFrame()

    if type_project == "new_moscow_aparts":
        data = pd.read_csv('new_moscow_aparts.csv', sep=";", encoding='utf-8')

    key_class = list(flatten(list(id_and_geo(data).values())))
    if id_project in key_class:

        page = Web_page(data)
        template_context = page.second_page(id_project)

        if request.method == 'POST':
            get_analog(id_project, data)

        return render_template('chart.html', **template_context)

@app.route('/SomeFunction')
def SomeFunction():
    #get_analog(data)
    print('In SomeFunction')
    return "Nothing"

@app.route('/shutdown')
def shutdown():
    return request.environ.get('werkzeug.server.shutdown')()


if __name__ == '__main__':
    app.run(debug=True)
