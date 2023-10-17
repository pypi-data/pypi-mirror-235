"""A test case for the path utils module"""
import logging
import re
import unittest
from lost_cat.utils.rules_utils import Rule, RuleState, RuleEngine, RulesTool

logger = logging.getLogger(__name__)

class TestRulesModule(unittest.TestCase):
    """A container class for the rule module test cases"""


    @classmethod
    def setUpClass(cls):
        """ Set up for Trie Unit Tests..."""
        cls.phrases = [
            "Top Drawer:	High quality, exceptional; something that's very valuable.",
            "A Chip on Your Shoulder:	Being angry about something that happened in the past.",
            "Par For the Course:	What you would expect to happen; something normal or common.",
            "In a Pickle:	Being in a difficult predicament; a mess; an undesirable situation.",
            "Heads Up:	Used as an advanced warning. To become keenly aware.",
            "On the Same Page:	Thinking alike or understanding something in a similar way with others.",
            "Elvis Has Left The Building:	Something that is all over.",
            "Keep Your Eyes Peeled:	To be watchful; paying careful attention to something.",
            "Rain on Your Parade:	To spoil someone's fun or plans; ruining a pleasurable moment",
            "A Hundred and Ten Percent:	Someone who gives more than what seems to be possible.",
            "Limit:	something that's very valuable.",
        ]

    @classmethod
    def tearDownClass(cls):
        """ Tear down for Rule Unit Tests"""
        pass

    def test_rule(self):
        """check the simple rule class"""

        rule = Rule(
            name="Has Something",
            idx=1,
            engine=RuleEngine.CONTAINS,
            expr="something",
            tags=[{
                "key": "somthing",
                "value": True,
                # "regex"
            }],
            stop=True,
            state=RuleState.SINGLE,
            options={
                "ignorecase": True
            }
        )

        result = rule.run(phrase=self.phrases[2])
        assert result.get("passed", False) is True
        print(result)

        result = rule.run(phrase=self.phrases[3])
        assert result.get("passed", False) is False
        print(result)

    def test_rules_stop(self):
        """Check the runner against a sequence of rules"""

        rule = Rule(idx=1,
            name="Has Advanced",
            engine=RuleEngine.CONTAINS,
            expr="advanced",
            tags=[{
                "key": "advanced",
                "value": True,
                # "regex"
            }],
            stop=True,
            state=RuleState.SINGLE,
            options={
                "ignorecase": True
            }
        )

        rules = RulesTool()
        rules.add_rule(rule=rule)

        results = rules.run(phrases=self.phrases)

        assert len(results) == 1
        print(results)

    def test_rules(self):
        """Check the runner against a sequence of rules"""

        rule = Rule(idx=1,
            name="Has Something",
            engine=RuleEngine.CONTAINS,
            expr="Something",
            tags=[{
                "key": "advanced",
                "value": True,
                # "regex"
            }],
            state=RuleState.SINGLE,
            options={
                "ignorecase": True
            }
        )

        rules = RulesTool()
        rules.add_rule(rule=rule)

        results = rules.run(phrases=self.phrases)

        assert len(results) == 7
        print(results)

    def test_rules_limit(self):
        """Check the runner against a sequence of rules"""

        rule = Rule(idx=1,
            name="Has Something",
            engine=RuleEngine.CONTAINS,
            expr="Something",
            tags=[{
                "key": "advanced",
                "value": True,
                # "regex"
            }],
            state=RuleState.SINGLE,
            options={
                "ignorecase": True,
                "limit": 6
            }
        )

        rules = RulesTool()
        rules.add_rule(rule=rule)

        results = rules.run(phrases=self.phrases)

        assert len(results) == 1
        print(results)
