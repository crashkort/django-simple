# django-simple
- Install python 3.8
- Setup a virtual enviroment and activate it
	virtualenv -v python3.8 env && source env/bin/activate
- Clone the repo 
	git clone git@github.com:crashkort/django-simple.git && cd django-simple
- Install requirements
	 pip3 install -U -r requirements.txt
- Handle migratations
	python manage.py makemigrations && python manage.py migrate
- Run the django install
	python manage.py runserver
