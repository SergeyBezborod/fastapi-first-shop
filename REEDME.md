🛍️ FastAPI Shop - Интернет-магазин
Современный fullstack интернет-магазин, построенный на FastAPI (backend) и Vue.js 3 (frontend) с чистотой архитектурой и отличной производительностью.

🚀 Технологический стек
Backend
<p align="left"> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"> <img src="https://img.shields.io/badge/Uvicorn-5A67D8?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn"> </p>
Frontend
<p align="left"> <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue.js"> <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite"> <img src="https://img.shields.io/badge/Pinia-FFD02F?style=for-the-badge&logo=pinia&logoColor=black" alt="Pinia"> <img src="https://img.shields.io/badge/Vue_Router-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white" alt="Vue Router"> <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" alt="Axios"> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="TailwindCSS"> </p>
📁 Структура проекта
bash
fastapi-shop/
├── 📂 backend/
│   ├── 📂 app/
│   │   ├── ⚙️ config.py           # Настройки приложения
│   │   ├── 🗄️ database.py         # Конфигурация БД
│   │   ├── 🚀 main.py            # Главный файл приложения
│   │   ├── 📂 models/            # Модели базы данных
│   │   │   ├── __init__.py
│   │   │   ├── 🏷️ category.py
│   │   │   └── 📦 product.py
│   │   ├── 📂 schemas/           # Pydantic схемы
│   │   │   ├── category.py
│   │   │   └── product.py
│   │   ├── 📂 repositories/      # Слой доступа к данным
│   │   │   ├── category_repository.py
│   │   │   └── product_repository.py
│   │   ├── 📂 services/          # Бизнес-логика
│   │   │   ├── category_service.py
│   │   │   ├── product_service.py
│   │   │   └── cart_service.py
│   │   ├── 📂 routes/            # API маршруты
│   │   │   ├── __init__.py
│   │   │   ├── products.py
│   │   │   ├── categories.py
│   │   │   └── cart.py
│   │   └── 📂 static/            # Статические файлы
│   │       └── 📂 images/
│   ├── 📋 requirements.txt       # Python зависимости
│   ├── 🎯 run.py                # Точка входа для запуска
│   └── 🌱 seed_data.py          # Скрипт для заполнения БД
└── 📂 frontend/
    ├── 📂 src/
    │   ├── 📂 components/        # Vue компоненты
    │   │   ├── 🧩 Header.vue
    │   │   ├── 🛒 CartItem.vue
    │   │   └── ...
    │   ├── 📂 views/             # Страницы приложения
    │   │   ├── 🏠 HomePage.vue
    │   │   ├── 🛍️ CartPage.vue
    │   │   └── 📄 ProductDetailPage.vue
    │   ├── 📂 stores/            # Pinia stores
    │   ├── 📂 router/            # Vue Router конфигурация
    │   ├── 🔧 main.js            # Главный файл приложения
    │   └── 🎨 App.vue            # Корневой компонент
    ├── 📦 package.json           # Node.js зависимости
    ├── ⚡ vite.config.js         # Конфигурация Vite
    └── 📄 index.html             # HTML шаблон
🛠️ Установка и запуск
Предварительные требования
Python 3.8+ 🐍

Node.js 16+ ⚡

npm или yarn 📦

🔙 Настройка Backend
Шаги установки:
bash
# 1. Перейдите в папку backend
cd backend

# 2. Создайте виртуальное окружение
python -m venv venv

# 3. Активируйте виртуальное окружение
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Установите зависимости
pip install -r requirements.txt
⚙️ Настройка окружения (опционально)
Создайте файл .env в папке backend:

env
# backend/.env
DEBUG=True
DATABASE_URL=sqlite:///./shop.db
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
🗄️ Инициализация базы данных
bash
python seed_data.py
🚀 Запуск сервера
bash
python run.py
📍 Backend сервер будет доступен по адресу:
http://localhost:8000

🔜 Настройка Frontend
Шаги установки:
bash
# 1. Перейдите в папку frontend
cd frontend

# 2. Установите зависимости
npm install

# 3. Запустите dev сервер
npm run dev
📍 Frontend будет доступен по адресу:
http://localhost:5173

📖 API Документация
После запуска backend сервера, интерактивная документация API будет доступна по адресам:

Документация	Ссылка
Swagger UI	http://localhost:8000/api/docs
ReDoc	http://localhost:8000/api/redoc
🔌 Основные эндпоинты
🏷️ Категории
Метод	Эндпоинт	Описание
GET	/api/categories	Получить все категории
GET	/api/categories/{id}	Получить категорию по ID
📦 Товары
Метод	Эндпоинт	Описание
GET	/api/products	Получить все товары
GET	/api/products/{id}	Получить товар по ID
GET	/api/products/category/{category_id}	Получить товары категории
🛒 Корзина
Метод	Эндпоинт	Описание
POST	/api/cart/add	Добавить товар в корзину
PUT	/api/cart/update	Обновить количество товара
DELETE	/api/cart/remove/{product_id}	Удалить товар из корзины
🎯 Функциональность
👤 Для пользователей
📱 Адаптивный дизайн - отлично работает на всех устройствах

🛍️ Просмотр товаров - каталог с фильтрацией по категориям

📄 Детальные страницы - подробная информация о товарах

🛒 Корзина покупок - добавление/удаление товаров, изменение количества

💾 Сохранение состояния - корзина сохраняется в localStorage

👨‍💻 Для разработчиков
🏗️ Чистая архитектура - разделение на слои (repositories, services, routes)

🔧 Type safety - Pydantic схемы для валидации данных

🗄️ База данных - SQLAlchemy ORM с поддержкой миграций

🔒 CORS настройки - готовность к интеграции с фронтендом

📝 Документация API - автоматическая генерация Swagger/ReDoc

🔧 Команды разработки
Backend
bash
# Запуск с автоперезагрузкой
python run.py

# Заполнение базы данных тестовыми данными
python seed_data.py

# Проверка здоровья API
curl http://localhost:8000/health
Frontend
bash
# Development сервер
npm run dev

# Сборка для production
npm run build

# Предварительный просмотр production сборки
npm run preview

# Линтинг кода
npm run lint

# Форматирование кода
npm run format
📞 Контакты и поддержка
Если у вас есть вопросы или предложения по улучшению проекта, создайте issue в репозитории проекта.

<div align="center">
⭐ Не забудьте поставить звезду репозиторию, если проект вам понравился!

</div>