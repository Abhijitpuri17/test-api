from flask import Flask
from requests import request  

app = Flask(__name__)

@app.route('/')
def hello_world():
  # Log the request (replace with your preferred logging library/implementation)
  return 'Hello, World!'

if __name__ == '__main__':
  app.run(debug=False)  # Set debug to False for deployment
