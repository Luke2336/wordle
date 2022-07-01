all:
	python3 main.py

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete