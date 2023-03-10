
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

install:
	poetry install


