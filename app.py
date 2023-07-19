from flask import Flask

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource():
    # code to handle GET request
    return 'This is the resource'


@app.route('/api/resource', methods=['POST'])
def create_resource():
    # code to handle POST request
    return 'Resource created'

if __name__ == '__main__':
       app.run()