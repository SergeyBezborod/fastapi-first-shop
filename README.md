# 🛍️ FastAPI Shop - Интернет-магазин

Современный fullstack интернет-магазин, построенный на FastAPI (backend) и Vue.js 3 (frontend) с чистой архитектурой и отличной производительностью.

## Backend
<p align="left">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/Uvicorn-5A67D8?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn">
</p>

## Frontend
<p align="left">
<img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue.js">
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
<img src="https://img.shields.io/badge/Pinia-FFD02F?style=for-the-badge&logo=pinia&logoColor=black" alt="Pinia">
<img src="https://img.shields.io/badge/Vue_Router-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white" alt="Vue Router">
<img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" alt="Axios">
<img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="TailwindCSS">
</p>

## ✨ Особенности

### 🎯 Для пользователей
- 📱 **Адаптивный дизайн** - отлично работает на всех устройствах
- 🛍️ **Умный каталог** - фильтрация и поиск товаров по категориям
- 📄 **Детальные страницы** - полная информация о товарах с изображениями
- 🛒 **Корзина покупок** - добавление/удаление товаров, изменение количества
- 💾 **Сохранение состояния** - корзина сохраняется в localStorage

### ⚡ Для разработчиков
- 🏗️ **Чистая архитектура** - разделение на слои (repositories, services, routes)
- 🔧 **Type safety** - Pydantic схемы для валидации данных
- 🗄️ **SQLAlchemy ORM** - поддержка миграций и различных СУБД
- 🔒 **CORS настройки** - готовность к интеграции с фронтендом
- 📝 **Автодокументация** - автоматическая генерация Swagger/ReDoc

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.8+ 🐍
- Node.js 16+ ⚡
- npm или yarn 📦

```bash
# Клонировать репозиторий
git clone https://github.com/your-username/fastapi-shop.git
cd fastapi-shop

```

### 🔙 Backend установка
```bash
# Перейти в папку backend
cd backend

# Создать виртуальное окружение
python -m venv venv

# Активировать окружение
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Инициализировать базу данных
python seed_data.py

# Запустить сервер
python run.py
```
Backend будет доступен по адресу: http://localhost:8000

### 🔜 Frontend установка
```bash
# Перейти в папку frontend
cd frontend

# Установить зависимости
npm install

# Запустить dev сервер
npm run dev
```
Frontend будет доступен по адресу: http://localhost:5173

## 📚 Структура проекта

```text
fastapi-shop/
├── backend/
│   ├── app/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── category.py
│   │   │   └── product.py
│   │   ├── schemas/
│   │   │   ├── category.py
│   │   │   └── product.py
│   │   ├── repositories/
│   │   │   ├── category_repository.py
│   │   │   └── product_repository.py
│   │   ├── services/
│   │   │   ├── category_service.py
│   │   │   ├── product_service.py
│   │   │   └── cart_service.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── products.py
│   │   │   ├── categories.py
│   │   │   └── cart.py
│   │   └── static/
│   │       └── images/
│   ├── requirements.txt
│   ├── run.py
│   └── seed_data.py
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── Header.vue
    │   │   ├── CartItem.vue
    │   │   └── ...
    │   ├── views/
    │   │   ├── HomePage.vue
    │   │   ├── CartPage.vue
    │   │   └── ProductDetailPage.vue
    │   ├── stores/
    │   ├── router/
    │   ├── main.js
    │   └── App.vue
    ├── package.json
    ├── vite.config.js
    └── index.html
```

## 📖 API Документация
После запуска backend сервера доступна автоматическая документация:

Интерактивная документация с возможностью тестирования (Swagger UI) -	http://localhost:8000/api/docs	
Альтернативная документация (ReDoc) -	http://localhost:8000/api/redoc	
