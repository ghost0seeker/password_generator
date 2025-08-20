A simple password generator which uses /dev/urandom to generate passswords in memorable format

Usage:

```python
# cli
python gen_pass.py 10 # or some other int

# fastapi server
python gen_pass_server.py

# get password via REST
curl http://localhost:8000/json
```