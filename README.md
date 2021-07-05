# Clone and run project
```bash
git clone https://github.com/JohnFirsthawk/django-project.git
python -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
cd myproject
cp myproject/.env.example myproject/.env
```
edit myproject/.env file to define
```vim
SECRET_KEY='test123'
DATABASE_URL=sqlite:///./db.sqlite3
```
# run development server
```bash
python manage.py runserver
```
