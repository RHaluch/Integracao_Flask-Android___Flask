from my_app import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    ativo = db.Column(db.Boolean)
    quantidade_jogos = db.Column(db.Integer)

    def __init__(self,name,year,price, ativo, quantidade_jogos):
        self.name = name
        self.year = year
        self.price = price
        self.ativo = ativo
        self.quantidade_jogos = quantidade_jogos

    def __repr__(self):
        return 'Console {0}'.format(self.id)