# Define password structure
    # upper lowerx7 upper 4xdigits 3xspecial

import os
import sys
import string
import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
special = ['!', '@', '#', '&', '%', '$', '*', '+', '=', '?']
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def select_function(array, seed):
    rng = random.Random(seed)
    return rng.choice(array)

def read_urandom(num_bytes):
    with open("/dev/urandom", 'rb') as f:
        return int.from_bytes(f.read(num_bytes), 'big')
        # print(int.from_bytes(f.read(num_bytes), 'big'))

def pass_gen(num_bytes):

    password = []
    password.append(select_function(upper, read_urandom(num_bytes)))
    for idx in range(7):
        password.append(select_function(lower, read_urandom(num_bytes)))
    password.append(select_function(upper, read_urandom(num_bytes)))
    for idx in range(4):
        password.append(str(select_function(digits, read_urandom(num_bytes))))
    for idx in range(3):
        password.append(select_function(special, read_urandom(num_bytes)))

    return(''.join(password))

@app.get("/json")
def get_json():

    message = pass_gen(random.randint(10, 100))

    return {"password": message, "status": "success"}
    

@app.get("/", response_class=HTMLResponse)
def get_alert():
    # Call your method
    message = pass_gen(random.randint(10, 100))
    
    # Return HTML with JavaScript alert
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Alert Page</title>
    </head>
    <body>
        <h2>Password!</h2>
        <p>{message}</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    # Run on port 8000 (you can change this)
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
