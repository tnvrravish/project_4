import logging

from app import db
from app.db.models import User, Transaction
from faker import Faker
from sqlalchemy.sql import functions


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        user = User('tnvrra393@gmail.com', 'spiderCLAW')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1


def test_accessing_user(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        assert db.session.query(User).count() == 2
        # log.info(user)
        assert user.email == 'tnvrra393@gmail.com'
        assert user.active == True


def test_inital_balance(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        assert user.inital_balance == 0
        assert user.get_balance() == 0


def test_adding_transactions(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        db.session.commit()
        # result = db.session.query(functions.sum(Transaction.amount)).scalar()
        result = db.session.query(functions.sum(Transaction.amount)).scalar()
        assert result == 1000
        assert db.session.query(Transaction).count() == 2

def test_deleting_user(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        assert db.session.query(Transaction).count() == 2
        db.session.delete(user)
        assert db.session.query(Transaction).count() == 0



        # song1 = Song.query.filter_by(title='test').first()
        # assert song1.title == "test"
        # #changing the title of the song
        # song1.title = "SuperSongTitle"
        # #saving the new title of the song
        # db.session.commit()
        # song2 = Song.query.filter_by(title='SuperSongTitle').first()
        # assert song2.title == "SuperSongTitle"
        # #checking cascade delete
        # db.session.delete(user)
        # assert db.session.query(User).count() == 0
        # assert db.session.query(Song).count() == 0
        #
        #
        #
        #
