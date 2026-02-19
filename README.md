# Zamonaviy Ilmlar - Talim Platformasi

Zamonaviy Ilmlar - burada o'quvchilar va o'qituvchilar uchun to'liq talim platformasi.

## 🎓 Platformaning Xususiyatlari

- ✅ Foydalanuvchi Autentifikatsiyasi (O'quvchi/O'qituvchi)
- ✅ 8 ta Fandan Kurslar
- ✅ Video Darslar
- ✅ Quiz va Testlar
- ✅ Uyga Vazifalar
- ✅ Progress Ko'rsatkichi
- ✅ Sertifikat Olish
- ✅ Sharh va Baho Sistema

## 🛠️ Texnologiyalar

- **Backend**: Django (Python)
- **Frontend**: Django Templates + Bootstrap
- **Database**: PostgreSQL / SQLite
- **Authentication**: Django Auth System

## 📦 O'rnatish

```bash
git clone https://github.com/gozalmalikova24-a11y/zamonaviy-ilmlar.git
cd zamonaviy-ilmlar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📂 Repozitoriya Tuzilmasi

```
zamonaviy-ilmlar/
├── manage.py
├── requirements.txt
├── zamonaviy_ilmlar/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── courses/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── quizzes/
│   ├── models.py
│   ├── views.py
│   └── templates/
└── templates/
    └── base.html
```

## 👨‍💻 Ishtirokchilar

- Gozal Malikova (Developer)