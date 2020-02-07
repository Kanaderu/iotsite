from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    """ we create a command wait_for_db to check if database is
    available before running server. Here we test if this command"""

    # check if the command works when db is available
    def test_wait_for_db_ready(self):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # check if command works when db is not connected
    # by default, we ll have sleep function to wait for 1s if database is not available
    # we dont want this sleep to wait for this test
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # make the patch return error for first five calls
            # and return true on sixth call
            gi.side_effect = [OperationalError]*5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
