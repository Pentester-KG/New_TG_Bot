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
