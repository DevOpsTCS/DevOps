#!/usr/bin/python
from app import app
debug = True
app.run(host='10.138.97.172', port=5070, threaded=2)
