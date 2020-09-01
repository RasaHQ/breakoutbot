install:
	pip install rasa

check:
	pre-commit run --files *.yml data/*