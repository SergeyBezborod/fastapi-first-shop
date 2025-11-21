# Стадия сборки
FROM node:20-alpine as build-stage

WORKDIR /app

# Копирование package.json и package-lock.json
COPY package*.json ./

# Установка зависимостей
RUN npm ci

# Копирование исходного кода
COPY . .

# Сборка приложения
RUN npm run build

# Стадия production
FROM node:20-alpine as production-stage

WORKDIR /app

# Установка serve для раздачи статических файлов
RUN npm install -g serve

# Копирование собранного приложения
COPY --from=build-stage /app/dist ./dist

# Открытие порта
EXPOSE 3000

# Запуск приложения
CMD ["serve", "-s", "dist", "-l", "3000"]