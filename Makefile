install:
	pip install rasa

check:
	pre-commit run --files *.yml data/*

test: check
	rasa test --stories tests/conversation_tests.md --fail-on-prediction-errors
