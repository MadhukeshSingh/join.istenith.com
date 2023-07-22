<p align='center'>
<img width="200" src="static/logo.png" alt="ISTE">
</p>
<h1 align='center'>INTERVIEWS WEBSITE'22</h1>
This website is using django backend. All you need to do is to go through https://docs.djangoproject.com/ so that you get the basic knowledge that how things are working in django.

## Steps to follow :pencil2::

1. First of all install Django:

For any system:

```bash
  python -m pip install Django
```

For Archlinux:

```bash
sudo pacman -S python-django
```

2. Clone the repository:

```bash
git clone https://github.com/istenith/join.istenith.com.git
```

3. Change the directory to join.istenith.com using:

```bash
cd join.istenith.com
```

4. Create a virtual environment:

```bash
pip install virtualenv
virtualenv venv
```

5. Activate the virtual environment

```bash
source venv/bin/activate
```

6. Now install all the packages which are being used in this project:

```bash
pip install -r requirements.txt
```

7. Migrate all the database

```bash
python manage.py migrate
```
8. Load the static files
```bash
python manage.py collectstatic
```
9. Now run the development server:

```bash
python manage.py runserver
```
