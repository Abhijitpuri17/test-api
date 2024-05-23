from flask import Flask, request

app = Flask(__name__)

@app.route('/headers', methods=['POST', 'GET'])  # Only allow GET requests
def print_headers():
  """Prints all request headers"""
  headers = request.headers
  body = request.get_json()
  print(f"Request body: {body}")
  # Loop through headers dictionary and print key-value pairs
  for key, value in headers.items():
    print(f"{key}: {value}")
  return "Headers printed!"

if __name__ == '__main__':
  app.run(debug=True)
