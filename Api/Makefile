run:
	FLASK_ENV=development FLASK_APP=atadosapi/app.py flask run

install:
	python3 setup.py install

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf *.egg-info

test:
	python3 setup.py install
	make clean
	FLASK_ENV=test FLASK_APP=atadosapi/app.py flask drop-db
	FLASK_ENV=test FLASK_APP=atadosapi/app.py flask create-db
	FLASK_ENV=test pytest tests/ -v
