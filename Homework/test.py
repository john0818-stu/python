import os
import unittest
import tempfile

from main import app
import MongoData , MySQLData

class Test( unittest.TestCase ) :

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        MySQLData.MySQLData()
        MongoData.MongoData( "runoobdb" , "sites" )
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    
    def test_empty_db(self):
        rv = self.app.get('/')
        assert "Mongo2MySQL" in str( rv.data )
    
        rv = self.app.get('/findWally')
        assert "Title" in str( rv.data )
        
        rv = self.app.get('/findNews')
        assert "find" in str( rv.data )

        rv = self.app.get('/save_mongo')
        assert "Title" in str( rv.data )

        rv = self.app.get('/Mongo2MySQL')
        assert "key : value" in str( rv.data )

if __name__ == "__main__" :
    unittest.main() 