class Queries:
    CREATE_SURVEY_TABLE = """
    CREATE TABLE IF NOT EXISTS review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    number TEXT,
    date_of_visit TEXT,
    quality_food TEXT,
    quality_clean TEXT
    )
    """

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS Dishes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        picture TEXT,
        category_id INTEGER, 
        FOREIGN KEY (category_id) REFERENCES category (id)
        )
    """
    CREATE_CATEGORY_TABLE = """
        CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    POPULATE_CATEGORY = """
        INSERT INTO category (name)
        VALUES ('Салаты'),
        ('Европейская кухня'), ('Восточная кухня'),
        ('Напитки'), ('Десерты')

    """
    DROP_CATEGORY_TABLE = """DROP TABLE IF EXISTS category"""
    DROP_DISHES_TABLE = """DROP TABLE IF EXISTS Dishes"""
    POPULATE_DISHES = """
    INSERT INTO Dishes (name, price, picture, category_id)
    VALUES 
    ('Теплый салат с фалафелем и яблоком', 390, 'images/salad1.jpg', 1),
    ('Салат Кобб', 380, 'images/salad2.jpg', 1),
    ('Греческий салат', 430, 'images/salad3.jpg', 1),
    ('Салат с курицей по-азатски', 350, 'images/salad4.jpg', 1),
    ('Салат Капрезе', 430, 'images/salad5.jpg', 1),
    ('Брускетта с авокадо и креветками', 690, 'images/food1.jpg', 2),
    ('Суп из красной чечевицы', 495, 'images/food2.jpg', 2),
    ('куриные шашлычки по-гречески на гриле', 530, 'images/food3.jpg', 2),
    ('Хек в духовке целиком', 450, 'images/food4.jpg', 2),
    ('Говяжьи котлеты с хлебом и молоком', 400, 'images/food5.jpg', 2),
    ('Мастава', 240, 'images/meal1.jpg', 3),
    ('Шурпа', 280, 'images/meal2.jpg', 3),
    ('Курица запеченная с картошкой', 270, 'images/meal3.jpg', 3),
    ('Шурпа Куза', 270, 'images/meal4.jpg', 3),
    ('Пик-Жиз', 300, 'images/meal5.jpg', 3),
    ('Молочный коктейль', 150, 'images/juice1.jpg', 4),
    ('Апельсиновый сок', 150, 'images/juice2.jpg', 4),
    ('Натуральный сок', 150, 'images/juice3.jpg', 4),
    ('Кока-Кола', 150, 'images/juice4.jpg', 4),
    ('Вода газированная', 150, 'images/juice5.jpg', 4),
    ('Тирамису с трюфелем', 220, 'images/desert1.jpg', 5),
    ('Пирожное макарон', 220, 'images/desert2.jpg', 5),
    ('Крем-брюле с апельсином', 220, 'images/desert3.jpg', 5),
    ('Панна-котта с ягодами', 220, 'images/desert4.jpg', 5),
    ('Профитроли с кракелюром', 200, 'images/desert5.jpg', 5)
    
    

    """