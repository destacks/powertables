# Destacks Powertable

## Templating Systems

- JS (Nunjucks)
- Django (DTL)
- Django, Flask, Starlette, FastAPI (Jinja2)

## Features

- column filtering
- column sorting
- get
- create
- update (put/patch)
- delete
- export
- use of multiple models in one table
- use of multiple tables in one view
- use of filtersets (bulk CRUD)
- support complex SQL lookups
- methods for optimizing lookup speeds
- logger (for example for logging speed of lookups in production)
- function based and class based views
- Following REST principles (even using HTTP Verbs)
- use of caching and HTTP modifier
- i18n
- l10n
- great documentation
- no-jquery, no datatables.js
- BEM CSS SAAS
- easy CSS themeing
- bootstrap integration (?)
- tailwind integration (?)
- Use of messaging systems
- Use of role system for visibility (different tables and editing possibilities for
  different roles)
- Column pivoting
- A11Y
- infinity scroll
- zero JS config
- Server Side validation with optional (CSS pattern validation injection)
- Data Import (CSV, Excel etc.)
- reactive derived fields that are not model fields (which are sort- and filterable)
- Commands for models inspection and auto creation of views -> online tool (like Spring
  initalizer)
- htmx (?), unpoly (?) etc. usage/support (?) (maybe if given, can switch out with
  engine)
- strictly adheres to progressive enhancement principles, 100 % functionality without
  JS!
- very conservative update policy, with LTS versions for patching (should align with
  Django LTS)
- no IE11 support

## Development

- TDD
- Clean Architecture
- Clean Code
- IOC
- SOLID-Principles
- AOP
- ROCA

## Shell commands

- `python manage.py dumpdata contacts --indent 2 > contacts.json`


## Knowledge

- [Form inside a table](https://stackoverflow.com/a/5967613)
