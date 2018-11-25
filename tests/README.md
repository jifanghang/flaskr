## Tests
This folder contains the unit tests for the project.

Please install `pytest` and `coverage` if you want to use the unittest codes here.
```bash
pip install pytest coverage
```

* `conftest.py`: contains setup functions (*fixtures*) for each test.
* `test_factory.py`: test factory itself - pass test config.
* `test_db.py`: test database.
* `test_auth.py`: test user authentication.
* `test_blog.py`: test blog functionalities.

***To make running tests (with coverage) less verbose, a `../setup.cfg` file is added.***

Run the tests
```bash
pytest
pytest -v
```

To measure the code coverage of test
```bash
coverage run -m pytest
coverage report          # coverage report
coverage html            # html report
```