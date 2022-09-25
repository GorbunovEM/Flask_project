from statistics import mean
import math
from flask import request


class Methods:

    def __init__(self):
        self.district_list = []
        self.class_list = []
        self.deal_date_list = []
        self.finish_date_list = []

    @staticmethod
    def get_dict():
        out = {}
        district_list = list((request.form.getlist('dist')))
        class_list = list((request.form.getlist('class')))
        deal_date_list = list((request.form.getlist('deal')))
        finish_date_list = list(map(int, list((request.form.getlist('finish')))))
        if district_list:
            out['Dist1'] = district_list
        if class_list:
            out['Class'] = class_list
        if deal_date_list:
            out['Deal3'] = deal_date_list
        if finish_date_list:
            out['Date_finish'] = finish_date_list
        return out

    @staticmethod
    def find_mean_price(data, out, room=1):
        if len(out) == 1:
            try:
                grp_w_room = data.groupby(['Room', list(out.keys())[0]]).mean().round()
                grp_wo_room = data.groupby([list(out.keys())[0]]).mean().round()
                mean_price_room = []
                mean_price = []
                for item_0 in out[list(out.keys())[0]]:
                    mean_price_room.append(grp_w_room.Price[room][item_0])
                    mean_price.append(grp_wo_room.Price[item_0])
                room = mean([m for m in mean_price_room if not (math.isnan(m)) == True])
                all = mean([m for m in mean_price if not (math.isnan(m)) == True])
                return room, all
            except:
                return 1, 1

        if len(out) == 2:
            try:
                grp_w_room = data.groupby(['Room', list(out.keys())[0], list(out.keys())[1]]).mean().round()
                grp_wo_room = data.groupby([list(out.keys())[0], list(out.keys())[1]]).mean().round()
                mean_price_room = []
                mean_price = []
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[1]]:
                        try:
                            mean_price_room.append(grp_w_room.Price[room][item_0][item_1])
                            mean_price.append(grp_wo_room.Price[item_0][item_1])
                        except:
                            next
                room = mean([m for m in mean_price_room if not (math.isnan(m)) == True])
                all = mean([m for m in mean_price if not (math.isnan(m)) == True])
                return room, all
            except:
                return 1, 1

        elif len(out) == 3:
            try:
                grp_w_room = data.groupby(['Room', list(out.keys())[0], list(out.keys())[1],
                                           list(out.keys())[2]]).mean().round()
                grp_wo_room = data.groupby([list(out.keys())[0], list(out.keys())[1],
                                            list(out.keys())[2]]).mean().round()
                mean_price_room = []
                mean_price = []
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[1]]:
                        try:
                            for item_2 in out[list(out.keys())[2]]:
                                try:
                                    mean_price_room.append(grp_w_room.Price[room][item_0][item_1][item_2])
                                    mean_price.append(grp_wo_room.Price[item_0][item_1][item_2])
                                except:
                                    next
                        except:
                            next
                room = mean([m for m in mean_price_room if not (math.isnan(m)) == True])
                all = mean([m for m in mean_price if not (math.isnan(m)) == True])
                return room, all
            except:
                return 1, 1

        elif len(out) == 4:
            try:
                grp_w_room = data.groupby(["Room", list(out.keys())[0], list(out.keys())[1],
                                    list(out.keys())[2], list(out.keys())[3]]).mean().round()
                grp_wo_room = data.groupby(["Room", list(out.keys())[0], list(out.keys())[1],
                                           list(out.keys())[2], list(out.keys())[3]]).mean().round()
                mean_price_room = []
                mean_price = []
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[1]]:
                        try:
                            for item_2 in out[list(out.keys())[2]]:
                                try:
                                    for item_3 in out[list(out.keys())[3]]:
                                        try:
                                            mean_price_room.append(grp_w_room.Price[room][item_0][item_1][item_2][item_3])
                                            mean_price.append(grp_wo_room.Price[item_0][item_1][item_2][item_3])
                                        except:
                                            next
                                except:
                                    next
                        except:
                            next
                room = mean([m for m in mean_price_room if not (math.isnan(m)) == True])
                all = mean([m for m in mean_price if not (math.isnan(m)) == True])
                return room, all
            except:
                return 1, 1

    @staticmethod
    def filter_data(data, out):
        if len(out) == 1:
            try:
                mean_area = []
                quant_square = []
                list_project = {}
                for item_0 in out[list(out.keys())[0]]:
                    mean_area.append(data.groupby([list(out.keys())[0]]).sum().round().Area1[item_0])
                    quant_square.append(data.groupby([list(out.keys())[0]]).count().round().Price[item_0])
                    name = list(data.groupby(list(out.keys())[0]).get_group(item_0).groupby(["Project", "id1"]).groups
                                .keys())
                    latitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                    .groupby(["Project", "Geo_spot1"]).groups.keys())
                    longitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                     .groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(name)):
                        list_project[name[i][0]] = [name[i][1], latitude[i][1], longitude[i][1]]
                sales_temp = sum(mean_area) / len(out[list(out.keys())[0]])
                return sum(mean_area), sum(quant_square), sales_temp, list_project
            except:
                return 1, 1, 1, 1

        if len(out) == 2:
            try:
                mean_area = []
                quant_square = []
                list_project = {}
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[0]]:
                        try:
                            mean_area.append(data.groupby([list(out.keys())[0], list(out.keys())[1]]).sum().round()
                                             .Area1[item_0][item_1])
                            quant_square.append(data.groupby([list(out.keys())[0], list(out.keys())[1]]).count()
                                                .round().Price[item_0][item_1])
                            name = list(data.groupby(list(out.keys())[0]).get_group(item_0).groupby(list(out.keys())[1])
                                     .get_group(item_1).groupby(["Project", "id1"]).groups.keys())
                            latitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                            .groupby(list(out.keys())[1]).get_group(item_1)
                                            .groupby(["Project", "Geo_spot1"]).groups.keys())
                            longitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                             .groupby(list(out.keys())[1])
                                             .get_group(item_1).groupby(["Project", "Geo_spot2"]).groups.keys())
                            for i in range(len(name)):
                                list_project[name[i][0]] = [name[i][1], latitude[i][1], longitude[i][1]]
                        except:
                            next
                sales_temp = sum(mean_area) / len(out[list(out.keys())[0]])
                return sum(mean_area), sum(quant_square), sales_temp, list_project
            except:
                return 1, 1, 1, 1

        if len(out) == 3:
            try:
                mean_area = []
                quant_square = []
                list_project = {}
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[0]]:
                        try:
                            for item_2 in out[list(out.keys())[0]]:
                                try:
                                    mean_area.append(
                                        data.groupby([list(out.keys())[0], list(out.keys())[1], list(out.keys())[2]])
                                            .sum().round().Area1[item_0][item_1][item_2])
                                    quant_square.append(
                                        data.groupby([list(out.keys())[0], list(out.keys())[1], list(out.keys())[2]])
                                            .count().round().Price[item_0][item_1][item_2])
                                    name = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                             .groupby(list(out.keys())[1])
                                             .get_group(item_1).groupby(list(out.keys())[2]).get_group(item_2)
                                             .groupby(["Project", "id1"]).groups.keys())
                                    latitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                             .groupby(list(out.keys())[1]).get_group(item_1)
                                             .groupby(list(out.keys())[2]).get_group(item_2)
                                             .groupby(["Project", "Geo_spot1"]).groups.keys())
                                    longitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                             .groupby(list(out.keys())[1]).get_group(item_1)
                                             .groupby(list(out.keys())[2]).get_group(item_2)
                                             .groupby(["Project", "Geo_spot2"]).groups.keys())
                                    for i in range(len(name)):
                                        list_project[name[i][0]] = [name[i][1], latitude[i][1], longitude[i][1]]
                                except:
                                    next
                        except:
                            next
                sales_temp = sum(mean_area) / len(out[list(out.keys())[0]])
                return sum(mean_area), sum(quant_square), sales_temp, list_project
            except:
                return 1, 1, 1, 1

        if len(out) == 4:
            try:
                mean_area = []
                quant_square = []
                list_project = {}
                for item_0 in out[list(out.keys())[0]]:
                    for item_1 in out[list(out.keys())[0]]:
                        try:
                            for item_2 in out[list(out.keys())[0]]:
                                try:
                                    for item_3 in out[list(out.keys())[0]]:
                                        try:
                                            mean_area.append(data.groupby([list(out.keys())[0], list(out.keys())[1],
                                                                           list(out.keys())[2], list(out.keys())[3]])
                                                             .sum().round().Area1[item_0][item_1][item_2][item_3])
                                            quant_square.append(data.groupby([list(out.keys())[0],
                                                                              list(out.keys())[1],
                                                                              list(out.keys())[2],
                                                                              list(out.keys())[3]])
                                                                .count().round().Price[item_0][item_1][item_2][item_3])
                                            name = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                                        .groupby(list(out.keys())[1]).get_group(
                                                item_1).groupby(list(out.keys())[2]).get_group(item_2)
                                                        .groupby(list(out.keys())[3]).get_group(item_3)
                                                        .groupby(["Project", "id1"]).groups.keys())
                                            latitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                                            .groupby(list(out.keys())[1])
                                                            .get_group(item_1).groupby(list(out.keys())[2])
                                                            .get_group(item_2).groupby(list(out.keys())[3]
                                                            .get_group(item_3).groupby(["Project", "Geo_spot1"])
                                                            .groups.keys()))
                                            longitude = list(data.groupby(list(out.keys())[0]).get_group(item_0)
                                                             .groupby(list(out.keys())[1])
                                                             .get_group(item_1).groupby(list(out.keys())[2])
                                                             .get_group(item_2).groupby(list(out.keys())[3])
                                                             .get_group(item_3).groupby(["Project", "Geo_spot2"])
                                                             .groups.keys())
                                            for i in range(len(name)):
                                                list_project[name[i][0]] = [name[i][1], latitude[i][1], longitude[i][1]]
                                        except:
                                            next
                                except:
                                    next
                        except:
                            next
                sales_temp = sum(mean_area) / len(out[list(out.keys())[0]])
                return sum(mean_area), sum(quant_square), sales_temp, list_project
            except:
                return 1, 1, 1, 1