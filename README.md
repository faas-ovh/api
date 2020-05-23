# queue-api
[![pipeline status](https://gitlab.com/softreck/api.telemonitorowanie.pl/badges/master/pipeline.svg)](https://gitlab.com/softreck/api.telemonitorowanie.pl/-/commits/master)

start

    run.bat
    browser
    
## docs
https://fastapi.tiangolo.com/deployment/


https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

## NGINX 
unix
    
    nginx/install.sh

## Uvicorn
unix

    ./uvicorn.start.sh

windows
    cd F:\PycharmProjects\gitlab-queue-api
    .\uvicorn.start.bat

## Environment
    py -m pip install -r requirements.txt
    
    pip install -r src/requirements.txt

### Local

unix

    env-local/start.sh
    env-local/stop.sh

windows

    env-local\start.bat
    env-local\stop.bat

    
### Test

    env-test/start.sh
    env-test/stop.sh

### Production

    env-production/start.sh
    env-production/stop.sh

