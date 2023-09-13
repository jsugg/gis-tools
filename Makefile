.PHONY: test start-api

test:
	coverage run --source=features.polygon_calculation.polygon,features.polygon_calculation.main,utils.logger,utils.file_handler -m unittest discover tests
	coverage report -m

start-api:
	cd api && flask run
