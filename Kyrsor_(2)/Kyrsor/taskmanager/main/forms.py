from django import forms
from .models import Comments_2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
import string
import re
import numpy as np
from ast import literal_eval



class CommentsForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].empty_label = 'ВУЗ не выбран'


        self.fields['text_1'].widget.attrs.update({'class': 'form-control_1', 'id': 'inputText', 'name': 'inputText'})  # добавляем атрибут name
        self.fields['text_1'].widget.attrs.update({'class': 'form-control_2', 'id': 'inputText', 'name': 'inputText'})  # добавляем атрибут name
        self.fields['text_3'].widget.attrs.update({'class': 'form-control_3', 'id': 'inputText', 'name': 'inputText'})  # добавляем атрибут name
        self.fields['text_4'].widget.attrs.update({'class': 'form-control_4', 'id': 'inputText', 'name': 'inputText'})  # добавляем атрибут name
        self.fields['text_5'].widget.attrs.update({'class': 'form-control_5', 'id': 'inputText', 'name': 'inputText'})  # добавляем атрибут name

        self.fields['text_1'].empty_label = 'ВУЗ не выбран'
        self.fields['text_2'].empty_label = 'ВУЗ не выбран'
        self.fields['text_4'].empty_label = 'ВУЗ не выбран'
        self.fields['text_5'].empty_label = 'ВУЗ не выбран'
        self.fields['text_4'].empty_label = 'ВУЗ не выбран'

    class Meta:
        model = Comments_2
        fields = ['name', 'text_1', 'rait_1', 'text_2', 'rait_2', 'text_3', 'rait_3', 'text_4', 'rait_4', 'text_5', 'rait_6','rait']
        labels = {
            'name': 'Название ВУЗа',
            'text_1': 'Текст отзыва',
            'text_2': 'Текст отзыва',
            'text_3': 'Текст отзыва',
            'text_4': 'Текст отзыва',
            'text_5': 'Текст отзыва',
        }
        # exclude = ['rait']

    def clean(self):

        cleaned_data = super().clean()

        input_text_1 = cleaned_data.get('text_1')
        if not input_text_1:
            cleaned_data['rait_1'] = 1
        # Если поле text_1 пустое, выполнить какие-то действия
        else:
        # Если поле text_1 не пустое, выполнить другие действия
            print(cleaned_data['text_1'])
            print(cleaned_data['rait_1'])
            new_text_seq_1 = preprocess_new_text(input_text_1)
            prediction_1 = model.predict(new_text_seq_1)
            sentiment_1 = np.argmax(prediction_1)
            print(sentiment_1)
            cleaned_data['rait_1'] = sentiment_1  # добавляем значение sentiment в поле rait формы

        input_text_2 = cleaned_data.get('text_2')
        if not input_text_2:
            cleaned_data['rait_2'] = 1
        else:
            print(cleaned_data['text_2'])
            print(cleaned_data['rait_2'])
            new_text_seq_2 = preprocess_new_text(input_text_2)
            prediction_2 = model.predict(new_text_seq_2)
            sentiment_2 = np.argmax(prediction_2)
            print(sentiment_2)
            cleaned_data['rait_2'] = sentiment_2  # добавляем значение sentiment в поле rait формы

        input_text_3 = cleaned_data.get('text_3')
        if not input_text_3:
            cleaned_data['rait_3'] = 1
        else:
            print(cleaned_data['text_3'])
            print(cleaned_data['rait_3'])
            new_text_seq_3 = preprocess_new_text(input_text_3)
            prediction_3 = model.predict(new_text_seq_3)
            sentiment_3 = np.argmax(prediction_3)
            print(sentiment_3)
            cleaned_data['rait_3'] = sentiment_3  # добавляем значение sentiment в поле rait формы

        input_text_4 = cleaned_data.get('text_4')

        if not input_text_4:
            cleaned_data['rait_4'] = 1
        else:
            print(cleaned_data['text_4'])
            print(cleaned_data['rait_4'])
            new_text_seq_4 = preprocess_new_text(input_text_4)
            prediction_4 = model.predict(new_text_seq_4)
            sentiment_4 = np.argmax(prediction_4)
            print(sentiment_4)
            cleaned_data['rait_4'] = sentiment_4  # добавляем значение sentiment в поле rait формы

        input_text_5 = cleaned_data.get('text_5')
        if not input_text_5:
            cleaned_data['rait_6'] = 1
        else:
            print(cleaned_data['text_5'])
            print(cleaned_data['rait_6'])
            new_text_seq_5 = preprocess_new_text(input_text_5)
            prediction_5 = model.predict(new_text_seq_5)
            sentiment_5 = np.argmax(prediction_5)
            print(sentiment_5)
            cleaned_data['rait_6'] = sentiment_5  # добавляем значение sentiment в поле rait формы

        sentiment = cleaned_data['rait_1'] + cleaned_data['rait_2'] + cleaned_data['rait_3'] + cleaned_data['rait_4'] + cleaned_data['rait_6']
        print(sentiment)
        cleaned_data['rait'] = sentiment  # добавляем значение sentiment в поле rait формы

        return cleaned_data

    rait_1 = forms.IntegerField(min_value=0, max_value=2, required=False, widget=forms.HiddenInput())  # добавляем параметр required=False
    rait_2 = forms.IntegerField(min_value=0, max_value=2, required=False, widget=forms.HiddenInput())
    rait_3 = forms.IntegerField(min_value=0, max_value=2, required=False, widget=forms.HiddenInput())
    rait_4 = forms.IntegerField(min_value=0, max_value=2, required=False, widget=forms.HiddenInput())
    rait_6 = forms.IntegerField(min_value=0, max_value=2, required=False, widget=forms.HiddenInput())
    rait = forms.IntegerField(min_value=0, max_value=10, required=False, widget=forms.HiddenInput())


max_len = 1454

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
