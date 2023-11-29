from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()
 

 #python3 reset_db.py no terminal para resetar o banco de dados