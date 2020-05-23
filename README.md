# queue-api

# [How to Execute BASH Commands in a Remote Machine in Python](https://www.thepythoncode.com/article/executing-bash-commands-remotely-in-python)
more: https://github.com/x4nth055/pythoncode-tutorials
To run this:
- `pip3 install -r requirements.txt`
- To execute an entire BASH script (.sh) named `script.sh` for instance on `192.168.1.101` with `test` as username and `abc123` as password:
    ```
    python execute_bash.py 192.168.1.101 -u root -p inventedpassword123 -b script.sh
    ```
  
## inspiration
https://github.com/x4nth055/pythoncode-tutorials/tree/master/general/execute-ssh-commands

start

    run.bat
    browser

windows
    cd F:\PycharmProjects\gitlab-queue-api
    .\uvicorn.start.bat

## Environment
    py -m pip install paramiko
    py -m pip install -r requirements.txt
    
    pip install -r src/requirements.txt

