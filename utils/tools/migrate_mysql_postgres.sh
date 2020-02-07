#!/bin/bash

# dump existing data with MySQLite
python manage.py dumpdata > db.json
# or use the following to exclude content type data
python manage.py dumpdata --exclude=contenttypes --natural-foreign --natural-primary > db.json

# change backend to PostGres

# build PostGres database and tables
python manage.py migrate --run-syncdb

# exclude content type data
python manage.py shell

```
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
```

# load MySQLite data into PostGres
python manage.py loaddata db.json
