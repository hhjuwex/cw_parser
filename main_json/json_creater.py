import re
import importlib
import json
from datetime import datetime

import core_parser

def split_reports(reports: str) -> list:
    list_of_lines = reports.split('\n')
    list_of_reports = []
    report = []
    fl = False
    for line in list_of_lines:
        if re.match(r"^#[1-9]\d*\s+(?:[1-9]|[12]\d|3[01])\b", line):
            if fl:
                list_of_reports.append(report)
                report = []
            else:
                fl = True
        report.append(line)
    list_of_reports.append(report)
    return list_of_reports

def import_context(context: str):
    module_path = f"modular_parsers.{context}.parser_{context}"
    module = importlib.import_module(module_path)
    return module


def create_json(reports: list, context: str, version: str, source: str) -> str:
    metadata = {
        "schema_version": version,
        "generation_time": datetime.now().strftime("%H:%M %d.%m.%Y"),
        "source": source
    }
    local_parser = import_context(context)


    with open("parsed.json",'w') as jsn:




#"schema_version": version,
#"generation_time": datetime.now().strftime("%H:%M %d.%m.%Y")