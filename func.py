from statistics import mean
import pandas as pd
import math

#вставка пробела между разрядами
def rang(x):
    try:
        num = round(x, 0)
        return '{0:,}'.format(num).replace(',', ' ')
    except:
        return 0


# фильтр по дате сделки
def iter_mean_deal(data, room, deal):
    try:
        grp = data.groupby(["Room", 'Deal3']).mean().round()
        list_func = []
        for de in deal:
            list_func.append(grp.Price[room][de])
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки и классу
def iter_mean_deal_class(data, room, deal, cls):
    try:
        grp = data.groupby(["Room", 'Deal3', "Class"]).mean().round()
        list_func = []
        for de in deal:
            for cl in cls:
                try:
                    list_func.append(grp.Price[room][de][cl])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки, классу, району
def iter_mean_deal_class_dist(data, room, deal, cls, dist):
    try:
        grp = data.groupby(["Room", 'Deal3', "Class", "Dist1"]).mean().round()
        list_func = []
        for de in deal:
            for cl in cls:
                try:
                    for di in dist:
                        try:
                            list_func.append(grp.Price[room][de][cl][di])
                        except:
                            next
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки, классу, району, дате ввода
def iter_mean_deal_class_dist_fin(data, room, deal, cls, dist, fin):
    try:
        grp = data.groupby(["Room", 'Deal3', "Class", "Dist1", "Date_finish"]).mean().round()
        list_func = []
        for de in deal:
            for cl in cls:
                try:
                    for di in dist:
                        try:
                            for fi in fin:
                                try:
                                    list_func.append(grp.Price[room][de][cl][di][fi])
                                except:
                                    next
                        except:
                            next
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по классу, району, дате ввода
def iter_mean_class_dist_fin(data, room, cls, dist, fin):
    try:
        grp = data.groupby(["Room", "Class", "Dist1", "Date_finish"]).mean().round()
        list_func = []
        for cl in cls:
            for di in dist:
                try:
                    for fi in fin:
                        try:
                            list_func.append(grp.Price[room][cl][di][fi])
                        except:
                            next
                except:
                    next

        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по классу, району
def iter_mean_class_dist(data, room, cls, dist):
    try:
        grp = data.groupby(["Room", "Class", "Dist1"]).mean().round()
        list_func = []
        for cl in cls:
            for di in dist:
                try:
                    list_func.append(grp.Price[room][cl][di])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по классу
def iter_mean_class(data, room, cls):
    try:
        grp = data.groupby(["Room", "Class"]).mean().round()
        list_func = []
        for cl in cls:
            list_func.append(grp.Price[room][cl])
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по району
def iter_mean_dist(data, room, dist):
    try:
        grp = data.groupby(["Room", "Dist1"]).mean().round()
        list_func = []
        for di in dist:
            list_func.append(grp.Price[room][di])
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате ввода
def iter_mean_fin(data, room, fin):
    try:
        grp = data.groupby(["Room", "Date_finish"]).mean().round()
        list_func = []
        for fi in fin:
            list_func.append(grp.Price[room][fi])
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки и дате ввода
def iter_mean_deal_fin(data, room, deal, fin):
    try:
        grp = data.groupby(["Room", 'Deal3', "Date_finish"]).mean().round()
        list_func = []
        for de in deal:
            for fi in fin:
                try:
                    list_func.append(grp.Price[room][de][fi])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки и району
def iter_mean_deal_dist(data, room, deal, dist):
    try:
        grp = data.groupby(["Room", 'Deal3', "Dist1"]).mean().round()
        list_func = []
        for de in deal:
            for di in dist:
                try:
                    list_func.append(grp.Price[room][de][di])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки, району и дате ввода
def iter_mean_deal_dist_fin(data, room, deal, dist, fin):
    try:
        grp = data.groupby(["Room", 'Deal3', "Dist1", "Date_finish"]).mean().round()
        list_func = []
        for de in deal:
            for di in dist:
                try:
                    for fi in fin:
                        try:
                            list_func.append(grp.Price[room][de][di][fi])
                        except:
                            next
                except:
                    next

        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по дате сделки, классу, району
def iter_mean_deal_class_fin(data, room, deal, cls, fin):
    try:
        grp = data.groupby(["Room", 'Deal3', "Class", "Date_finish"]).mean().round()
        list_func = []
        for de in deal:
            for cl in cls:
                try:
                    for fi in fin:
                        try:
                            list_func.append(grp.Price[room][de][cl][fi])
                        except:
                            next
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по классу и дате ввода
def iter_mean_class_fin(data, room, cls, fin):
    try:
        grp = data.groupby(["Room", "Class", "Date_finish"]).mean().round()
        list_func = []
        for cl in cls:
            for fi in fin:
                try:
                    list_func.append(grp.Price[room][cl][fi])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

# фильтр по району и дате ввода
def iter_mean_dist_fin(data, room, dist, fin):
    try:
        grp = data.groupby(["Room", "Dist1", "Date_finish"]).mean().round()
        list_func = []
        for di in dist:
            for fi in fin:
                try:
                    list_func.append(grp.Price[room][di][fi])
                except:
                    next
        return mean([item for item in list_func if not(math.isnan(item)) == True])
    except:
        return 0

#///////////////////////////////////////////////////////////////////////////////////////////////////////
# фильтр по дате сделки
def iter_mean_deal_nor(data, deal):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            list_func_price.append(data.groupby(['Deal3']).mean().round().Price[de])
            list_func_area.append(data.groupby(['Deal3']).sum().round().Area1[de])
            list_func_quant.append(data.groupby(['Deal3']).count().round().Price[de])
            b = list(data.groupby('Deal3').get_group(de).groupby(["Project", "id1"]).groups.keys())
            c = list(data.groupby('Deal3').get_group(de).groupby(["Project", "Geo_spot1"]).groups.keys())
            d = list(data.groupby('Deal3').get_group(de).groupby(["Project", "Geo_spot2"]).groups.keys())
            for i in range(len(b)):
                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки и классу
def iter_mean_deal_class_nor(data, deal, cls):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for cl in cls:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Class"]).mean().round().Price[de][cl])
                    list_func_area.append(data.groupby(['Deal3', "Class"]).sum().round().Area1[de][cl])
                    list_func_quant.append(data.groupby(['Deal3', "Class"]).count().round().Price[de][cl])
                    b = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки, классу, району
def iter_mean_deal_class_dist_nor(data, deal, cls, dist):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for cl in cls:
                try:
                    for di in dist:
                        try:
                            list_func_price.append(data.groupby(['Deal3', "Class", "Dist1"]).mean().round().Price[de][cl][di])
                            list_func_area.append(data.groupby(['Deal3', "Class", "Dist1"]).sum().round().Area1[de][cl][di])
                            list_func_quant.append(data.groupby(['Deal3', "Class", "Dist1"]).count().round().Price[de][cl][di])
                            b = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "id1"]).groups.keys())
                            c = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot1"]).groups.keys())
                            d = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot2"]).groups.keys())
                            for i in range(len(b)):
                                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                        except:
                            next
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки, классу, району, дате ввода
def iter_mean_deal_class_dist_fin_nor(data, deal, cls, dist, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for cl in cls:
                try:
                    for di in dist:
                        try:
                            for fi in fin:
                                try:
                                    list_func_price.append(data.groupby(['Deal3', "Class", "Dist1", "Date_finish"]).mean().round().Price[de][cl][di][fi])
                                    list_func_area.append(data.groupby(['Deal3', "Class", "Dist1", "Date_finish"]).sum().round().Area1[de][cl][di][fi])
                                    list_func_quant.append(data.groupby(['Deal3', "Class", "Dist1", "Date_finish"]).count().round().Price[de][cl][di][fi])
                                    b = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                                    c = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                                    d = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                                    for i in range(len(b)):
                                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                                except:
                                    next
                        except:
                            next
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по классу, району, дате ввода
def iter_mean_class_dist_fin_nor(data, cls, dist, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for cl in cls:
            for di in dist:
                try:
                    for fi in fin:
                        try:
                            list_func_price.append(data.groupby(["Class", "Dist1", "Date_finish"]).mean().round().Price[cl][di][fi])
                            list_func_area.append(data.groupby(["Class", "Dist1", "Date_finish"]).sum().round().Area1[cl][di][fi])
                            list_func_quant.append(data.groupby(["Class", "Dist1", "Date_finish"]).count().round().Price[cl][di][fi])
                            b = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                            c = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                            d = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                            for i in range(len(b)):
                                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                        except:
                            next
                except:
                    next

        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по классу, району
def iter_mean_class_dist_nor(data, cls, dist):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for cl in cls:
            for di in dist:
                try:
                    list_func_price.append(data.groupby(["Class", "Dist1"]).mean().round().Price[cl][di])
                    list_func_area.append(data.groupby(["Class", "Dist1"]).sum().round().Area1[cl][di])
                    list_func_quant.append(data.groupby(["Class", "Dist1"]).count().round().Price[cl][di])
                    b = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby("Class").get_group(cl).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по классу
def iter_mean_class_nor(data, cls):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for cl in cls:
            list_func_price.append(data.groupby(["Class"]).mean().round().Price[cl])
            list_func_area.append(data.groupby(["Class"]).sum().round().Area1[cl])
            list_func_quant.append(data.groupby(["Class"]).count().round().Price[cl])
            b = list(data.groupby("Class").get_group(cl).groupby(["Project", "id1"]).groups.keys())
            c = list(data.groupby("Class").get_group(cl).groupby(["Project", "Geo_spot1"]).groups.keys())
            d = list(data.groupby("Class").get_group(cl).groupby(["Project", "Geo_spot2"]).groups.keys())
            for i in range(len(b)):
                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по району
def iter_mean_dist_nor(data, dist):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for di in dist:
            list_func_price.append(data.groupby(["Dist1"]).mean().round().Price[di])
            list_func_area.append(data.groupby(["Dist1"]).sum().round().Area1[di])
            list_func_quant.append(data.groupby(["Dist1"]).count().round().Price[di])
            b = list(data.groupby("Dist1").get_group(di).groupby(["Project", "id1"]).groups.keys())
            c = list(data.groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot1"]).groups.keys())
            d = list(data.groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot2"]).groups.keys())
            for i in range(len(b)):
                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по дате ввода
def iter_mean_fin_nor(data,fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for fi in fin:
            list_func_price.append(data.groupby(["Date_finish"]).mean().round().Price[fi])
            list_func_area.append(data.groupby(["Date_finish"]).sum().round().Area1[fi])
            list_func_quant.append(data.groupby(["Date_finish"]).count().round().Price[fi])
            b = list(data.groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
            c = list(data.groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
            d = list(data.groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
            for i in range(len(b)):
                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по дате сделки и дате ввода
def iter_mean_deal_fin_nor(data, deal, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for fi in fin:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Date_finish"]).mean().round().Price[de][fi])
                    list_func_area.append(data.groupby(['Deal3', "Date_finish"]).sum().round().Area1[de][fi])
                    list_func_quant.append(data.groupby(['Deal3', "Date_finish"]).count().round().Price[de][fi])
                    b = list(data.groupby('Deal3').get_group(de).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby('Deal3').get_group(de).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby('Deal3').get_group(de).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки и району
def iter_mean_deal_dist_nor(data, deal, dist):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for di in dist:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Dist1"]).mean().round().Price[de][di])
                    list_func_area.append(data.groupby(['Deal3', "Dist1"]).sum().round().Area1[de][di])
                    list_func_quant.append(data.groupby(['Deal3', "Dist1"]).count().round().Price[de][di])
                    b = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки, району и дате ввода
def iter_mean_deal_dist_fin_nor(data, deal, dist, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for di in dist:
                try:
                    for fi in fin:
                        try:
                            list_func_price.append(data.groupby(['Deal3', "Dist1", "Date_finish"]).mean().round().Price[de][di][fi])
                            list_func_area.append(data.groupby(['Deal3', "Dist1", "Date_finish"]).sum().round().Area1[de][di][fi])
                            list_func_quant.append(data.groupby(['Deal3', "Dist1", "Date_finish"]).count().round().Price[de][di][fi])
                            b = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                            c = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                            d = list(data.groupby('Deal3').get_group(de).groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                            for i in range(len(b)):
                                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                        except:
                            next
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по дате сделки, классу, району
def iter_mean_deal_class_fin_nor(data, deal, cls, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for de in deal:
            for cl in cls:
                try:
                    for fi in fin:
                        try:
                            list_func_price.append(data.groupby(['Deal3', "Class", "Date_finish"]).mean().round().Price[de][cl][fi])
                            list_func_area.append(data.groupby(['Deal3', "Class", "Date_finish"]).sum().round().Area1[de][cl][fi])
                            list_func_quant.append(data.groupby(['Deal3', "Class", "Date_finish"]).count().round().Price[de][cl][fi])
                            b = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                            c = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                            d = list(data.groupby('Deal3').get_group(de).groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                            for i in range(len(b)):
                                result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                        except:
                            next
                except:
                    next
        temp = sum(list_func_area) / len(deal)
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), temp, result
    except:
        return 0

# фильтр по классу и дате ввода
def iter_mean_class_fin_nor(data, cls, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for cl in cls:
            for fi in fin:
                try:
                    list_func_price.append(data.groupby(["Class", "Date_finish"]).mean().round().Price[cl][fi])
                    list_func_area.append(data.groupby(["Class", "Date_finish"]).sum().round().Area1[cl][fi])
                    list_func_quant.append(data.groupby(["Class", "Date_finish"]).count().round().Price[cl][fi])
                    b = list(data.groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby("Class").get_group(cl).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

# фильтр по району и дате ввода
def iter_mean_dist_fin_nor(data, dist, fin):
    try:
        list_func_price = []
        list_func_area = []
        list_func_quant = []
        result = {}
        for di in dist:
            for fi in fin:
                try:
                    list_func_price.append(data.groupby(["Dist1", "Date_finish"]).mean().round().Price[di][fi])
                    list_func_area.append(data.groupby(["Dist1", "Date_finish"]).sum().round().Area1[di][fi])
                    list_func_quant.append(data.groupby(["Dist1", "Date_finish"]).count().round().Price[di][fi])
                    b = list(data.groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "id1"]).groups.keys())
                    c = list(data.groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot1"]).groups.keys())
                    d = list(data.groupby("Dist1").get_group(di).groupby("Date_finish").get_group(fi).groupby(["Project", "Geo_spot2"]).groups.keys())
                    for i in range(len(b)):
                        result[b[i][0]] = [b[i][1], c[i][1], d[i][1]]
                except:
                    next
        return mean([item for item in list_func_price if not(math.isnan(item)) == True]), sum(list_func_area), sum(list_func_quant), result
    except:
        return 0

#/////////////////////////////////////////////////////////////////////////////////
def get_id(data):
    key_code = list(data.groupby(['Project', "id1"]).id1)
    key_class = list(data.groupby('Project').groups.keys())
    key_geo1 = list(data.groupby(['Project', "Geo_spot1"]).Geo_spot1)
    key_geo2 = list(data.groupby(['Project', "Geo_spot2"]).Geo_spot2)
    result = {}
    for i in range(len(key_class)):
       result[key_class[i]] = [list(set(key_code[i][1]))[0], list(set(key_geo1[i][1]))[0], list(set(key_geo2[i][1]))[0]]
    return result



#/////////////////////////////////////////////////////////////////////////////////

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
            price_group.append(round(data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Price.mean()))
        if pd.isnull(b):
            area_group.append(0)
        else:
            area_group.append(round(data.groupby("id1").get_group(id).groupby("Deal3").get_group(element).Area1.sum()))
    return data_grp, price_group, area_group

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main_chart(data, fin, cls, dist):
    deal = ["2020 4кв." ,"2021 1кв.", "2021 2кв.", "2021 3кв.", "2021 4кв."]
    list_func_price = []
    list_func_area = []
    res_price = []
    res_area = []
    if len(fin) == 0 and len(cls) == 0 and len(dist) == 0:
        for de in deal:
            try:
                list_func_price.append(data.groupby(['Deal3']).mean().round().Price[de])
                list_func_area.append(data.groupby(['Deal3']).sum().round().Area1[de])
            except:
                next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) != 0 and len(cls) == 0 and len(dist) == 0:
        for de in deal:
            for fi in fin:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Date_finish"]).mean().round().Price[de][fi])
                    list_func_area.append(data.groupby(['Deal3', "Date_finish"]).sum().round().Area1[de][fi])
                except:
                    next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) == 0 and len(cls) != 0 and len(dist) == 0:
        for de in deal:
            for cl in cls:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Class"]).mean().round().Price[de][cl])
                    list_func_area.append(data.groupby(['Deal3', "Class"]).sum().round().Area1[de][cl])
                except:
                    next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) == 0 and len(cls) == 0 and len(dist) != 0:
        for de in deal:
            for di in dist:
                try:
                    list_func_price.append(data.groupby(['Deal3', "Dist1"]).mean().round().Price[de][di])
                    list_func_area.append(data.groupby(['Deal3', "Dist1"]).sum().round().Area1[de][di])
                except:
                    next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) != 0 and len(cls) != 0 and len(dist) == 0:
        for de in deal:
            for fi in fin:
                for cl in cls:
                    try:
                        list_func_price.append(data.groupby(['Deal3', "Date_finish", "Class"]).mean().round().Price[de][fi][cl])
                        list_func_area.append(data.groupby(['Deal3', "Date_finish", "Class"]).sum().round().Area1[de][fi][cl])
                    except:
                        next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) == 0 and len(cls) != 0 and len(dist) != 0:
        for de in deal:
            for cl in cls:
                for di in dist:
                    try:
                        list_func_price.append(data.groupby(['Deal3', "Class", "Dist1"]).mean().round().Price[de][cl][di])
                        list_func_area.append(data.groupby(['Deal3', "Class", "Dist1"]).sum().round().Area1[de][cl][di])
                    except:
                        next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) != 0 and len(cls) == 0 and len(dist) != 0:
        for de in deal:
            for fi in fin:
                for di in dist:
                    try:
                        list_func_price.append(data.groupby(['Deal3', "Date_finish", "Dist1"]).mean().round().Price[de][fi][di])
                        list_func_area.append(data.groupby(['Deal3', "Date_finish", "Dist1"]).sum().round().Area1[de][fi][di])
                    except:
                        next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    elif len(fin) != 0 and len(cls) != 0 and len(dist) != 0:
        for de in deal:
            for fi in fin:
                for di in dist:
                    for cl in cls:
                        try:
                            list_func_price.append(data.groupby(['Deal3', "Date_finish", "Dist1", "Class"]).mean().round().Price[de][fi][di][cl])
                            list_func_area.append(data.groupby(['Deal3', "Date_finish", "Dist1", "Class"]).sum().round().Area1[de][fi][di][cl])
                        except:
                            next
            res_price.append(round(mean([item for item in list_func_price if not(math.isnan(item)) == True])))
            res_area.append(round(sum([item for item in list_func_area if not (math.isnan(item)) == True])))
            list_func_price = []
            list_func_area = []
    return (res_price, res_area)