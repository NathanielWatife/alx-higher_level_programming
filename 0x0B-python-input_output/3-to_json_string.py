#!/usr/bin/python3
""" Definesa string to JSON function"""
import json


def to_json_string(my_obj):
    """Return the JSON representaion of astring onject"""
    return json.dumps(my_obj)
