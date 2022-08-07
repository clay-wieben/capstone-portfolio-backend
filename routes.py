import os
from flask import current_app, jsonify, render_template, request, send_from_directory
from app import create_app, db
from models import Paragraphs, paragraphs_schema, paragraph_schema

app = create_app()

@app.route("/", methods=["GET"], strict_slashes=False)
def paragraphs():

    paragraphs = Paragraphs.query.all()
    results = paragraphs_schema.dump(paragraphs)

    return jsonify(results)

@app.route('/get/<id>/', methods = ['GET'])
def get_specific(id):
    paragraph = Paragraphs.query.get(id)
    db.session.get(Paragraphs, id)
    db.session.commit()

    return paragraph_schema.jsonify(paragraph)

@app.route('/add', methods = ['POST'])
def add_paragraphs():
    title = request.json['title']
    body = request.json['body']

    paragraphs = Paragraphs(title=title, body=body)
    db.session.add(paragraphs)
    db.session.commit()
    return paragraph_schema.jsonify(paragraphs)

@app.route('/delete/<id>/', methods = ['DELETE'])
def paragraph_delete(id):
    paragraph = Paragraphs.query.get(id)
    db.session.delete(paragraph)
    db.session.commit()

    return paragraph_schema.jsonify(paragraph)

@app.route('/static/images/<path:filename>')
def send_file(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    app.run(debug=True)