### Installation
```bash
$ pip install django-db-config
```

#### `settings.py`
```python
INSTALLED_APPS+=['django_db_config']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Models
model|db_table|fields/columns
-|-|-
`Config`|`config`|`id`,`key`,`value`

