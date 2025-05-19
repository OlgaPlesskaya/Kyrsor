from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView , CreateView

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
import string
import re
import numpy as np
from ast import literal_eval
from django.views.decorators.csrf import csrf_protect
from yandex_geocoder import Client
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django import forms
# Create your views here.
from .models import Vuz_1
from .models import Comments
from .models import Comments_2
from decimal import Decimal
from .models import Programms
from .models import Dormitory
from .models import University_buildings
import requests
from geopy.distance import geodesic
from django.contrib import messages
from datetime import datetime, timedelta
from .forms import CommentsForm
from django.http import JsonResponse
from django.db.models import Q

# def index(request):
#     tasks = Vuzzz.objects.all()
#     return render(request, 'main/index_bootstrap.html',{'name':'Название вуза','tasks':tasks})
#
# def vuz_bootstrap(request):
#     return render(request, 'main/vuz_bootstrap.html')
#
# def otz_bootstrap(request):
#     return render(request, 'main/otz_bootstrap.html')
#
# def vuz_otz_bootstrap(request):
#     return render(request, 'main/vuz_otz_bootstrap.html')

class VuzView(ListView):
    # paginate_by = 10
    model = Vuz_1
    context_object_name = 'vuz_1_list'
    paginate_by = 10


    # def get_template_names(self):
    #
    #     if self.request.path == '':
    #
    #         return ['main/vuz_1_list.html']
    #     elif self.request.path == '/page_2/':
    #         return ['main/otz_bootstrap.html']
    #     else:
    #         return super().get_template_names()

def get_vuz_options(request):
    query = request.GET.get('query')
    vuz_list = Vuz_1.objects.filter(Q(name__icontains=query) | Q(short_name__icontains=query))
    options = [{'value': vuz.pk, 'text': vuz.name} for vuz in vuz_list]
    return JsonResponse(options, safe=False)

def comments(request):
    vuz_list = Vuz_1.objects.all()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CommentsForm()
    comments = Comments_2.objects.all()
    context = {
        'form': form,
        'comments': comments,
        'vuz_list': vuz_list,
    }
    return render(request, 'main/otz_bootstrap.html', context)

def otz_bootstrap(request):
    return render(request, 'main/otz_bootstrap_1.html')

class VuzDetailView(DetailView):
    model = Vuz_1
    slug_field = "id"
    template_name = 'main/vuz_1_detail.html'
    context_object_name = 'vuz_1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_vus'] = Vuz_1.objects.all()
        context['another_template'] = 'vuz_1_detail_1.html'
        context['another_template_1'] = 'vuz_1_detail_2.html'
        context['another_template_2'] = 'vuz_1_detail_2_1.html'

        comments = self.object.comments_set.all()

        comments_2 = self.object.comments_2_set.all()

        prog = self.object.programms_set.all()

        dom = self.object.dormitory_set.all()

        buil = self.object.university_buildings_set.all()

        one_rait_comments = comments.filter(rait=1)
        zero_rait_comments = comments.filter(rait=0)
        two_rait_comments = comments.filter(rait=2)

        one_rait_comments_1 = comments_2.filter(rait__range=(4, 7))
        zero_rait_comments_1 = comments_2.filter(rait__range=(0, 2))
        two_rait_comments_1 = comments_2.filter(rait__range=(8, 10))

        filter_value_1 = self.request.GET.get('filter_1', None)
        if filter_value_1 == '2':
            print('2')
            comments_3 = comments_2.filter(rait__range=(8, 11))
        elif filter_value_1 == '0':
            print('0')
            comments_3 = comments_2.filter(rait__range=(-1, 4))
        elif filter_value_1 == '1':
            print('1')
            comments_3 = comments_2.filter(rait__range=(4, 7))
        elif filter_value_1 == '4':
            comments_3 = comments_2.order_by('-date')
        else:
            print('all')
            comments_3 = self.object.comments_2_set.all()




        filter_value = self.request.GET.get('filter', None)
        if filter_value== '2':
            print('2')
            comments_1 = comments.filter(rait=2)
        elif filter_value== '0':
            print('0')
            comments_1 = comments.filter(rait=0)
        elif filter_value== '1':
            print('1')
            comments_1 = comments.filter(rait=1)
        else:
            print('all')
            comments_1 = self.object.comments_set.all()

        context['filter_value_1'] = filter_value_1
        context['filter_value'] = filter_value

        context['one_rait_comments'] = one_rait_comments
        context['two_rait_comments'] = two_rait_comments
        context['zero_rait_comments'] = zero_rait_comments

        context['one_rait_comments_1'] = one_rait_comments_1
        context['two_rait_comments_1'] = two_rait_comments_1
        context['zero_rait_comments_1'] = zero_rait_comments_1

        context['comments'] = comments
        context['prog'] = prog
        context['dom'] = dom
        context['buil'] = buil
        context['comments_1'] = comments_1
        context['comments_2'] = comments_2
        context['comments_3'] = comments_3


        # paginator = Paginator(comments_3, 4)  # показывать 3 комментариев на странице
        # # добавляем URL-адрес со ссылкой на страницу отзывов
        #
        # page_number = self.request.GET.get('page', 1)
        # page = paginator.get_page(page_number)
        # context['comments_3'] = page


        queryset = super().get_queryset()

        api_key = '1378cdde-b790-4327-9442-39ce536a4341'




        # for vuz_1 in queryset:
        #     address = f"{vuz_1.metro_name}"
        #     # latitude = f"{vuz_1.latitude}"
        #     # longitude = f"{vuz_1.longitude}"
        # #     print(address)
        #
            # start_point = f"{vuz_1.latitude},{vuz_1.longitude}"  # координаты начальной точки
            # end_point = f"{vuz_1.metro_latitude},{vuz_1.metro_longitude}"  # координаты конечной точки
            # distanse_km = geodesic(start_point, end_point).kilometers
            # print(distanse_km)
            # vuz_1.distance_to_metro = round(distanse_km,2)
            # vuz_1.save()






        #     url = f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address}&format=json'
        # #
        # #     url = f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={longitude},{latitude}&kind=metro&results=1&format=json'
        #     response = requests.get(url).json()
        # #
        # #
        # #     components = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
        # #     for component in components:
        # #         if component['kind'] == 'metro':
        # #             metro_station = component['name']
        # #             break
        # #
        # #     print(metro_station)
        # #     vuz_1.metro_name = metro_station
        # #     vuz_1.save()
        # #     # Извлекаем координаты из ответа
        #     longitude, latitude = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
        #         'pos'].split()
        #
        #     # Сохраняем координаты в переменную coordinates
        #     coordinates = float(latitude), float(longitude)
        # #     vuz_1.coordinates = coordinates
        # #     print(coordinates)
        # #     vuz_1.save()
        #     vuz_1.metro_latitude = float(latitude)
        #     vuz_1.save()
        #     vuz_1.metro_longitude = float(longitude)
        #     vuz_1.save()
        return context

def get_dom(request):
    dom = Dormitory.objects.all() # получаем все объекты модели
    data = [] # создаем пустой список для хранения данных

    for d in dom:
        data.append({
            'name': d.name,
            'description': d.description,
            # добавляем другие поля модели, если нужно
        })

    return JsonResponse({'data': data}) # возвращаем данные в формате JSON




# class VusView(ListView):
#     paginate_by = 10
#     model = Vuz_1
#     queryset = Vuz_1.objects.all()
#     context_object_name = 'vuz_1_list'
#     # ordering = ['-distance_from_dormitory']
#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     ordering = self.request.GET.get('ordering', '-distance_from_dormitory')
#     #     return queryset.order_by(ordering)
#
# class VusDetailView(DetailView):
#     model = Vuz_1
#     slug_field = "id"
#     template_name = 'vuz_1_detail.html'  # указываем шаблон для отображения объекта модели
#     context_object_name = 'vuz_1'  # имя переменной, которую мы будем использовать в шаблоне
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['related_vus'] = Vuz_1.objects.all()
#         context['another_template'] = 'vuz_1_detail_1.html'  # добавляем другой шаблон для отображения
#         return context

    # def get_template_names(self):
    #     template_name = 'vuz_1_detail'
    #     if self.kwargs.get('template_name') == 'vuz_1_detail_1':
    #         template_name = 'vuz_1_detail_1'
    #     return [template_name]



# class FilterVusView(ListView):
#     paginate_by = 10
#     def get_queryset(self):
#         return Vuz_1.objects.all().order_by('distance_between_buildings')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         sort = self.request.GET.get('sort', 'distance')
#         context['sort'] = sort
#         return context

class Search(ListView):
    paginate_by = 10
    def get_queryset(self):
        return Vuz_1.objects.filter(
            Q(name__iregex= self.request.GET.get("q")) |
            Q(short_name__iregex=self.request.GET.get("q"))
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        if not context["object_list"]:
            context["message"] = "Ой, введеного вами ВУЗа нет в нашей базе"
        return context

# class distance:
#     """Расстояние от вуза до метро"""
#     def get_distance_from_metro(self):
#         return Vuz_1.objects.all().values("distance_from_metro")
#
#     def get_distance_from_dormitory(self):
#         return Vuz_1.objects.all().values("distance_from_dormitory")
#
#     def get_distance_between_buildings(self):
#         return Vuz_1.objects.all().values("distance_between_buildings")

# _____________________________________________________________________________
# Подключение нейронки
# _____________________________________________________________________________

max_len = 52


model = load_model('learning_10_2023.h5')

with open('dict.txt', encoding='cp1251') as filehandler:
    content = filehandler.read()
    vocab_dict = literal_eval(content)
    vocab = [word for word, _ in sorted(vocab_dict.items(), key=lambda x: x[1])]

word2idx = {word: idx + 1 for idx, word in enumerate(vocab)}

def preprocess_text(text):
    if not isinstance(text, str):
        return []

        # Замена ссылок на 'URL'
        text = re.sub(r'http\S+', ' url ', text)
        # Удаление знаков препинания и замена на пробелы
        text = remove_punctuation(text)
        # Приведение к нижнему регистру
        text = text.lower()
        # Удаление смайликов
        text = re.sub(r'[^\w\s]|_', ' ', text)
        # Замена буквы 'ё' на 'е'
        text = text.replace('ё', 'е')
        # Удаление цифр
        text = re.sub(r'\d', ' ', text)
    words = text.split()
    return words

def preprocess_new_text(text):
    words = preprocess_text(text)
    seq = [word2idx.get(word, 0) for word in words]
    seq = np.array(seq).reshape(1, -1)
    seq = pad_sequences(seq, maxlen=max_len, padding='post')
    return seq




@csrf_protect
def neural_network_form(request):
    return render(request, 'main/otz_bootstrap.html')

@csrf_protect
def neural_network_process(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputText', '')
        new_text_seq = preprocess_new_text(input_text)
        prediction = model.predict(new_text_seq)
        sentiment = np.argmax(prediction)

        if sentiment == 0:
            result = 'Negative'
        elif sentiment == 1:
            result = 'Neutral'
        else:
            result = 'Positive'

        # Расчет количества отзывов каждой категории
        negative_count = len([s for s in prediction if np.argmax(s) == 0])
        neutral_count = len([s for s in prediction if np.argmax(s) == 1])
        positive_count = len([s for s in prediction if np.argmax(s) == 2])

        # Вычисление максимального значения для графика
        max_count = max(negative_count, neutral_count, positive_count)
        print('jr')
        return render(request, 'main/otz_bootstrap.html', {
            'result': result,
            'negative_count': negative_count,
            'neutral_count': neutral_count,
            'positive_count': positive_count,
            'max_count': max_count
        })
    else:
        return render(request, 'main/otz_bootstrap.html')









# class VusDetailView(View):
#     def get(self,request,pk):
#         vuz = Vuz_1.objects.get(id=pk)
#         return render(request, 'main/vuz_bootstrap.html', {'vuz': vuz})

# class VusView(View):
#     def get(self,request):
#         vuzs = Vuz_1.objects.all()
#         return render(request, 'main/index_bootstrap.html',{'vuz_list':vuzs})

# class FilterVusView(distance,ListView):
    # """Фильтр вузов"""
    # def get_queryset(self):
    #     queryset = Vuz_1.objects.filter(
    #         # distance_from_metro__in = self.request.GET.getlist("distance_from_metro"),
    #         # distance_from_dormitory__in = self.request.GET.getlist("distance_from_dormitory")
    #     )
    #     return queryset


