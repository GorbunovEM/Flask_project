from function import *
from charts import Charts
from methods import Methods


class Web_page:


    def __init__(self, data):
        self.data = data
        self.finish_grp = self.data.groupby('Date_finish').groups
        self.deal_grp = self.data.groupby('Deal3').groups
        self.room_grp = self.data.groupby('Room').mean()
        self.key_class = id_and_geo(self.data)
        self.key_finish = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029","2030"]
        self.key_deal = list(self.deal_grp.keys())
        self.all_flat = format_data(self.data.Price.mean().round())
        try:
            self.oneflat = format_data(self.room_grp.Price[1])
        except:
            self.oneflat = 0
        try:
            self.twoflat = format_data(self.room_grp.Price[2])
        except:
            self.twoflat = 0
        try:
            self.threeflat = format_data(self.room_grp.Price[3])
        except:
            self.threeflat = 0
        try:
            self.fourflat = format_data(self.room_grp.Price[4])
        except:
            self.fourflat = 0
        try:
            self.stflat = format_data(self.room_grp.Price[0])
        except:
            self.stflat = 0
        self.area_flat = format_data(self.data.Area1.sum().round())
        self.qunt_flat = format_data(self.data.id2.count().round())
        self.temp_flat = format_data(self.data.Area1.sum().round() / len(self.key_deal))



    def form_dict(self):
        template_context = dict(all_flat=self.all_flat,
                                oneflat=self.oneflat,
                                twoflat=self.twoflat,
                                threeflat=self.threeflat,
                                fourflat=self.fourflat,
                                stflat=self.stflat,
                                area_flat=self.area_flat,
                                qunt_flat=self.qunt_flat,
                                temp_flat=self.temp_flat,
                                key_class=self.key_class,
                                key_finish=self.key_finish,
                                values1=Charts.main_chart(self.data, {})[0],
                                values2=Charts.main_chart(self.data, {})[1])
        return template_context

    def refresh_page(self, out):

        flat = Methods

        template_context = dict(all_flat=format_data(float(flat.find_mean_price(self.data, out)[1])),
                                oneflat=format_data(float(flat.find_mean_price(self.data, out, 1)[0])),
                                twoflat=format_data(float(flat.find_mean_price(self.data, out, 2)[0])),
                                threeflat=format_data(float(flat.find_mean_price(self.data, out, 3)[0])),
                                fourflat=format_data(float(flat.find_mean_price(self.data, out, 4)[0])),
                                stflat=format_data(float(flat.find_mean_price(self.data, out, 0)[0])),
                                area_flat=format_data(float(flat.filter_data(self.data, out)[0])),
                                qunt_flat=format_data(float(flat.filter_data(self.data, out)[1])),
                                temp_flat=format_data(float(flat.filter_data(self.data, out)[2])),
                                key_class=flat.filter_data(self.data, out)[3],
                                key_finish=self.key_finish,
                                values1=Charts.main_chart(self.data, out)[0],
                                values2=Charts.main_chart(self.data, out)[1])

        return template_context


    def second_page(self, id_project):

        chart = Charts

        legend = 'Кварталы'
        labels = chart.charts(id_project, self.data)[0]
        values1 = chart.charts(id_project, self.data)[2]
        values2 = chart.charts(id_project, self.data)[1]

        room_grp = self.data.groupby('id1').get_group(id_project).groupby("Room").Price.mean().round()
        key_deal = len(labels)

        try:
            all_flat = format_data(self.data.groupby('id1').get_group(id_project).Price.mean())
        except:
            all_flat = 0
        try:
            oneflat = format_data(room_grp[1])
        except:
            oneflat = 0
        try:
            twoflat = format_data(room_grp[2])
        except:
            twoflat = 0
        try:
            threeflat = format_data(room_grp[3])
        except:
            threeflat = 0
        try:
            fourflat = format_data(room_grp[4])
        except:
            fourflat = 0
        try:
            stflat = format_data(room_grp[0])
        except:
            stflat = 0

        area_flat = format_data(self.data.groupby('id1').get_group(id_project).Area1.sum().round())
        qunt_flat = format_data(self.data.groupby('id1').get_group(id_project).Area1.count().round())
        temp_flat = format_data(self.data.groupby('id1').get_group(id_project).Area1.sum().round() / key_deal)

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
        return template_context