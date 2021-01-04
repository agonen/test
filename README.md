# test

## Setup instructions:

1. Create virtual environment and install requirements

```shell
    virtualenv -p python3.7 .venv
    pip install -r requirements.txt
```

2. Install redis (macos )

```shell
    brew install redis
    # redis-server /usr/local/etc/redis.conf  <-- starting redis-server
```

## Running 
1. Active venv 
```shell
. .venv/bin/activate
```
2. run main.py  
Note: without paramters will trigger flask server
