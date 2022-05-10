## Knowledge

- [How to write reusable apps](https://docs.djangoproject.com/en/dev/intro/reusable-apps/)
- [How-to: installable Django app](https://realpython.com/installable-django-app/)
- [Form inside a table](https://stackoverflow.com/a/5967613)

## Publish

```bash
. venv/bin/activate

# Update to newest Readme and license texts
cp ./README.md django-powertables/
cp ./LICENSE.txt django-powertables/
cp ./LICENSE.AGPL.txt django-powertables/

cd django-powertables

# Build
python setup.py sdist

# Test with twine
twine check dist/*

# Upload with twine
twine upload dist/*
```
