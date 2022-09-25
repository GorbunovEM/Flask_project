from statistics import mean
import pandas as pd
import math


class Charts:


    @staticmethod
    def charts(id, data):
        data_grp = list(data.groupby("id1").get_group(id).groupby("Deal3").groups.keys())
        price_group = []
        area_group = []
        for element in data_grp:
            a = data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Price.mean()
            b = data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Area1.sum()
            if pd.isnull(a):
                price_group.append(0)
            else:
                price_group.append(
                    round(data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Price.mean()))
            if pd.isnull(b):
                area_group.append(0)
            else:
                area_group.append(
                    round(data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Area1.sum()))
        return data_grp, price_group, area_group

    @staticmethod
    def main_chart(data, out):
        if 'Deal3' in out.keys():
            del out['Deal3']
        deal = ["2020 4кв.", "2021 1кв.", "2021 2кв.", "2021 3кв.", "2021 4кв."]
        mean_price = []
        sum_area = []
        price = []
        area = []

        if len(out) == 0:
            for item_0 in deal:
                try:
                    mean_price.append(data.groupby(['Deal3']).mean().round().Price[item_0])
                    sum_area.append(data.groupby(['Deal3']).sum().round().Area1[item_0])
                except:
                    next
                price.append(round(mean([item for item in mean_price if not (math.isnan(item)) == True])))
                area.append(round(sum([item for item in sum_area if not (math.isnan(item)) == True])))
                mean_price = []
                sum_area = []

        elif len(out) == 1:
            for item_0 in deal:
                for item_1 in out[list(out.keys())[0]]:
                    try:
                        mean_price.append(data.groupby(['Deal3', list(out.keys())[0]]).mean().round()
                                               .Price[item_0][item_1])
                        sum_area.append(data.groupby(['Deal3', list(out.keys())[0]]).sum().round()
                                              .Area1[item_0][item_1])
                    except:
                        next
                price.append(round(mean([item for item in mean_price if not (math.isnan(item)) == True])))
                area.append(round(sum([item for item in sum_area if not (math.isnan(item)) == True])))
                mean_price = []
                sum_area = []

        elif len(out) == 2:
            for item_0 in deal:
                for item_1 in out[list(out.keys())[0]]:
                    for item_2 in out[list(out.keys())[1]]:
                        try:
                            mean_price.append(data.groupby(['Deal3', list(out.keys())[0], list(out.keys())[1]]).mean()
                                              .round().Price[item_0][item_1][item_2])
                            sum_area.append(data.groupby(['Deal3', list(out.keys())[0], list(out.keys())[1]]).sum()
                                            .round().Area1[item_0][item_1][item_2])
                        except:
                            next
                price.append(round(mean([item for item in mean_price if not (math.isnan(item)) == True])))
                area.append(round(sum([item for item in sum_area if not (math.isnan(item)) == True])))
                mean_price = []
                sum_area = []

        elif len(out) == 3:
            for item_0 in deal:
                for item_1 in out[list(out.keys())[0]]:
                    for item_2 in out[list(out.keys())[1]]:
                        for item_3 in out[list(out.keys())[2]]:
                            try:
                                mean_price.append(
                                    data.groupby(['Deal3', list(out.keys())[0], list(out.keys())[1], list(out.keys())[2]])
                                        .mean().round().Price[item_0][item_1][item_2][item_3])
                                sum_area.append(
                                    data.groupby(['Deal3', list(out.keys())[0], list(out.keys())[1], list(out.keys())[2]])
                                        .sum().round().Area1[item_0][item_1][item_2][item_3])
                            except:
                                next
                price.append(round(mean([item for item in mean_price if not (math.isnan(item)) == True])))
                area.append(round(sum([item for item in sum_area if not (math.isnan(item)) == True])))
                mean_price = []
                sum_area = []
        return (price, area)