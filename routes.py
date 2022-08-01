from flask import current_app, jsonify, request
from app import create_app, db
from models import Paragraphs, paragraphs_schema, paragraph_schema

app = create_app()

@app.route("/kelly", methods=["GET"], strict_slashes=False)
def kelly():
    return jsonify("I don't know what I'm doing.")

@app.route("/get", methods=["GET"], strict_slashes=False)
def paragraphs():

    paragraphs = Paragraphs.query.all()
    results = paragraphs_schema.dump(paragraphs)

    return jsonify(results)

@app.route('/add', methods = ['POST'])
def add_paragraphs():
    # return jsonify(request.json)
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

if __name__ == "__main__":
    app.run(debug=True)