from flask import Flask, jsonify, Blueprint
from api.menus.menus_bp import menus_bp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return jsonify({"message": "Hello World"})

# define and call blueprints
app.register_blueprint(menus_bp, url_prefix='/api/menus')


if __name__ == "__main__":
    app.run(debug=True)