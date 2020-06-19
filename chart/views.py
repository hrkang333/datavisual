from django.shortcuts import render
from .models import Passenger, Confirmed, Deaths, Recovered
from django.db.models import Count, Q
import json  # ***json 임포트 추가***

def home(request):  #메인
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    # 빈 리스트 4종 준비 (series 이름 뒤에 '_data' 추가)
    categories = list()                 # for xAxis
    survived_series_data = list()       # for series named 'Survived'
    not_survived_series_data = list()   # for series named 'Not survived'
    survival_rate = list()    # for series named 'Survival rate'

    # 리스트 4종에 형식화된 값을 등록
    for entry in dataset:
        categories.append('%s 등석' % entry['ticket_class'])         # for xAxis
        survived_series_data.append(entry['survived_count'])          # for series named 'Survived'
        not_survived_series_data.append(entry['not_survived_count'])  # for series named 'Not survived'
        survival_rate.append(entry['survived_count'] \
      / (entry['survived_count']+entry['not_survived_count'])*100)  # for series named 'Survival rate'


    survived_series = {
        'name': '생존',
        'data': survived_series_data,
        'tooltip' : {"valueSuffix": "명"},
        'yAxis': 1,
        'color': 'green'
    }
    not_survived_series = {
        'name': '비생존',
        'data': not_survived_series_data,
        'tooltip': {"valueSuffix": "명"},
        'yAxis': 1,
        'color': 'red'
    }
    survival_rate = {
        'name': '생존율',
        'type': 'spline',
        'data': survival_rate,
        'tooltip': {"valueSuffix": "%"},
        'color': 'skyblue'
            }
    chart = {
        'chart': {'type': 'column'},
        'title': {"text": "좌석 등급에 따른 타이타닉 생존/비생존 인원 및 생존율"},
        'xAxis': {'categories':categories},
        'yAxis': [{"labels": {"format": "{value} %", "style": {"color": "blue"}},
                   "title": {"text": "생존율", "style": {"color": "blue"}}},

                  {"labels": {"format": "{value} 명", "style": {"color": "black"}},
                   "title": {"text": "인원", "style": {"color": "black"}}, "opposite": "true"}],

        'tooltip': {"shared": "true"},

        'legend': {"layout": "vertical", "align": "left", "x": 120,
                   "verticalAlign": "top", "y": 100, "floating": "true"},

        'series': [survived_series, not_survived_series, survival_rate]
    }
    dump = json.dumps(chart)

    return render(request, 'home.html', {'chart': dump})







def con_19(request):    #확진자
    dataset = Confirmed.objects \
        .values('Date', 'France','Germany','Korea_South','US','United_Kingdom') \
        .order_by('Date')

# 빈 리스트 6종 준비 (series 이름 뒤에 '_data' 추가)
    Date = list()                 # for xAxis
    France_series_data = list()       # for series named 'France'
    Germany_series_data = list()   # for series named 'Germany'
    Korea_South_series_data = list()   # for series named 'Korea_South'
    US_series_data = list()   # for series named 'US'
    United_Kingdom_series_data = list()   # for series named 'United_Kingdom'


 # 리스트 6종에 형식화된 값을 등록
    for entry in dataset:
        Date.append(entry['Date'])         # for xAxis


        France_series_data.append(entry['France'])          # for series named 'France'

        Germany_series_data.append(entry['Germany'])          # for series named 'Germany'

        Korea_South_series_data.append(entry['Korea_South'])          # for series named 'Korea_South'

        US_series_data.append(entry['US'])          # for series named 'US'

        United_Kingdom_series_data.append(entry['United_Kingdom'])          # for series named 'United_Kingdom'


    France_series = {
        'name': 'France',
        'data': France_series_data,
        #'pointInterval': 24 * 3600 * 1200,
        'color': '#47C83E'
    }
    Germany_series = {
        'name': 'Germany',
        'data': Germany_series_data,
        #'pointInterval': 24 * 3600 * 1200,
        'color': '#F2CB61'
    }
    Korea_South_series = {
        'name': 'Korea_South',
        'data': Korea_South_series_data,
        #'pointInterval': 24 * 3600 * 1200,
        'color': '#6866FF'
    }
    US_series = {
        'name': 'US',
        'data': US_series_data,
        #'pointInterval': 24 * 3600 * 1200,
        'color': '#DC3977'
    }
    United_Kingdom_series = {
        'name': 'United_Kingdom',
        'data': United_Kingdom_series_data,
        #'pointInterval': 24 * 3600 * 1200,
        'color': '#7C1D6F'
    }


    chart = {
        'chart': {"type": "spline", "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {"text": "국가별 covid-19 확진자"},
        'subtitle': {"text": "For the France, Germany, Korea South, US, United Kingdom"},
        'xAxis': {"type": "datetime"},
        #'xAxis': {"type": "datetime", 'labels': {'dateTimeLabelFormats': {'month': '%e. %b'}}},
        'yAxis': [{"labels": {"format": "{value} 건/백만 명", "style": {"color": "blue"}},
                    "title": {"text": "합계 건수", "style": {"color": "blue"}}}],
        "plotOptions": {"spline": {"lineWidth": 3, "states": {"hover": {"lineWidth": 5}}}},

        'series': [France_series, Germany_series, Korea_South_series, US_series, United_Kingdom_series]
    }
    dump = json.dumps(chart)

    return render(request, 'con_19.html', {'chart': dump})


def dth_19(request):    #사망자
    dataset = Deaths.objects \
        .values('Date','France','Germany','Korea_South','US','United_Kingdom') \
        .order_by('Date')

# 빈 리스트 6종 준비 (series 이름 뒤에 '_data' 추가)
    Date = list()                 # for xAxis
    France_series_data = list()       # for series named 'France'
    Germany_series_data = list()   # for series named 'Germany'
    Korea_South_series_data = list()   # for series named 'Korea_South'
    US_series_data = list()   # for series named 'US'
    United_Kingdom_series_data = list()   # for series named 'United_Kingdom'


    # 리스트 6종에 형식화된 값을 등록
    for entry in dataset:
        Date.append(entry['Date'])         # for xAxis


        France_series_data.append(entry['France'])          # for series named 'France'

        Germany_series_data.append(entry['Germany'])          # for series named 'Germany'

        Korea_South_series_data.append(entry['Korea_South'])          # for series named 'Korea_South'

        US_series_data.append(entry['US'])          # for series named 'US'

        United_Kingdom_series_data.append(entry['United_Kingdom'])          # for series named 'United_Kingdom'


    France_series = {
        'name': 'France',
        'data': France_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#47C83E'
    }
    Germany_series = {
        'name': 'Germany',
        'data': Germany_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#F2CB61'
    }
    Korea_South_series = {
        'name': 'Korea_South',
        'data': Korea_South_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#6866FF'
    }
    US_series = {
        'name': 'US',
        'data': US_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#DC3977'
    }
    United_Kingdom_series = {
        'name': 'United_Kingdom',
        'data': United_Kingdom_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#7C1D6F'
    }


    chart = {
        'chart': {"type": "spline", "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {"text": "국가별 covid-19 사망자"},
        'subtitle': {"text": "For the France, Germany, Korea South, US, United Kingdom"},
        'xAxis': {"type": "datetime", 'labels': {'dateTimeLabelFormats': {'month': '%e. %b'}}},
   #date = arrow.get(date.year, date.month, date.day).timestamp * 1000
        # Date = arrow.get(Date.year, Date.month, Date.day).timestamp * 1000
        'yAxis': [{"labels": {"format": "{value} 건/백만 명", "style": {"color": "blue"}},
                   "title": {"text": "합계 건수", "style": {"color": "blue"}}}],
        "plotOptions": {"spline": {"lineWidth": 3, "states": {"hover": {"lineWidth": 5}}}},

        'series': [France_series, Germany_series, Korea_South_series, US_series, United_Kingdom_series]
    }
    dump = json.dumps(chart)

    return render(request, 'dth_19.html', {'chart': dump})


def rec_19(request):    #회복자
    dataset = Recovered.objects \
        .values('Date','France','Germany','Korea_South','US','United_Kingdom') \
        .order_by('Date')

# 빈 리스트 6종 준비 (series 이름 뒤에 '_data' 추가)
    Date = list()                 # for xAxis
    France_series_data = list()       # for series named 'France'
    Germany_series_data = list()   # for series named 'Germany'
    Korea_South_series_data = list()   # for series named 'Korea_South'
    US_series_data = list()   # for series named 'US'
    United_Kingdom_series_data = list()   # for series named 'United_Kingdom'


    # 리스트 6종에 형식화된 값을 등록
    for entry in dataset:
        Date.append(entry['Date'])         # for xAxis


        France_series_data.append(entry['France'])          # for series named 'France'

        Germany_series_data.append(entry['Germany'])          # for series named 'Germany'

        Korea_South_series_data.append(entry['Korea_South'])          # for series named 'Korea_South'

        US_series_data.append(entry['US'])          # for series named 'US'

        United_Kingdom_series_data.append(entry['United_Kingdom'])          # for series named 'United_Kingdom'


    France_series = {
        'name': 'France',
        'data': France_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#47C83E'
    }
    Germany_series = {
        'name': 'Germany',
        'data': Germany_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#F2CB61'
    }
    Korea_South_series = {
        'name': 'Korea_South',
        'data': Korea_South_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#6866FF'
    }
    US_series = {
        'name': 'US',
        'data': US_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#DC3977'
    }
    United_Kingdom_series = {
        'name': 'United_Kingdom',
        'data': United_Kingdom_series_data,
        'pointInterval': 24 * 3600 * 1200,
        'color': '#7C1D6F'
    }


    chart = {
        'chart': {"type": "spline", "borderColor": "#9DB0AC", "borderWidth": 3},
        'title': {"text": "국가별 covid-19 회복자"},
        'subtitle': {"text": "For the France, Germany, Korea South, US, United Kingdom"},
        'xAxis': {"type": "datetime", 'labels': {'dateTimeLabelFormats': {'month': '%e. %b'}}},
   #date = arrow.get(date.year, date.month, date.day).timestamp * 1000
        # Date = arrow.get(Date.year, Date.month, Date.day).timestamp * 1000
        'yAxis': [{"labels": {"format": "{value} 건/백만 명", "style": {"color": "blue"}},
                   "title": {"text": "합계 건수", "style": {"color": "blue"}}}],
        "plotOptions": {"spline": {"lineWidth": 3, "states": {"hover": {"lineWidth": 5}}}},

        'series': [France_series, Germany_series, Korea_South_series, US_series, United_Kingdom_series]
    }
    dump = json.dumps(chart)

    return render(request, 'rec_19.html', {'chart': dump})



def ticket_class_view_3(request):  # 방법 3
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    # 빈 리스트 4종 준비 (series 이름 뒤에 '_data' 추가)
    categories = list()                 # for xAxis
    survived_series_data = list()       # for series named 'Survived'
    not_survived_series_data = list()   # for series named 'Not survived'
    survival_rate = list()    # for series named 'Survival rate'

    # 리스트 4종에 형식화된 값을 등록
    for entry in dataset:
        categories.append('%s 등석' % entry['ticket_class'])         # for xAxis
        survived_series_data.append(entry['survived_count'])          # for series named 'Survived'
        not_survived_series_data.append(entry['not_survived_count'])  # for series named 'Not survived'
        survival_rate.append(entry['survived_count'] \
      / (entry['survived_count']+entry['not_survived_count'])*100)  # for series named 'Survival rate'


    survived_series = {
        'name': '생존',
        'data': survived_series_data,
        'tooltip' : {"valueSuffix": "명"},
        'yAxis': 1,
        'color': 'green'
    }
    not_survived_series = {
        'name': '비생존',
        'data': not_survived_series_data,
        'tooltip': {"valueSuffix": "명"},
        'yAxis': 1,
        'color': 'red'
    }
    survival_rate = {
        'name': '생존율',
        'type': 'spline',
        'data': survival_rate,
        'tooltip': {"valueSuffix": "%"},
        'color': 'skyblue'
            }
    chart = {
        'chart': {'type': 'column'},
        'title': {"text": "좌석 등급에 따른 타이타닉 생존/비생존 인원 및 생존율"},
        'xAxis': {'categories':categories},
        'yAxis': [{"labels": {"format": "{value} %", "style": {"color": "blue"}},
                   "title": {"text": "생존율", "style": {"color": "blue"}}},

                  {"labels": {"format": "{value} 명", "style": {"color": "black"}},
                   "title": {"text": "인원", "style": {"color": "black"}}, "opposite": "true"}],

        'tooltip': {"shared": "true"},

        'legend': {"layout": "vertical", "align": "left", "x": 120,
                   "verticalAlign": "top", "y": 100, "floating": "true"},

        'series': [survived_series, not_survived_series, survival_rate]
    }
    dump = json.dumps(chart)

    return render(request, 'ticket_class_3.html', {'chart': dump})