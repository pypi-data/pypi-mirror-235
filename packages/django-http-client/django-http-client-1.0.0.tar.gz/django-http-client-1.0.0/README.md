### Installation
```bash
$ pip install django-http-client
```

#### `settings.py`
```python
INSTALLED_APPS+=['django_http_client']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Models
model|db_table
-|-
`Request`|`http_client_request`
`RequestException`|`http_client_request_exception`
`Response`|`http_client_response`

###### `Request` methods

name|description
-|-
`.get_data()`|return data dict
`.get_headers()`|return headers dict

###### `Response` methods

name|description
-|-
`.delete_disk_path()`|delete `disk_path` file or dir
`.get_content()`|return content
`.get_content_data()`|return content data/json/dict
`.get_headers()`|return headers dict
`.get_request_info()`|return `request_info` dict

### Examples
`Request`
```python
from django_http_client.models import Request

Request(
    host='api.github.com', # used for limit_per_host/load balancer
    url='https://api.github.com/users/LOGIN/repos?page=1',
    method='GET',
    allow_redirects=True,
    headers=json.dumps(headers),
    disk_path='api.github.com/users/LOGIN/repos/1',
    max_redirects=5,
    max_retries=5
).save()
```

`Response`
```python
from django_http_client.models import Response

with session.request(**kwargs) as response:
    Response(
        url=response.url,
        status=response.status,
        headers=json.dumps(response.headers),
        request_info=json.dumps(request_info),
        disk_path=disk_path
    ).save()

for response in Response.objects.all():
    request_info = response.get_request_info()
    headers = response.get_headers()
    response.delete_disk_path()
```

`RequestException`
```python
from django_http_client.models import RequestException

except Exception as e:
    RequestException(
        host=request_info['host'], # used for load balancer/stat
        url=response.url,
        request_info=json.dumps(request_info),
        exc_type=type(e),
        exc_message = str(e),
        timestamp = round(time.time(),3)
    ).save()
```

