from db import db
from models.entities import Item
from typing import List


class ItemRepo:
    
 def create(self,item):
    db.session.add(item)
    db.session.commit()
    
 def fetchById(self,_id)-> 'Item':
     return db.session.query(Item).filter_by(id=_id).first()
 
 def fetchAll(self) -> List['Item']:
     return db.session.query(Item).all()
 
 def delete(self,_id) -> None:
     item= db.session.query(Item).filter_by(id=_id).first()
     db.session.delete(item)
     db.session.commit()
     
 def update(self,item_data):
    db.session.merge(item_data)
    db.session.commit()