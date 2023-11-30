pip3 install -U Flask-WTF
pip3 install -U email-validator
pip3 install -U flask-sqlalchemy
python3 app.py

--sql--
CREATE USER 'trabg2'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON *.* TO 'trabg2'@'localhost';
CREATE DATABASE IF NOT EXISTS trabg2;
FLUSH PRIVILEGES;
