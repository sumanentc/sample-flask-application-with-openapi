from db import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)


    def __repr__(self):
        return 'ItemModel(id=%d,name=%s, price=%s,)' % (self.id,self.name, self.price)

    def json(self):
        return {'id':self.id,'name': self.name, 'price': self.price}