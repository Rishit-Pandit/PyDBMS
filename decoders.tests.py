import unittest
from utils import Table
import decoders as dec


data = [
	  [
	    ['CREATE', 'TABLE', 'STUDENTS', '(', 'NAME', 'VARCHAR', 'CLASS', 'INT', ')'], 
	    { 
	      'NAME': { 'Type': 'VARCHAR', 'Values': [], 'Params': [] }, 
	      'CLASS': { 'Type': 'INT', 'Values': [], 'Params': [] } 
	    }
	  ],
	  [
	    ['CREATE', 'TABLE', 'STORE', '(', 'ITEM', 'VARCHAR', 'QTY', 'INT', 'AMOUNT', 'FLOAT', ')'], 
	    { 
	      'ITEM': { 'Type': 'VARCHAR', 'Values': [], 'Params': [] }, 
	      'QTY': { 'Type': 'INT', 'Values': [], 'Params': [] }, 
	      'AMOUNT': { 'Type': 'FLOAT', 'Values': [], 'Params': [] }
	    }
	  ],
	]


class TestDecoders(unittest.TestCase):

	def test_create_table(self):
		for [command, table] in data:
			self.assertEqual(dec.createTable(command[2], command[3:]).columns, table)


if __name__ == '__main__':
    unittest.main()


