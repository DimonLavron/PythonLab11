from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.Currency import Currency
from models.Person import Person
from models.TypeOfCredit import TypeOfCredit


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://iotuser:password@localhost:3306/lab13_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.String(15), unique=False)
    client = db.Column(db.String(100), unique=False)
    clerk = db.Column(db.String(100), unique=False)
    date_of_beginning_service = db.Column(db.String(15), unique=False)
    service_term_in_month = db.Column(db.Integer, unique=False)
    service_fee = db.Column(db.Float, unique=False)
    interest_rate = db.Column(db.Float, unique=False)
    type_of_credit = db.Column(db.String(25), unique=False)

    def __init__(self, currency=None, client=None, clerk=None, date_of_beginning_service="01.01.1970", service_term_in_month=0, service_fee=0.0, interest_rate=0.0, type_of_credit=None):
        self.currency = str(currency)
        self.client = str(client)
        self.clerk = str(clerk)
        self.date_of_beginning_service = date_of_beginning_service
        self.service_term_in_month = service_term_in_month
        self.service_fee = service_fee
        self.interest_rate = interest_rate
        self.type_of_credit = str(type_of_credit)

    def __str__(self):
        return str(self.__dict__)


class CreditSchema(ma.Schema):
    class Meta:
        fields = ('currency', 'client', 'clerk', 'date_of_beginning_service', 'service_term_in_month', 'service_fee', 'interest_rate', 'type_of_credit')


credit_schema = CreditSchema()
credits_schema = CreditSchema(many=True)
db.create_all()

credit1 = Credit(Currency.EUR, Person("Dima", "Lavrishyn"), Person("Ivan", "Petrov"), "12.01.2019", 12, 12.5, 9.8, TypeOfCredit.CONSUMER)
credit2 = Credit(Currency.UAH, Person("Alina", "Klochko"), Person("Artem", "Sudakov"), "31.07.2018", 18, 7.5, 6.4, TypeOfCredit.MORTGAGE)
credit3 = Credit(Currency.RUB, Person("Olena", "Gavrylyuk"), Person("Melisa", "Harchenko"), "19.05.2016", 44, 11.3, 16.1, TypeOfCredit.CAR)
db.session.add(credit1)
db.session.add(credit2)
db.session.add(credit3)
db.session.commit()

@app.route('/credit', methods=['GET'])
def get_all_credits():
    all_credits = Credit.query.all()
    result = credits_schema.dump(all_credits)
    return jsonify(result.data)

@app.route('/credit/<credit_id>', methods=['GET'])
def get_credit(credit_id):
    credit = Credit.query.get(credit_id)
    return credit_schema.jsonify(credit)

@app.route('/credit', methods=['POST'])
def add_credit():
    currency = request.json['currency']
    client = request.json['client']
    clerk = request.json['clerk']
    date_of_beginning_service = request.json['date_of_beginning_service']
    service_term_in_month = request.json['service_term_in_month']
    service_fee = request.json['service_fee']
    interest_rate = request.json['interest_rate']
    type_of_credit = request.json['type_of_credit']

    new_credit = Credit(currency, client, clerk, date_of_beginning_service, service_term_in_month, service_fee, interest_rate, type_of_credit)

    db.session.add(new_credit)
    db.session.commit()

    return credit_schema.jsonify(new_credit)

@app.route('/credit/<credit_id>', methods=['PUT'])
def update_credit(credit_id):
    credit = Credit.query.get(credit_id)
    credit.currency = request.json['currency']
    credit.client = request.json['client']
    credit.clerk = request.json['clerk']
    credit.date_of_beginning_service = request.json['date_of_beginning_service']
    credit.service_term_in_month = request.json['service_term_in_month']
    credit.service_fee = request.json['service_fee']
    credit.interest_rate = request.json['interest_rate']
    credit.type_of_credit = request.json['type_of_credit']

    db.session.commit()
    return credit_schema.jsonify(credit)

@app.route('/credit/<credit_id>', methods=['DELETE'])
def delete_credit(credit_id):
    credit = Credit.query.get(credit_id)
    db.session.delete(credit)
    db.session.commit()

    return credit_schema.jsonify(credit)


if __name__ == '__main__':
    app.run()
