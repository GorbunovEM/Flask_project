from flask import Flask, render_template, request
from func import *
import pandas as pd
from pandas.core.common import flatten
from get_analog import get_analog

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/moscow_flats', methods=['POST', 'GET'])
def moscow_flats():
    try:
        data = pd.read_csv('moscow_flats.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        try:
            all_flat = rang(round(data.Price.mean()))
        except:
            all_flat = 0
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(round(data.Area1.sum()))
        qunt_flat = rang(round(data.id2.count()))
        temp_flat = rang(round(data.Area1.sum()) / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int,list((request.form.getlist('finish')))))

            if (len(get_deal)!=0 and len(get_dist)==0 and len(get_class)==0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)==0 and len(get_class)!=0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)!=0 and len(get_class)!=0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                                        key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)!=0 and len(get_class)!=0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)!=0 and len(get_class)!=0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])/(len(key_deal))),
                                        key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)!=0 and len(get_class)!=0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)==0 and len(get_class)!=0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)!=0 and len(get_class)==0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)==0 and len(get_class)==0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)==0 and len(get_class)==0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)!=0 and len(get_class)==0 and len(get_finish)==0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)!=0 and len(get_class)==0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                                        key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)!=0 and len(get_dist)==0 and len(get_class)!=0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                                        key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)==0 and len(get_class)!=0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal)==0 and len(get_dist)!=0 and len(get_class)==0 and len(get_finish)!=0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('moscow.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/moscow_aparts', methods=['POST', 'GET'])
def moscow_aparts():
    try:
        data = pd.read_csv('moscow_aparts.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1 = main_chart(data, fin = [], cls = [], dist = [])[0],
                                values2 = main_chart(data, fin = [], cls = [], dist = [])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                    template_context = dict(all_flat=float(iter_mean_class_nor(data, get_class)[0]),
                                            oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                            twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                            threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                            fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                            stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                            area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                            qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                            temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                            key_class=iter_mean_class_nor(data, get_class)[3],
                                            key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                            values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                            values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('moscow_aparts.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/spb_flats', methods=['POST', 'GET'])
def spb_flats():
    try:
        data = pd.read_csv('spb_flats.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        try:
            all_flat = rang(round(data.Price.mean()))
        except:
            all_flat = 0
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(round(data.Area1.sum()))
        qunt_flat = rang(round(data.id2.count()))
        temp_flat = rang(round(data.Area1.sum()) / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(
                    float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang((float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal)))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('spb.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/spb_aparts', methods=['POST', 'GET'])
def spb_aparts():
    try:
        data = pd.read_csv('spb_aparts.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('spb.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/newmos_flats', methods=['POST', 'GET'])
def newmos_flats():
    try:
        data = pd.read_csv('new_moscow_flats.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('newmoscow.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/newmos_aparts', methods=['POST', 'GET'])
def newmos_aparts():
    try:
        data = pd.read_csv('new_moscow_aparts.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('newmoscow.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/mosregion_flats', methods=['POST', 'GET'])
def mosrigion_flats():
    try:
        data = pd.read_csv('moscow_region_flats.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(
                    float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('mosregion.html', **template_context)
    except:
        return render_template('error.html')

@app.route('/mosregion_aparts', methods=['POST', 'GET'])
def mosrigion_aparts():
    try:
        data = pd.read_csv('moscow_region_aparts.csv', sep=";", encoding='utf-8')
        finish_grp = data.groupby('Date_finish').groups
        deal_grp = data.groupby('Deal3').groups
        room_grp = data.groupby('Room').mean()
        key_class = get_id(data)
        key_finish = list(finish_grp.keys())
        key_deal = list(deal_grp.keys())

        all_flat = rang(data.Price.mean().round())
        try:
            oneflat = rang(room_grp.Price[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp.Price[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp.Price[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp.Price[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp.Price[0])
        except:
            stflat = 0

        area_flat = rang(data.Area1.sum().round())
        qunt_flat = rang(data.id2.count().round())
        temp_flat = rang(data.Area1.sum().round() / len(key_deal))

        template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])

        if request.method == 'POST':
            get_dist = list((request.form.getlist('dist')))
            get_class = list((request.form.getlist('class')))
            get_deal = list((request.form.getlist('deal')))
            get_finish = list(map(int, list((request.form.getlist('finish')))))

            if (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_nor(data, get_deal)[0])),
                                        oneflat=rang(float(iter_mean_deal(data, 1, get_deal))),
                                        twoflat=rang(float(iter_mean_deal(data, 2, get_deal))),
                                        threeflat=rang(float(iter_mean_deal(data, 3, get_deal))),
                                        fourflat=rang(float(iter_mean_deal(data, 4, get_deal))),
                                        stflat=rang(float(iter_mean_deal(data, 0, get_deal))),
                                        area_flat=rang(float(iter_mean_deal_nor(data, get_deal)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_nor(data, get_deal)[2])),
                                        temp_flat=rang(float(iter_mean_deal_nor(data, get_deal)[3])),
                                        key_class=iter_mean_deal_nor(data, get_deal)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[0])),
                                        oneflat=rang(float(iter_mean_deal_class(data, 1, get_deal, get_class))),
                                        twoflat=rang(float(iter_mean_deal_class(data, 2, get_deal, get_class))),
                                        threeflat=rang(float(iter_mean_deal_class(data, 3, get_deal, get_class))),
                                        fourflat=rang(float(iter_mean_deal_class(data, 4, get_deal, get_class))),
                                        stflat=rang(float(iter_mean_deal_class(data, 0, get_deal, get_class))),
                                        area_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_nor(data, get_deal, get_class)[3])),
                                        key_class=iter_mean_deal_class_nor(data, get_deal, get_class)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[0])),
                    oneflat=rang(float(iter_mean_deal_class_dist(data, 1, get_deal, get_class, get_dist))),
                    twoflat=rang(float(iter_mean_deal_class_dist(data, 2, get_deal, get_class, get_dist))),
                    threeflat=rang(float(iter_mean_deal_class_dist(data, 3, get_deal, get_class, get_dist))),
                    fourflat=rang(float(iter_mean_deal_class_dist(data, 4, get_deal, get_class, get_dist))),
                    stflat=rang(float(iter_mean_deal_class_dist(data, 0, get_deal, get_class, get_dist))),
                    area_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[3])),
                    key_class=iter_mean_deal_class_dist_nor(data, get_deal, get_class, get_dist)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_class_dist_fin(data, 1, get_deal, get_class, get_dist,get_finish))),
                                        twoflat=rang(float(iter_mean_deal_class_dist_fin(data, 2, get_deal, get_class, get_dist,get_finish))),
                                        threeflat=rang(float(iter_mean_deal_class_dist_fin(data, 3, get_deal, get_class, get_dist,get_finish))),
                                        fourflat=rang(float(iter_mean_deal_class_dist_fin(data, 4, get_deal, get_class, get_dist,get_finish))),
                                        stflat=rang(float(iter_mean_deal_class_dist_fin(data, 0, get_deal, get_class, get_dist,get_finish))),
                                        area_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist,get_finish)[3])),
                                        key_class=iter_mean_deal_class_dist_fin_nor(data, get_deal, get_class, get_dist, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_class_dist_fin(data, 1, get_class, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_class_dist_fin(data, 2, get_class, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_class_dist_fin(data, 3, get_class, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_class_dist_fin(data, 4, get_class, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_class_dist_fin(data, 0, get_class, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[1]) / (len(key_deal))),
                    key_class=iter_mean_class_dist_fin_nor(data, get_class, get_dist, get_finish)[3],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_class_dist(data, 1, get_class, get_dist))),
                                        twoflat=rang(float(iter_mean_class_dist(data, 2, get_class, get_dist))),
                                        threeflat=rang(float(iter_mean_class_dist(data, 3, get_class, get_dist))),
                                        fourflat=rang(float(iter_mean_class_dist(data, 4, get_class, get_dist))),
                                        stflat=rang(float(iter_mean_class_dist(data, 0, get_class, get_dist))),
                                        area_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_class_dist_nor(data, get_class, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_dist_nor(data, get_class, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_nor(data, get_class)[0])),
                                        oneflat=rang(float(iter_mean_class(data, 1, get_class))),
                                        twoflat=rang(float(iter_mean_class(data, 2, get_class))),
                                        threeflat=rang(float(iter_mean_class(data, 3, get_class))),
                                        fourflat=rang(float(iter_mean_class(data, 4, get_class))),
                                        stflat=rang(float(iter_mean_class(data, 0, get_class))),
                                        area_flat=rang(float(iter_mean_class_nor(data, get_class)[1])),
                                        qunt_flat=rang(float(iter_mean_class_nor(data, get_class)[2])),
                                        temp_flat=rang(float(iter_mean_class_nor(data, get_class)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_nor(data, get_class)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_nor(data, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_dist(data, 1, get_dist))),
                                        twoflat=rang(float(iter_mean_dist(data, 2, get_dist))),
                                        threeflat=rang(float(iter_mean_dist(data, 3, get_dist))),
                                        fourflat=rang(float(iter_mean_dist(data, 4, get_dist))),
                                        stflat=rang(float(iter_mean_dist(data, 0, get_dist))),
                                        area_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_nor(data, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_dist_nor(data, get_dist)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_nor(data, get_dist)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_fin_nor(data, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_fin(data, 1, get_finish))),
                                        twoflat=rang(float(iter_mean_fin(data, 2, get_finish))),
                                        threeflat=rang(float(iter_mean_fin(data, 3, get_finish))),
                                        fourflat=rang(float(iter_mean_fin(data, 4, get_finish))),
                                        stflat=rang(float(iter_mean_fin(data, 0, get_finish))),
                                        area_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_fin_nor(data, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_fin_nor(data, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_fin_nor(data, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_deal_fin(data, 1, get_deal, get_finish))),
                                        twoflat=rang(float(iter_mean_deal_fin(data, 2, get_deal, get_finish))),
                                        threeflat=rang(float(iter_mean_deal_fin(data, 3, get_deal, get_finish))),
                                        fourflat=rang(float(iter_mean_deal_fin(data, 4, get_deal, get_finish))),
                                        stflat=rang(float(iter_mean_deal_fin(data, 0, get_deal, get_finish))),
                                        area_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_deal_fin_nor(data, get_deal, get_finish)[3])),
                                        key_class=iter_mean_deal_fin_nor(data, get_deal, get_finish)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) == 0):
                template_context = dict(all_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[0])),
                                        oneflat=rang(float(iter_mean_deal_dist(data, 1, get_deal, get_dist))),
                                        twoflat=rang(float(iter_mean_deal_dist(data, 2, get_deal, get_dist))),
                                        threeflat=rang(float(iter_mean_deal_dist(data, 3, get_deal, get_dist))),
                                        fourflat=rang(float(iter_mean_deal_dist(data, 4, get_deal, get_dist))),
                                        stflat=rang(float(iter_mean_deal_dist(data, 0, get_deal, get_dist))),
                                        area_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[1])),
                                        qunt_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[2])),
                                        temp_flat=rang(float(iter_mean_deal_dist_nor(data, get_deal, get_dist)[3])),
                                        key_class=iter_mean_deal_dist_nor(data, get_deal, get_dist)[4],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_dist_fin(data, 1, get_deal, get_dist, get_finish))),
                    twoflat=rang(float(iter_mean_deal_dist_fin(data, 2, get_deal, get_dist, get_finish))),
                    threeflat=rang(float(iter_mean_deal_dist_fin(data, 3, get_deal, get_dist, get_finish))),
                    fourflat=rang(float(iter_mean_deal_dist_fin(data, 4, get_deal, get_dist, get_finish))),
                    stflat=rang(float(iter_mean_deal_dist_fin(data, 0, get_deal, get_dist, get_finish))),
                    area_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[3])),
                    key_class=iter_mean_deal_dist_fin_nor(data, get_deal, get_dist, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) != 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(
                    all_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[0])),
                    oneflat=rang(float(iter_mean_deal_class_fin(data, 1, get_deal, get_class, get_finish))),
                    twoflat=rang(float(iter_mean_deal_class_fin(data, 2, get_deal, get_class, get_finish))),
                    threeflat=rang(float(iter_mean_deal_class_fin(data, 3, get_deal, get_class, get_finish))),
                    fourflat=rang(float(iter_mean_deal_class_fin(data, 4, get_deal, get_class, get_finish))),
                    stflat=rang(float(iter_mean_deal_class_fin(data, 0, get_deal, get_class, get_finish))),
                    area_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[1])),
                    qunt_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[2])),
                    temp_flat=rang(float(iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[3])),
                    key_class=iter_mean_deal_class_fin_nor(data, get_deal, get_class, get_finish)[4],
                    key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
                    values1=main_chart(data, get_finish, get_class, get_dist)[0],
                    values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) == 0 and len(get_class) != 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[0])),
                                        oneflat=rang(float(iter_mean_class_fin(data, 1, get_class, get_finish))),
                                        twoflat=rang(float(iter_mean_class_fin(data, 2, get_class, get_finish))),
                                        threeflat=rang(float(iter_mean_class_fin(data, 3, get_class, get_finish))),
                                        fourflat=rang(float(iter_mean_class_fin(data, 4, get_class, get_finish))),
                                        stflat=rang(float(iter_mean_class_fin(data, 0, get_class, get_finish))),
                                        area_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_class_fin_nor(data, get_class, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_class_fin_nor(data, get_class, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            elif (len(get_deal) == 0 and len(get_dist) != 0 and len(get_class) == 0 and len(get_finish) != 0):
                template_context = dict(all_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        oneflat=rang(float(iter_mean_dist_fin(data, 1, get_dist, get_finish))),
                                        twoflat=rang(float(iter_mean_dist_fin(data, 2, get_dist, get_finish))),
                                        threeflat=rang(float(iter_mean_dist_fin(data, 3, get_dist, get_finish))),
                                        fourflat=rang(float(iter_mean_dist_fin(data, 4, get_dist, get_finish))),
                                        stflat=rang(float(iter_mean_dist_fin(data, 0, get_dist, get_finish))),
                                        area_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1])),
                                        qunt_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[2])),
                                        temp_flat=rang(float(iter_mean_dist_fin_nor(data, get_dist, get_finish)[1]) / (len(key_deal))),
                                        key_class=iter_mean_dist_fin_nor(data, get_dist, get_finish)[3],
                                        key_finish=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"],
                                        values1=main_chart(data, get_finish, get_class, get_dist)[0],
                                        values2=main_chart(data, get_finish, get_class, get_dist)[1])
            else:
                template_context = dict(all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat,
                                key_class=key_class,
                                key_finish=key_finish,
                                values1=main_chart(data, fin=[], cls=[], dist=[])[0],
                                values2=main_chart(data, fin=[], cls=[], dist=[])[1])
        return render_template('mosregion.html', **template_context)
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

    if type_project == "moscow_aparts":
        data = pd.read_csv('moscow_aparts.csv', sep=";", encoding='utf-8')
    elif type_project == "moscow_flats":
        data = pd.read_csv('moscow_flats.csv', sep=";", encoding='utf-8')
    elif type_project == "moscow_region_aparts":
        data = pd.read_csv('moscow_region_aparts.csv', sep=";", encoding='utf-8')
    elif type_project == "moscow_region_flats":
        data = pd.read_csv('moscow_region_flats.csv', sep=";", encoding='utf-8')
    elif type_project == "new_moscow_aparts":
        data = pd.read_csv('new_moscow_aparts.csv', sep=";", encoding='utf-8')
    elif type_project == "new_moscow_flats":
        data = pd.read_csv('new_moscow_flats.csv', sep=";", encoding='utf-8')
    elif type_project == "spb_aparts":
        data = pd.read_csv('spb_aparts.csv', sep=";", encoding='utf-8')
    elif type_project == "spb_flats":
        data = pd.read_csv('spb_flats.csv', sep=";", encoding='utf-8')

    key_class = list(flatten(list(get_id(data).values())))
    if id_project in key_class:

        legend = 'Кварталы'
        labels = charts(id_project, data)[0]
        values1 = charts(id_project, data)[2]
        values2 = charts(id_project, data)[1]
        room_grp = data.groupby('id1').get_group(id_project).groupby("Room").Price.mean().round()

        key_deal = len(labels)
        try:
            all_flat = rang(data.groupby('id1').get_group(id_project).Price.mean())
        except:
            all_flat = 0
        try:
            oneflat = rang(room_grp[1])
        except:
            oneflat = 0
        try:
            twoflat = rang(room_grp[2])
        except:
            twoflat = 0
        try:
            threeflat = rang(room_grp[3])
        except:
            threeflat = 0
        try:
            fourflat = rang(room_grp[4])
        except:
            fourflat = 0
        try:
            stflat = rang(room_grp[0])
        except:
            stflat = 0

        area_flat = rang(data.groupby('id1').get_group(id_project).Area1.sum().round())
        qunt_flat = rang(data.groupby('id1').get_group(id_project).Area1.count().round())
        temp_flat = rang(data.groupby('id1').get_group(id_project).Area1.sum().round() / key_deal)

        template_context = dict(values1=values1,
                                values2=values2,
                                labels=labels,
                                legend=legend,
                                all_flat=all_flat,
                                oneflat=oneflat,
                                twoflat=twoflat,
                                threeflat=threeflat,
                                fourflat=fourflat,
                                stflat=stflat,
                                area_flat=area_flat,
                                qunt_flat=qunt_flat,
                                temp_flat=temp_flat)
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
