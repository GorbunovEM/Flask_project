import pandas as pd
import numpy as np
import math

def get_analog(id ,data):

    last_period = list(data.groupby("id1").get_group(id).groupby("Deal3").groups.keys())[-1]
    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []


    if len(list(data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).Price)) < 10:
        last_period = list(data.groupby("id1").get_group(id).groupby("Deal3").groups.keys())[-2]
    else:
        last_period = list(data.groupby("id1").get_group(id).groupby("Deal3").groups.keys())[-1]

    try:
        room_0 = data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).groupby("Room").get_group(0)
        for i in range(len(list(room_0.Price))):
            dict_0 = dict(room_0.iloc[i])
            list_0.append(dict_0)
        newlist_0 = sorted(list_0, key=lambda k: k['Price'])
        n_0 = math.ceil(len(newlist_0) / 2)

        analog_0 = [[newlist_0[n_0 - 1]["Project"], newlist_0[n_0 - 1]["id3"], newlist_0[n_0 - 1]["Room"],
                     newlist_0[n_0 - 1]["Area1"],newlist_0[n_0 - 1]["Price"], newlist_0[n_0 - 1]["Date_finish"]],
                    [newlist_0[n_0]["Project"], newlist_0[n_0]["id3"], newlist_0[n_0]["Room"], newlist_0[n_0]["Area1"],
                     newlist_0[n_0]["Price"], newlist_0[n_0]["Date_finish"]],
                    [newlist_0[n_0 + 1]["Project"], newlist_0[n_0 + 1]["id3"], newlist_0[n_0 + 1]["Room"],
                     newlist_0[n_0 + 1]["Area1"], newlist_0[n_0 + 1]["Price"], newlist_0[n_0 + 1]["Date_finish"]]]
    except:
        analog_0 = [["Нет данных", "Нет данных", "студия", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "студия", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "студия", "Нет данных", "Нет данных", "Нет данных"]]

    try:
        room_1 = data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).groupby("Room").get_group(1)
        for i in range(len(list(room_1.Price))):
            dict_1 = dict(room_1.iloc[i])
            list_1.append(dict_1)
        newlist_1 = sorted(list_1, key=lambda k: k['Price'])
        n_1 = math.ceil(len(newlist_1) / 2)

        analog_1 = [[newlist_1[n_1 - 1]["Project"], newlist_1[n_1 - 1]["id3"],newlist_1[n_1 - 1]["Room"],
                     newlist_1[n_1 - 1]["Area1"], newlist_1[n_1 - 1]["Price"], newlist_1[n_1 - 1]["Date_finish"]],
                    [newlist_1[n_1]["Project"], newlist_1[n_1]["id3"], newlist_1[n_1]["Room"],
                     newlist_1[n_1]["Area1"], newlist_1[n_1]["Price"], newlist_1[n_1]["Date_finish"]],
                    [newlist_1[n_1 + 1]["Project"], newlist_1[n_1 + 1]["id3"],newlist_1[n_1 + 1]["Room"],
                     newlist_1[n_1 + 1]["Area1"], newlist_1[n_1 + 1]["Price"], newlist_1[n_1 + 1]["Date_finish"]]]
    except:
        analog_1 = [["Нет данных", "Нет данных", "1", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "1", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "1", "Нет данных", "Нет данных", "Нет данных"]]


    try:
        room_2 = data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).groupby("Room").get_group(2)
        for i in range(len(list(room_2.Price))):
            dict_2 = dict(room_2.iloc[i])
            list_2.append(dict_2)
        newlist_2 = sorted(list_2, key=lambda k: k['Price'])
        n_2 = math.ceil(len(newlist_2) / 2)

        analog_2 = [[newlist_2[n_2 - 1]["Project"], newlist_2[n_2 - 1]["id3"],newlist_2[n_2 - 1]["Room"],
                     newlist_2[n_2 - 1]["Area1"], newlist_2[n_2 - 1]["Price"], newlist_2[n_2 - 1]["Date_finish"]],
                    [newlist_2[n_2]["Project"], newlist_2[n_2]["id3"], newlist_2[n_2]["Room"], newlist_2[n_2]["Area1"],
                     newlist_2[n_2]["Price"], newlist_2[n_2]["Date_finish"]],
                    [newlist_2[n_2 + 1]["Project"], newlist_2[n_2 + 1]["id3"],newlist_2[n_2 + 1]["Room"],
                     newlist_2[n_2 + 1]["Area1"], newlist_2[n_2 + 1]["Price"], newlist_2[n_2 + 1]["Date_finish"]]]
    except:
        analog_2 = [["Нет данных", "Нет данных", "2", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "2", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "2", "Нет данных", "Нет данных", "Нет данных"]]

    try:
        room_3 = data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).groupby("Room").get_group(3)
        for i in range(len(list(room_3.Price))):
            dict_3 = dict(room_3.iloc[i])
            list_3.append(dict_3)
        newlist_3 = sorted(list_3, key=lambda k: k['Price'])
        n_3 = math.ceil(len(newlist_3) / 2)

        analog_3 = [[newlist_3[n_3 - 1]["Project"], newlist_3[n_3 - 1]["id3"],newlist_3[n_3 - 1]["Room"],
                     newlist_3[n_3 - 1]["Area1"], newlist_3[n_3 - 1]["Price"], newlist_3[n_3 - 1]["Date_finish"]],
                    [newlist_3[n_3]["Project"], newlist_3[n_3]["id3"], newlist_3[n_3]["Room"], newlist_3[n_3]["Area1"],
                     newlist_3[n_3]["Price"], newlist_3[n_3]["Date_finish"]],
                    [newlist_3[n_3 + 1]["Project"], newlist_3[n_3 + 1]["id3"],newlist_3[n_3 + 1]["Room"],
                     newlist_3[n_3 + 1]["Area1"], newlist_3[n_3 + 1]["Price"], newlist_3[n_3 + 1]["Date_finish"]]]
    except:
        analog_3 = [["Нет данных", "Нет данных", "3", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "3", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "3", "Нет данных", "Нет данных", "Нет данных"]]

    try:
        room_4 = data.groupby("id1").get_group(id).groupby("Deal3").get_group(last_period).groupby("Room").get_group(4)
        for i in range(len(list(room_4.Price))):
            dict_4 = dict(room_4.iloc[i])
            list_4.append(dict_4)
        newlist_4 = sorted(list_4, key=lambda k: k['Price'])
        n_4 = math.ceil(len(newlist_4) / 2)

        analog_4 = [[newlist_4[n_4 - 1]["Project"], newlist_4[n_4 - 1]["id3"],newlist_4[n_4 - 1]["Room"],
                     newlist_4[n_4 - 1]["Area1"], newlist_4[n_4 - 1]["Price"], newlist_4[n_4 - 1]["Date_finish"]],
                    [newlist_4[n_4]["Project"], newlist_4[n_4]["id3"], newlist_4[n_4]["Room"], newlist_4[n_4]["Area1"],
                     newlist_4[n_4]["Price"], newlist_4[n_4]["Date_finish"]],
                    [newlist_4[n_4 + 1]["Project"], newlist_4[n_4 + 1]["id3"],newlist_4[n_4 + 1]["Room"],
                     newlist_4[n_4 + 1]["Area1"], newlist_4[n_4 + 1]["Price"], newlist_4[n_4 + 1]["Date_finish"]]]
    except:
        analog_4 = [["Нет данных", "Нет данных", "4", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "4", "Нет данных", "Нет данных", "Нет данных"],
                    ["Нет данных", "Нет данных", "4", "Нет данных", "Нет данных", "Нет данных"]]


    Table_excel = pd.DataFrame(np.array(analog_0+analog_1+analog_2+analog_3+analog_4),
                       columns=["Project", "id3", "Room", "Area1", "Price", "Date_finish"])

    Table_excel["Area1"] = [x.replace('.', ',') for x in Table_excel["Area1"]]
    Table_excel["Price"] = [x.replace('.', ',') for x in Table_excel["Price"]]
    # Specify a writer
    writer = pd.ExcelWriter('Analog.xlsx', engine='xlsxwriter')

    # Write your DataFrame to a file
    Table_excel.to_excel(writer, 'Sheet1')

    # Save the result
    writer.save()