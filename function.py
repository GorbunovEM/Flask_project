import pandas as pd
from pandas.core.common import flatten

def id_and_geo(data):
    key_code = list(data.groupby(['Project', "id1"]).id1)
    key_class = list(data.groupby('Project').groups.keys())
    key_geo1 = list(data.groupby(['Project', "Geo_spot1"]).Geo_spot1)
    key_geo2 = list(data.groupby(['Project', "Geo_spot2"]).Geo_spot2)
    list_project = {}
    for i in range(len(key_class)):
        list_project[key_class[i]] = [list(set(key_code[i][1]))[0], list(set(key_geo1[i][1]))[0],
                                      list(set(key_geo2[i][1]))[0]]
    print(list(flatten(list(list_project.values()))))
    return list_project


def format_data(x):
    try:
        num = round(x, 0)
        return '{0:,}'.format(num).replace(',', ' ')
    except:
        return 1