from datetime import datetime
import logging
import json
import os
import pandas as pd

from dotenv import load_dotenv
from tqdm import tqdm

from lost_cat.utils.path_utils import get_filename
from lost_cat.utils.rules_utils import Rule, RulesTool

logger = logging.getLogger(__name__)
load_dotenv()

def main(config: dict):
    """This will run a core sample of files"""
    # first load the rules...
    rules = RulesTool()
    if rules_paths := config.get("paths", {}).get("rules"):
        rules = load_rules(rules_paths=rules_paths)
    if len(rules.rules) == 0:
        print("Not rules given, exiting!")
        return

    # check if the export has been defined...
    if export_paths := config.get("paths", {}).get("exports"):
        # run the export for each path...
        export_rules(rules=rules, export_paths=export_paths)

    # now to see if any source information needs to have rules run against them
    with tqdm(total=len(config.get("paths", {}).get("sources",[])), desc="Processing Sources:") as spbar:
        for file_obj in config.get("paths", {}).get("sources",[]):
            data = fetch_phrases(file_obj=file_obj)
            for group, phrases in data.items():
                logger.info("Group: %s -> %s", group, len(phrases))
                results = rules.run(phrases)
                logger.info("Results:")
                for result in results:
                    logger.info("\t%s", result)

            spbar.update(1)

def load_rules(rules_paths: list) -> RulesTool:
    rules = RulesTool()
    rules_data = []
    with tqdm(total=len(rules_paths), desc="Loading rules from paths:") as rpbar:
        for file_obj in rules_paths:
            # load each rule into the engine
            rpbar.update(1)
            rule_path = get_filename(file_obj)
            if not os.path.exists(rule_path):
                logger.warning("Missing rule path: %s", rule_path)
                continue
            if file_obj.get("ext","").lower() == ".json":
                with open(rule_path, 'r', encoding="utf-8") as fp:
                    rule_data = json.load(fp=fp)

            elif file_obj.get("ext","").lower() in [".xlsx", ".xls", ".csv", ".tsv"]:
                # open in excel, load into a json object
                if sheet_name := file_obj.get("sheet"):
                    df = pd.read_excel(io=rule_path, sheet_name=sheet_name)
                else:
                    df = pd.read_excel(io=rule_path)

                # pivot to json
                df_json = df.to_json(orient="table")
                df_data = json.loads(df_json)
                logger.info("Rules Excel: %s", df_data)
                rule_data = {"rules": df_data.get("data",[])}
                logger.info("Rules Data: %s", rule_data)
            else:
                # unknown file
                logger.error("Unhandled file format for rules: %s", rule_path)
                raise ValueError("Unhandled file format for rules", rule_path)

            rules_data.append(rule_data)

    for idx, rule_defs in enumerate(rules_data):
        with tqdm(total=len(rule_defs.get("rules",[])), desc=f"Loading ruleset {idx}:") as dpbar:
            for r in rule_defs.get("rules",[]):
                dpbar.update(1)
                ruledict = {}

                for fld in ["name", "idx", "engine", "expr", "stop", "tags", "state", "options"]:
                    if value := r.get(fld):
                        ruledict[fld] = value

                for fld in ['options', 'tags']:
                    if isinstance(ruledict[fld], str):
                        logger.info("Rule: %s -> %s", fld, ruledict[fld])
                        ruledict[fld] = json.loads(ruledict[fld])

                rule = Rule(**ruledict)
                rules.add_rule(rule)
                logger.info("Rules: Load: %s", ruledict)

    return rules

def export_rules(rules: RulesTool, export_paths: list) -> None:
    """Will export the rules provided to the avariety of formats
    Currently handle json, or excel

    """
    data = []
    for group, ruleset in rules.groups.items():
        for rule in ruleset.get("rules",[]):
            # check the limit
            data.append(rule.export())

    #load into a df
    df = pd.DataFrame(data=data)
    logger.info(df.size)

    with tqdm(total=len(export_paths), desc="Exporting rules:") as epbar:
        for exp_obj in export_paths:
            exp_path = get_filename(exp_obj)
            if exp_obj.get("ext","") == ".json":
                # dump to json
                with open(exp_path, 'w', encoding="utf-8") as fp:
                    fp.write(json.dumps(data, indent=4))

            elif exp_obj.get("ext","") == ".xlsx":
                # dump to excel
                df.to_excel(exp_path)

            elif exp_obj.get("ext","") == ".xlsx":
                # dump to excel
                df.to_csv(exp_path)

            epbar.update(1)

def fetch_phrases(file_obj: dict) -> list:
    """Will open the provided file and retgurn a dataset
    file_obj: dict
            {
                "root": str
                "folders": [str, str, ...]
                "name": str
                "ext": str
                "sheet": str                    # if excel
                "fields": [str, str, ...]       # if table,
                                                # else return concatenated rows
                "group": [str, str, ...]        # if table,
                                                # else return concatenated rows
                "phrase": [str, str, ...]       # if table,
                                                # else return concatenated rows
            }

    returns
    -------
    dict
            {
                "<group>" : [
                    {
                        <label>: <data>
                        ...
                    }
                ],
                ...
            }
    """
    file_path = get_filename(file_dict=file_obj)
    data = {}
    df = None

    if file_obj.get("ext").lower() == ".xlsx":
        # process the excel file
        if sheet_name := file_obj.get("sheet"):
            df = pd.read_excel(io=file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(io=file_path)

    elif file_obj.get("ext").lower() == ".csv":
        # process the csv file
        df = pd.read_csv(file_path)
    elif file_obj.get("ext").lower() == ".tsv":
        # process the csv file
        df = pd.read_csv(file_path, sep="\t")
    else:
        # process as a text file and line...
        pass

    if isinstance(df,pd.DataFrame):
        print(df.shape)
        cols = []
        groups = []
        if group_cols := file_obj.get("group"):
            df["group"] = df[group_cols].agg('-'.join, axis=1)
            cols.append("group")
            groups = list(df["group"].unique())

        if phrase_col := file_obj.get("phrase"):
            df['phrase'] = df[phrase_col]
            cols.append("phrase")
        else:
            # join all fields together
            pass

        if len(groups) > 1:
            for dkey in groups:
                data[dkey] = list(df[df["group"] == dkey]["phrase"])
        else:
            # dump as list
            data = {
                "default": list[df["phrase"]]
            }

    return data

if __name__ == '__main__':
    import argparse

    nb_name = "lost-cat.rules"
    if not os.path.exists("logs"):
        os.mkdir("logs")

    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d.%H%M%S"))
    logpath = os.path.join("logs", f"{_logname}.log")
    if os.path.exists(logpath):
        os.remove(logpath)

    parser = argparse.ArgumentParser(
                        prog='Rules Engine Exporter and Runner',
                        description='Will load the rules and run them agains the supplied information',
                        epilog='for help please email support@thoughtswinsystems.com')

    parser.add_argument('--config', '-c',
                        dest='config_path',
                        help='sets the config path to use, otherwise uses default location.',
                        default=os.path.expandvars(os.path.join(".", *["config", "rules_config.json"])))

    parser.add_argument('-d', '--debug',
                        help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.INFO)

    args = parser.parse_args()

    logging.basicConfig(filename=logpath, level=args.loglevel)

    if not os.path.exists("config"):
        os.mkdir("config")
    config_data = None

    if os.path.exists(args.config_path):
        # load the config
        with open(args.config_path, mode="r", encoding="utf-8") as fpointer:
            config_data = json.load(fpointer)

    if config_data is None:
        config_data = {
            "paths":{
                "sources":[
                    {
                        "root": '.',
                        "folders": ["data"]
                    }
                ],
                "rules": [
                    {
                        "root": ".",
                        "folders": ["config"],
                        "name": "rules",
                        "ext": ".json"
                    }
                ],
                "exports": [
                    {
                        "root": ".",
                        "folders": ["data"],
                        "name": "rules",
                        "ext": ".xlsx"
                    }
                ],
                "ignore": [],
                "flags": {
                    "subs": False
                },
            },
        }

        # save this config file
        logger.warning("New config file created!")
        with open(args.config_path, 'w', encoding="utf-8") as fp:
            fp.write(json.dumps(config_data, indent=4))

    main(config=config_data)
