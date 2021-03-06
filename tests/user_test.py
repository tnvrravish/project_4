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
        # checking no of transactions for user tnvrra393@gmail.com
        assert len(user.transactions) == 2
        assert db.session.query(Transaction).count() == 2


def test_balance_after_transactions(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        db.session.commit()
        # checking no of transactions for user tnvrra393@gmail.com
        assert len(user.transactions) == 2
        assert db.session.query(Transaction).count() == 2
        result = db.session.query(functions.sum(Transaction.amount)).scalar()
        assert result == 1000


def test_adding_different_user_transactions(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user1 = User.query.filter_by(email='vishnu@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        user1.transactions = [Transaction(5000, 'CREDIT'), Transaction(-1500, 'DEBIT'), Transaction(-500, 'DEBIT')]
        db.session.commit()
        # checking no of transactions for user tnvrra393@gmail.com
        assert len(user.transactions) == 2
        # checking no of transactions for user vishnu@gmail.com
        assert len(user1.transactions) == 3
        # Check total transactions in tabel
        assert db.session.query(Transaction).count() == 5


def test_deleting_user(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        assert db.session.query(Transaction).count() == 2
        db.session.delete(user)
        assert db.session.query(Transaction).count() == 0


def test_changing_user_transactions_check_balance(application, add_user):
    with application.app_context():
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        user.transactions = [Transaction(3000, 'CREDIT'), Transaction(-2000, 'DEBIT')]
        db.session.commit()
        result = db.session.query(functions.sum(Transaction.amount)).scalar()
        assert result == 1000
        transaction1 = Transaction.query.filter_by(amount=3000).first()
        transaction1.amount = 4000
        db.session.commit()
        result = db.session.query(functions.sum(Transaction.amount)).scalar()
        assert result == 2000
        user.transactions.append(Transaction(2000, 'CREDIT'))
        db.session.commit()
        assert len(user.transactions) == 3
        result = db.session.query(functions.sum(Transaction.amount)).scalar()
        assert result == 4000


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
