# backend/seed_data.py
"""
Скрипт для заполнения базы данных тестовыми данными.
Создает категории и товары для демонстрации работы приложения.
Использует placeholder изображения с unsplash.com.
"""

from app.database import SessionLocal, init_db
from app.models.category import Category
from app.models.product import Product
from app.config import settings


def create_categories(db):
    """
    Создает категории товаров.

    Args:
        db: Сессия SQLAlchemy

    Returns:
        dict: Словарь созданных категорий {slug: Category}
    """
    categories_data = [
        {"name": "Электроника", "slug": "Электроника"},
        {"name": "Одежда", "slug": "Одежда"},
        {"name": "Книги", "slug": "Книги"},
        {"name": "Дом и сад", "slug": "Дом и сад"},
    ]

    categories = {}
    for cat_data in categories_data:
        category = Category(**cat_data)
        db.add(category)
        categories[cat_data["slug"]] = category

    db.commit()

    # Обновляем объекты после commit для получения ID
    for category in categories.values():
        db.refresh(category)

    return categories


def create_products(db, categories):
    """
    Создает товары в различных категориях.

    Args:
        db: Сессия SQLAlchemy
        categories: Словарь категорий
    """
    products_data = [
        # Electronics - Электроника
        {
            "name": "Беспроводные наушники",
            "description": "Высококачественные беспроводные наушники с шумоподавлением. Идеально подходят для любителей музыки и профессионалов. Время работы до 30 часов.",
            "price": 299.99,
            "category_id": categories["Электроника"].id,
            "image_url": "https://dkstatics-public.digikala.com/digikala-products/d1cfc051a3a78416b6d3106cf1b7a645d3419644_1671890836.jpg?x-oss-process=image/resize,m_lfit,h_300,w_300/quality,q_80"
        },
        {
            "name": "Умные часы Pro",
            "description": "Продвинутые умные часы с отслеживанием фитнеса, монитором сердечного ритма и GPS. Водонепроницаемы до 50м. Совместимы с iOS и Android.",
            "price": 399.99,
            "category_id": categories["Электроника"].id,
            "image_url": "https://images.deal.by/382344416_w200_h200_smart-chasy-umnye.jpg"
        },
        {
            "name": "Подставка для ноутбука",
            "description": "Эргономичная алюминиевая подставка для ноутбука. Регулируемая высота и угол наклона. Улучшает осанку и уменьшает нагрузку на шею. Совместима со всеми размерами ноутбуков.",
            "price": 49.99,
            "category_id": categories["Электроника"].id,
            "image_url": "https://avatars.mds.yandex.net/i?id=a83be19c15bd5e40181dee5fc58b9d55_sr-5289342-images-thumbs&n=13"
        },
        {
            "name": "USB-C концентратор",
            "description": "Многопортовый USB-C концентратор с HDMI, USB 3.0 и кард-ридером. Быстрая передача данных и вывод видео 4K. Компактный дизайн, идеальный для путешествий.",
            "price": 79.99,
            "category_id": categories["Электроника"].id,
            "image_url": "https://yandex-images.clstorage.net/9lD93xN32/e2e4e1wDgLV/mD_9JHlrmk_TCoSygzYK9a_ClRmCe54S8sxf06Kf6fu4d4q-Jr44y-LlJaApuar2iZmX3tZlmapCsNdCp06WRgzv6DQpK1tNl5jDthPyCbb_AZCNEfqNxnBMSgcsRPRzJTiU5my3cwHxJGIwrGOkcsNJi4kPsMkoGqdUROVZzNWZ9HZsuzxcyN5Vh7TG_cc_fgdZVBC1g9FwVxhXK0WwMyg0EyAusrnAtyX3N-xuYGPNjQvDiLKIIlzoFgNtXIsZUXD3IXTy3QZfXcx6SXvLejwMV9nSdYoTuhcflaMOcXFlNZVpJjV9gj2u8_0vbqhmgIXJz0y5AuqaLBqH5ZEGElixfur0s5JOHZsBOwE_i_2yw1wf2XKIGbfQGFOnC786KTJbb2Jw8Mj-KfU07KQhKE1OgMZEusCknanezeBWyRYS-fvkOzPYDZrXT_kDtUlw-YoV3xFzC9v7E9BaqcPyeWdyVe-n9bMI9GDyuSJt4C4Cy0NOR3oG7JbvHE3rnsNVU3qw7rX8UE1bF0z_APPLdv_FVlBZNAOT8pvS2ugJN3aoNB_n7Dt0TjZt8n8lLCanyAPLiQn7TqZXINtCoB6BWRXwca3xddSKktJPtIhygHI5D1bRG33CHLueHZIqx33yZn1V62C7_Qf2prk2bW3o4MaGxsiPtI-hF--YDKYfj1ZR-bjp9fiSA1XTijBNtA09ucKYHVk5Qxp92R3Yb8N8cW490ukjPLLDf-gyvuVm7SyCQQ9OSL5I4VusEgfnXImQmbP4ZD512stSEMA2CjLAOPEJXR6X98fbMNKU1anKfzAudFFm7r18y_WmcH1rrK2nzAqLRkj7DaYQqduFrpkKE5W4t6A_eRtKEZdId4k1AfBxCheeVztN1rpfWhFuSLT2JvsT6yB-eYCxZXx6r6jioECMAkQJvQWgHK0cTe9Yw9ibuz9qdTzZShaTA3lDvAI_ecPZnViwiRv4l1rYaE"
        },
        {
            "name": "Беспроводная клавиатура",
            "description": "Компактная беспроводная клавиатура с механическими переключателями. Длительное время работы от батареи и эргономичный дизайн. Идеальна как для работы, так и для игр.",
            "price": 89.99,
            "category_id": categories["Электроника"].id,
            "image_url": "https://avatars.mds.yandex.net/i?id=5726ea8831b932e00b628a7f9472b70b_sr-4080658-images-thumbs&n=13"
        },

        # Clothing - Одежда
        {
            "name": "Беговые кроссовки",
            "description": "Удобные беговые кроссовки с отличной амортизацией. Дышащий сетчатый верх и прочная резиновая подошва. Идеальны для бега и тренировок в зале.",
            "price": 129.99,
            "category_id": categories["Одежда"].id,
            "image_url": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa/global/309707/17/sv01/fnd/UKR/w/320/h/320/fmt/png"
        },

        # Books - Книги
        {
            "name": "Руководство по программированию на Python",
            "description": "Всеобъемлющее руководство по программированию на Python. От основ до продвинутых тем. Включает практические примеры и упражнения. Идеально для начинающих и программистов среднего уровня.",
            "price": 45.99,
            "category_id": categories["Книги"].id,
            "image_url": "https://avatars.mds.yandex.net/i?id=1e68fac9ba3ca8ae3eb1518be84dd25526c983ab-4355070-images-thumbs&n=13"
        },
        {
            "name": "Искусство дизайна",
            "description": "Вдохновляющая книга о принципах дизайна и творческом мышлении. Красивые иллюстрации и кейсы от известных дизайнеров.",
            "price": 39.99,
            "category_id": categories["Книги"].id,
            "image_url": "https://avatars.mds.yandex.net/i?id=dcf2e00e448413929d09bb0ef0998659e9c2f416-5567733-images-thumbs&n=13"
        },
        {
            "name": "Мастер-класс по кулинарии",
            "description": "Профессиональные кулинарные техники и рецепты. Пошаговые инструкции с красивыми фотографиями. Учитесь у шеф-поваров мирового класса.",
            "price": 49.99,
            "category_id": categories["Книги"].id,
            "image_url": "https://www.rollingstone.com/wp-content/uploads/2023/05/MasterClass-Subscription.png?w=300"
        },

        # Home & Garden - Дом и сад
        {
            "name": "Набор цветочных горшков",
            "description": "Набор из 3 керамических цветочных горшков с дренажными отверстиями. Современный дизайн, идеально подходит для комнатных растений. Включает поддоны для защиты мебели.",
            "price": 34.99,
            "category_id": categories["Дом и сад"].id,
            "image_url": "https://images-na.ssl-images-amazon.com/images/I/71YvypKnMAL._AC_UL330_SR330,330_.jpg"
        },
        {
            "name": "Светодиодная настольная лампа",
            "description": "Регулируемая светодиодная настольная лампа с сенсорным управлением. Несколько уровней яркости и цветовых температур. Энергоэффективная и безопасная для глаз.",
            "price": 59.99,
            "category_id": categories["Дом и сад"].id,
            "image_url": "https://avatars.mds.yandex.net/i?id=355c26ef5799faa9d69d79ed99cf65cb_sr-5264150-images-thumbs&n=13"
        }
    ]

    for product_data in products_data:
        product = Product(**product_data)
        db.add(product)

    db.commit()
    print(f"✅ Created {len(products_data)} products")


def seed_database():
    """
    Главная функция для заполнения базы данных.
    Создает таблицы, категории и товары.
    """
    print("🚀 Starting database seeding...")

    # Инициализируем БД (создаем таблицы)
    init_db()
    print("✅ Database tables created")

    # Создаем сессию
    db = SessionLocal()

    try:
        # Проверяем, не заполнена ли уже БД
        existing_categories = db.query(Category).count()
        if existing_categories > 0:
            print("⚠️  Database already contains data. Skipping seed.")
            return

        # Создаем категории
        print("📁 Creating categories...")
        categories = create_categories(db)
        print(f"✅ Created {len(categories)} categories")

        # Создаем товары
        print("📦 Creating products...")
        create_products(db, categories)

        print("🎉 Database seeding completed successfully!")

    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()