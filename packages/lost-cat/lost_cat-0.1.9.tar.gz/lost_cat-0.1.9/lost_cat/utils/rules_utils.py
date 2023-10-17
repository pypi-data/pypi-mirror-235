"""A mnodule for the Rule tool code and class"""
import logging
import re

logger = logging.getLogger(__name__)

class RuleEngine():
    """The type of the engine to use to process the phrase"""
    CONTAINS = 1    # the phrase contains the expr
    EQUALS = 2      # the phrase equals the expr
    REGEX = 3       # the regex matches

class RuleState():
    """Constant class to help set the state response"""
    SINGLE = 0      # one shot
    MULTILINE = 1   # read the nect x lines as the value
    UNTIL = 2       # reas the next lines until next rule

class Rule():
    """simple class to wrap the rule
    rules: {
            "idx": <rule id>
            "name": <name for the rule>,
            "engine": "contains" | "equals" | "regex",
            "expr": <expr>,                     #
            "tags": [
                {
                    "key": <key>,               # name of the field to return
                    "value": <value>            # value to use if true
                    "regex": <regex group>      # if regex the regex group to get value from
                                                # use either value or regex
                }
            ],
            "stop": "yes" | "no" # continue or not if true
            "options": {
                "ignorecase": bool
                "flags": <regex or other flags>
                "group": "<name>"               # groups by <name>
                                                # if stop encountered grouped rules don't run
                "priority": int                 # sorts the rules
                "limit": int                    # set the max length of tokens to process
                                                # -1 is do not check
            }
        },
    """
    def __init__(self, name:str,
            idx: int = None,
            engine: RuleEngine = RuleEngine.CONTAINS,
            expr: object = None,
            stop: bool = False,
            state: RuleState = RuleState.SINGLE,
            tags: list = None,
            options: dict = None
        ):
        """Creates the rule """
        self.name = name
        self.idx = idx
        self.engine = engine
        self.options = options

        # break out the options...
        self.ignorecase = self.options.get("ignorecase", True) if self.options is not None else True
        self.flags = self.options.get("flags") if self.options is not None else None
        self.limit = int(self.options.get("limit", -1)) if self.options is not None else -1
        self.priority = int(self.options.get("priority", -1)) if self.options is not None else -1
        self.group = self.options.get("group", "default") if self.options is not None else "default"

        # handle the regex
        if self.engine == RuleEngine.REGEX:
            if isinstance(expr, str):
                igcase = self.options.get("ignorecase", True) if self.options is not None else True
                if igcase is True:
                    self.expr = re.compile(expr, re.IGNORECASE)
                else:
                    self.expr = re.compile(expr)
            elif isinstance(expr, re.Pattern):
                self.expr = expr
            else:
                # bad state...
                # raise error
                pass
        else:
            self.expr = expr

        self.stop = stop
        self.tags = tags if tags is not None else {}
        self.state = state

        if logger.level == logging.DEBUG:
            logger.info("Rule:")
            for vkey, vvalue in vars(self).items():
                logger.info("\t%s: %s", vkey, vvalue)

    def export(self) -> dict:
        data = {}
        options = {}
        for vkey, vvalue in vars(self).items():
            # split out the options...
            if vkey in ["ignorecase", "flags", "limit", "priority", "group", "findall"]:
                options[vkey] = vvalue
            elif vkey == "options":
                for kopt, vopt in options.items():
                    if kopt not in options:
                        options[kopt] = vopt
            elif isinstance(vvalue, re.Pattern):
                data[vkey] = vvalue.pattern
            else:
                data[vkey] = vvalue
        data["options"] = options
        return data

    def run(self, phrase: str) -> dict:
        """Processes the rule against the parsed string
        return dict
            passed: True | False
            results: [key: value]
            stop: True | False"""
        data = {
            "passed": False,
            "tags": {},
            "stop": self.stop,
        }
        if phrase is None or len(phrase) == 0:
            return data

        # check what type of rule to use
        if self.engine == RuleEngine.REGEX:
            #flags = {
            #    "flags": self.flags
            #} if self.flags is not None else {}
            findall = self.options.get("findall", False) if self.options is not None else False

            if findall is True:
                # use the find all to recover alll matchin
                # <TODO: add finall code here>
                if m_findall := self.expr.finditer(phrase):
                    for m in m_findall:
                        for tagvalue in self.tags:
                            tagkey = tagvalue.get("key")
                            if grpkey := tagvalue.get("group"):
                                # use the regex group
                                resvalue = m.group(grpkey)
                            elif grpkey := tagvalue.get("match"):
                                resvalue = phrase
                            else:
                                resvalue = tagvalue.get("value") if "value" in tagvalue else "<missing>"

                            if tagkey in data.get("tags",{}):
                                # make a list
                                if isinstance(data.get("tags",{}).get(tagkey), set):
                                    data["tags"][tagkey].add(resvalue)
                                else:
                                    data["tags"][tagkey] = {data.get("tags",{}).get(tagkey), resvalue}
                            else:
                                data["tags"][tagkey] = resvalue

            elif m := self.expr.match(phrase): #**flags):
                data["passed"] = True
                # populate the values if any
                for tagvalue in self.tags:
                    tagkey = tagvalue.get("key")
                    if grpkey := tagvalue.get("group"):
                        # use the regex group
                        resvalue = m.group(grpkey)
                    elif grpkey := tagvalue.get("match"):
                        resvalue = phrase
                    else:
                        resvalue = tagvalue.get("value") if "value" in tagvalue else "<missing>"

                    if tagkey in data.get("tags",{}):
                        # make a list
                        if isinstance(data.get("tags",{}).get(tagkey), set):
                            data["tags"][tagkey].add(resvalue)
                        else:
                            data["tags"][tagkey] = {data.get("tags",{}).get(tagkey), resvalue}
                    else:
                        data["tags"][tagkey] = resvalue

        elif self.engine == RuleEngine.CONTAINS:
            if self.ignorecase is True:
                if self.expr.lower() in phrase.lower():
                    data["passed"] = True
            else:
                if self.expr == phrase:
                    data["passed"] = True
            # populate the values if any
            if data.get("passed") is True:
                for tagvalue in self.tags:
                    tagkey = tagvalue.get("key")
                    resvalue = tagvalue.get("value") if "value" in tagvalue else "<missing>"

                    if tagkey in data.get("tags",{}):
                        # make a list
                        if isinstance(data.get("tags",{}).get(tagkey), set):
                            data["tags"][tagkey].add(resvalue)
                        else:
                            data["tags"][tagkey] = {data.get("tags",{}).get(tagkey), resvalue}
                    else:
                        data["tags"][tagkey] = resvalue

        elif self.engine == RuleEngine.EQUALS:
            #
            if self.ignorecase is True:
                if self.expr.lower() in phrase.lower():
                    data["passed"] = True
            else:
                if self.expr == phrase:
                    data["passed"] = True
            # populate the values if any
            if data.get("passed") is True:
                for tagvalue in self.tags:
                    tagkey = tagvalue.get("key")
                    resvalue = tagvalue.get("value") if "value" in tagvalue else "<missing>"

                    if tagkey in data.get("tags",{}):
                        # make a list
                        if isinstance(data.get("tags",{}).get(tagkey), set):
                            data["tags"][tagkey].add(resvalue)
                        else:
                            data["tags"][tagkey] = {data.get("tags",{}).get(tagkey), resvalue}
                    else:
                        data["tags"][tagkey] = resvalue

        # <TODO: add the conditional and state rules here...

        return data

class RulesTool:
    """ manages and runs the rules against a
    string
    """

    # instatitate as a class variable
    name = "names"
    version = "0.0.1"

    def __init__(self) -> None:
        self.rules = []
        self.groups = {}

    def add_rule(self, rule: Rule):
        """Adds a regex to the class"""
        if rule.group not in self.groups:
            self.groups[rule.group] = {
                "rules": [],
                "enabled": True
            }
        self.groups[rule.group]["rules"].append(rule)
        self.rules.append(rule)

    def export(self) -> list:
        """Exports the rules as a string dict"""
        data = []
        for _, ruleset in self.groups.items():
            for rule in ruleset.get("rules",[]):
                data.append(rule.export())
        return data

    def run(self, phrases: list):
        """process the rules against each line and
        return the result"""
        # reset the rules
        for group, ruleset in self.groups.items():
            self.groups[group]["enabled"] = True

        # run the groups
        results = []
        for phrase in phrases:
            # now to process the groups...
            for group, ruleset in self.groups.items():
                if not ruleset.get("enabled", True):
                    continue

                for rule in ruleset.get("rules",[]):
                    # check the limit
                    if rule.limit > -1 and len(phrase.split()) > rule.limit:
                        continue

                    # run the rule
                    result = rule.run(phrase=phrase)
                    passed = result.get("passed", False)

                    if passed is True:
                        results.append({
                            "rule": rule,
                            "phrase": phrase,
                            "result": {
                                "passed": passed,
                                "stop": rule.stop,
                                "tags": result.get("tags")
                            }
                        })

                    # if rule passed and stop is set
                    # diable the rule, and
                    if passed and rule.stop:
                        self.groups[group]["enabled"] = False
                        break

        return results
