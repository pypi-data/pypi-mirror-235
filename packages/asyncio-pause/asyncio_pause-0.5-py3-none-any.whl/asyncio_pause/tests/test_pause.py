#!/usr/bin/env python
#
from __future__ import print_function

import sys
import math
import unittest
from datetime import datetime
from datetime import timedelta
import time
import asyncio

sys.path.insert(0, '..')
import __init__ as asyncio_pause

class TestPauseFor(unittest.TestCase):
    """ Test the delay function of PauseFor """

    def setUp(self):
        # self.event_loop = asyncio.get_event_loop()
        pass

    def test_past(self):
        """ test_past
        Test a time that has already passed
        """

        # Using seconds()
        async def t1():
            start = time.time()
            await asyncio_pause.seconds(-5)
            end = time.time()
            self.assertEqual(int(end - start), 0)
        asyncio.run(t1())

        # Using until()
        async def t2():
            start = time.time()
            await asyncio_pause.until(time.time() - 10)
            end = time.time()
            self.assertEqual(int(end - start), 0)
        asyncio.run(t2())
        

    def test_milliseconds(self):
        """ test_milliseconds
        Test 500 millisecond delay
        """
        async def t1():
            start = time.time()
            await asyncio_pause.milliseconds(500)
            end = time.time()
            diff = end - start
            target = abs(diff - 0.5)

            #
            # True if it's within 0.1 of the target time
            #
            print('Milliseconds came within {0} seconds of 0.5'.format(target))
            valid = (target <= 0.1)
            self.assertTrue(valid)
        asyncio.run(t1())

    def test_seconds(self):
        """ test_seconds
        Test 5 second delay
        """
        async def t1():
            now = time.time()
            await asyncio_pause.seconds(5)
            end = time.time()

            # True if 5 seconds have passed
            diff = int(end - now)
            self.assertEqual(diff, 5)
        asyncio.run(t1())

    def test_time(self):
        """ test_time
        Test 5 second delay
        """
        async def t1():
            now = time.time()
            await asyncio_pause.seconds(5)
            end = time.time()

            # True if 5 seconds have passed
            diff = int(end - now)
            self.assertEqual(diff, 5)
        asyncio.run(t1())

    def test_minutes(self):
        """ test_minutes
        Test 1 minute delay
        """
        async def t1():
            now = time.time()
            await asyncio_pause.minutes(1)
            end = time.time()

            # True if 1 minute has passed
            diff = int((end - now) / 60)
            self.assertEqual(diff, 1)
        asyncio.run(t1())

    def test_weeks(self):
        """ test_weeks
        Use weeks to pause for 2 seconds.
        This should effectively test days() and hours(), since the weeks() goes through both of those functions.
        """
        async def t1():
            now = time.time()
            await asyncio_pause.weeks(float((1.0 / 7.0 / 24.0 / 60.0 / 60.0) * 2.0))
            end = time.time()

            # True if 2 seconds has passed
            diff = int(end - now)
            self.assertEqual(diff, 2)
        asyncio.run(t1())

    def test_datetime(self):
        """ test_datetime
        Test 7 seconds, with a datetime object
        """
        async def t1():
            startDate = datetime.now()
            toDate = startDate + timedelta(seconds=7)
            await asyncio_pause.until(toDate)
            now = datetime.now()

            # True if at least 7 seconds has passed
            diff = now - startDate
            self.assertEqual(diff.seconds, 7)
        asyncio.run(t1())

    def test_timezone(self):
        """ test_datetime
        Test 7 seconds, with a datetime object
        """
        async def t1():
            if sys.version_info[0] >= 3:
                from datetime import timezone
                # Apply a timezone offset, Line Islands Time for fun
                startDate = datetime.now(timezone(timedelta(hours=14), 'LINT'))
                toDate = startDate + timedelta(seconds=7)
                await asyncio_pause.until(toDate)
                now = datetime.now(timezone.utc)

                # True if at least 7 seconds has passed
                diff = now - startDate
                self.assertEqual(diff.seconds, 7)
        asyncio.run(t1())

    def test_timestamp(self):
        """ test_timestamp
        Test 6 seconds, with a unix timestamp
        """
        async def t1():
            toTime = time.time() + 6
            start = time.time()
            await asyncio_pause.until(toTime)

            # True if it came within 0.1 of a second
            end = time.time()
            diff = int(end - start)
            self.assertEqual(diff, 6)
        asyncio.run(t1())

if __name__ == '__main__':
    unittest.main()