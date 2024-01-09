lint:
	flake8 .
	tox -e lint

typecheck:
	mypy api_client_results
	tox -e typecheck


