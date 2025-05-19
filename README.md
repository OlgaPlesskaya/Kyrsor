# 🎓 Система предоставления информации о ВУЗах «Курсор»  
## Проектная работа

> 🌐 Онлайн-сервис, помогающий абитуриентам выбрать подходящий вуз в Москве с учетом множества факторов: расположение, отзывы, программы обучения и многое другое.  
> 💡 В основе системы — Django (backend), HTML/CSS/JavaScript (frontend) и нейросетевая модель на Keras/TensorFlow для анализа отзывов.

---

## 🧩 Основные возможности

✅ **Информация о 50+ ВУЗах Москвы**  
✅ **Данные по направлениям подготовки, бюджетным местам и проходным баллам**  
✅ **Интерактивная карта корпусов и общежитий**  
✅ **Структурированные отзывы с автоматическим анализом тональности**  
✅ **Нейронная модель для определения эмоциональной окраски отзыва**

---

## 📸 Скриншоты

**Главная страница**

![image](https://github.com/user-attachments/assets/636b523f-8e1e-4777-8335-379673e5e8a1)

**Информация о ВУЗе**

![image](https://github.com/user-attachments/assets/8979a294-b36e-48c9-b220-19bd084c9295)

**Форма добавления отзыва**
![image](https://github.com/user-attachments/assets/435f0626-8c2e-4bb6-ab63-d2c90fd0d021)


---

## 🚀 Технологии

| Категория       | Используемые технологии                     |
|----------------|---------------------------------------------|
| Backend        | Python, Django                              |
| Frontend       | HTML, CSS, JavaScript                       |
| Базы данных    | SQLite / PostgreSQL                         |
| ML / NLP       | TensorFlow, Keras, NLTK, PyMorphy2           |
| Парсинг данных | BeautifulSoup, Selenium, Requests             |
| Анализ текста  | Дамерау–Левенштейн, Trie, автокоррекция     |
| Архитектура    | MVC (Model–View–Controller)                   |
| Визуализация   | Figma, IDEF0                                |

## 🛠 Установка и запуск

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/OlgaPlesskaya/Kyrsor.git
cd Kyrsor
```

### 2. Создайте и активируйте виртуальное окружение:

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 4. Выполните миграции:
```bash
python manage.py migrate
```

### 5. Запустите сервер:
```bash
python manage.py runserver
```

--- 

Готово! Сохраните этот текст как `README.md` в корень проекта.
