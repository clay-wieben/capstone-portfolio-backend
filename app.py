from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

def create_app():
    """Application-factory pattern"""
    app=Flask(__name__,
                static_url_path='',
                static_folder='./static')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app









# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow


# app = Flask(__name__)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# app.config['SQLALCHEMY_DATABSE_URI'] = 'mysql://root:''@localhost/flask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class Paragraphs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     body = db.Column(db.Text())

#     def __init__(self, title, body):
#         self.title = title
#         self.body = body

# class ParagraphSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'body')

# paragraph_schema = ParagraphSchema()
# paragraphs_schema =  ParagraphSchema(many=True)

# @app.route('/get', methods = ['GET'])
# def get_paragraphs():
#     all_paragraphs = Paragraphs.query.all()
#     results = paragraphs_schema.dump(all_paragraphs)
#     return jsonify(results)

# @app.route('/get/<id>/', methods = ['GET'])
# def post_details(id):
#     paragraph = Paragraphs.query.get(id)
#     return paragraph_schema.jsonify(paragraph)


# @app.route('/add', methods = ['POST'])
# def add_paragraphs():
#     title = request.json['title']
#     body = request.json['body']

#     paragraphs = Paragraphs(title, body)
#     db.session.add(paragraphs)
#     db.session.commit()
#     return paragraph_schema.jsonify(paragraphs)

# @app.route('/update/<id>/', methods = ['PUT'])
# def update_paragraph(id):
#     paragraph = Paragraphs.query.get(id)

#     title = request.json['title']
#     body = request.json['body']

#     paragraph.title = title
#     paragraph.body = body

#     db.session.commit()
#     return paragraph_schema.jsonify(paragraph)

# @app.route('/delete/<id>/', methods = ['DELETE'])
# def paragraph_delete(id):
#     paragraph = Paragraphs.query.get(id)
#     db.session.delete(paragraph)
#     db.session.commit()

#     return paragraph_schema.jsonify(paragraph)

# if __name__ == '__main__':
#     app.run(debug=True)