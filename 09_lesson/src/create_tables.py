from src.database import engine, Base
from src.models import Student  # noqa: F401


Base.metadata.create_all(engine)

print("Таблица создана")
