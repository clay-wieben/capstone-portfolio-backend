from app import db, ma

class Paragraphs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Paragraphs %r>" % self.title

class ParagraphSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "body")

paragraph_schema = ParagraphSchema()
paragraphs_schema = ParagraphSchema(many=True)
