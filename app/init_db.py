from app.database import Base, engine
from app.models import User, Project, Task, Comment  
Base.metadata.create_all(bind=engine)

print("✅ Tables créées avec succès !")
