run:
	export DB_NAME=category-mapping && export DB_USER=admin && export DB_PASSWORD=pass && docker-compose up

init_behave_test:
	export DB_NAME=category-mapping-test && export DB_USER=test && export DB_PASSWORD=test && docker-compose up

test_behave:
	export DB_NAME=category-mapping-test && export DB_USER=test && export DB_PASSWORD=test && pytest tests/behave -p no:warnings

test_unit:
	pytest tests/unit
