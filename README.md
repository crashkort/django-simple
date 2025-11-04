# django-simple
- Install python 3.10 or later (3.10, 3.11, 3.12, 3.13, or 3.14)
- Setup a virtual environment and activate it
	python3 -m venv env && source env/bin/activate
- Clone the repo 
	git clone git@github.com:crashkort/django-simple.git && cd django-simple
- Install requirements
	 pip3 install -U -r requirements.txt
- Handle migratations
	python manage.py makemigrations && python manage.py migrate
- Run the django install
	python manage.py runserver
