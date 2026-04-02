from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route 1: Posts
@app.route('/posts', methods=['GET'])
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return jsonify(response.json())

# Route 2: Comments
@app.route('/comments', methods=['GET'])
def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)
    return jsonify(response.json())

# Route 3: Albums
@app.route('/albums', methods=['GET'])
def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)