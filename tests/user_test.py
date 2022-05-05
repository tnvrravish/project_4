import logging

from app import db
from app.db.models import User, Song, Transaction
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('tnvrra393@gmail.com', 'spiderCLAW')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        #db.session.commit()
        #assert that we now have a new user
        #assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='tnvrra393@gmail.com').first()
        # log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'tnvrra393@gmail.com'
        #this is how you get a related record ready for insert
        user.songs= [Song("test","smap","rap",2012),Song("test2","te","pop",2011)]
        user.transactions = [Transaction(2000,'DEBIT'), Transaction(-2000,'CREDIT')]

        #commit is what saves the songs
        db.session.commit()
        log.info(Transaction.query.filter_by(id = 1).first())
        assert db.session.query(Song).count() == 2
        assert db.session.query(Transaction).count() == 2

        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        #changing the title of the song
        song1.title = "SuperSongTitle"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0



