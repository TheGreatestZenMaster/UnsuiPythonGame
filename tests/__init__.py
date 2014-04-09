from mock import Mock
import urllib2

### package-level setup and teardown for nosetests ###
def setup_package():
   ## prevent any real http requests from going out via monkey-patching ##

   # replace module methods with our mock
    urllib2.Request = Mock()
    urllib2.urlopen = Mock()
    
def teardown_package():
    # put everything back where it was by re-importing
    import urllib2
