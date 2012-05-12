
import unittest
from logmdc.storage import MappedContext

class LogMDCTest(unittest.TestCase):

    def setUp(self):
        self.context = MappedContext()

    def tearDown(self):
        self.context = None

    def test_get_empty(self):
        self.assertEquals(None, self.context.get('foo'))

    def test_get_default(self):
        self.assertEquals('DEFAULT', self.context.get('foo', 'DEFAULT'))

    def test_put(self):
        self.context.put("foo", "bar")

        self.assertEquals("bar", self.context.get("foo"))

    def test_remove(self):
        self.context.put("foo", "bar")
        self.context.remove("foo")

        self.assertEquals(None, self.context.get('foo'))
