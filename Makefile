install:
	pip install rasa pre-commit
	pre-commit install

check:
	pre-commit run --files *.yml data/*

test: check
	rasa test --stories tests/conversation_tests.md --fail-on-prediction-errors
