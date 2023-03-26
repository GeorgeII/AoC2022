### Poetry, pytest, Flake8,

Setup:

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

Run unit tests:

```sh
poetry run python -m unittest .\test\unit_tests.py
```

Run formatters, utilities and style checkers:

```sh
poetry run black .
poetry run isort .
poetry run flake8 .
```

Run benchmarks:

```sh
poetry run pytest test\benchmarks.py --benchmark-histogram=.benchmarks/historgram --benchmark-autosave
```

Output plot for benchmarks is saved as a `.benchmarks/historgram.svg` file:
<img src="https://raw.githubusercontent.com/GeorgeII/AoC2022/master/python/.benchmarks/historgram.svg?raw=true" />



