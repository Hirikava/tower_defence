import unittest

from Game.Object.Other.Timer import Timer
class TimerActionTest(unittest.TestCase):

    def test_ActionWillDownTimerBelowZeroIfDontUpdateIt(self):
        timer = Timer(100)
        action = timer.get_actions()[0]
        for i in range (0,110):
            action.act(1)
        self.assertEqual(-10,timer.get_time())

    def test_ActionWillNotDownTimerBelowZeroIfUpdateAction(self):
        timer = Timer(100)
        for i in range (0,110):
            for action in timer.get_actions():
                action.act(1,[],[],[timer])
        self.assertEqual(0,timer.get_time())