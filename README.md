# schedule-appointments
A django app to create and list appointments

# Requirement

- python ^3.7 (Use pyenv to switch between versions if you don't already. Its amazing!)
- [poetry](https://python-poetry.org/docs/#installation)

# Install Dependencies
```bash
$ poetry install
```

# Run migrations, collect static files and create test user
```bash
poetry run python manage.py migrate
poetry run python manage.py collectstatic
poetry run python manage.py create_test_user
```

# Run server
```bash
poetry run python manage.py runserver
```

# Run tests

```bash
poetry run pytest
```
