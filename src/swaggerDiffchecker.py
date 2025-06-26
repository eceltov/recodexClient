import yaml
import os
import sys
from deepdiff import DeepDiff

def read_swagger(path: str):
    if not os.path.exists(path):
        raise Exception(f"The path '{path}' does not point to a file.")

    with open(path, "r") as file:
        content = yaml.safe_load(file)
        return content

def find_different_paths(old_swagger: dict, new_swagger: dict):
    diff = DeepDiff(old_swagger["paths"], new_swagger["paths"])
    return diff.affected_root_keys

def split_dict(d: dict):
    literals = []
    objects = []
    for key, value in d.items():
        if isinstance(value, dict) or isinstance(value, list):
            objects.append(key)
        else:
            literals.append(key)
    return (literals, objects)

def split_keys(old_keys: list[str], new_keys: list[str], old_dict: dict, new_dict: dict):
    key_stats = {}
    for key in old_keys:
        if key not in new_keys:
            key_stats[key] = "removed"
        elif old_dict[key] == new_dict[key]:
            key_stats[key] = "kept"
        else:
            key_stats[key] = "modified"
    for key in new_keys:
        if key not in old_keys:
            key_stats[key] = "added"
    return key_stats

def split_parameters(old_parameters: list[dict], new_parameters: list[dict]):
    old_names = []
    new_names = []
    for param in old_parameters:
        old_names.append(param["name"])
    for param in new_parameters:
        new_names.append(param["name"])

    param_stats = {}
    for name in old_names:
        if name not in new_names:
            param_stats[name] = "removed"
        else:
            param_stats[name] = "kept"
    for name in new_names:
        if name not in old_names:
            param_stats[name] = "added"
    return param_stats

def split_lists(old_list: list, new_list: list):
    removed = []
    added = []
    kept = []

    for value in old_list:
        if value in new_list:
            kept.append(value)
        else:
            removed.append(value)
    for value in new_list:
        if value not in old_list:
            added.append(value)

    return (removed, added, kept)

def print_indented_kept(line: str, indentation: int):
    print(" " * (indentation + 2) + line)

def print_indented_added(line: str, indentation: int):
    print("+" + " " * (indentation + 1) + line)

def print_indented_removed(line: str, indentation: int):
    print("-" + " " * (indentation + 1) + line)

def get_param(params: list[dict], name: str):
    for param in params:
        if param["name"] == name:
            return param
    raise Exception(f"Parameter '{name}' not found")

def to_yaml_diff(label: str, old_obj: dict|list, new_obj: dict|list, indentation: int):
    # print the key under which the object is listed
    if bool(old_obj) and bool(new_obj):
        print_indented_kept(f"{label}:", indentation - 2)
    elif not bool(old_obj):
        print_indented_added(f"{label}:", indentation - 2)
    else:
        print_indented_removed(f"{label}:", indentation - 2)

    # check whether the objects are lists of dicts
    if isinstance(old_obj, list) or isinstance(new_obj, list):
        if not (isinstance(old_obj, list) and isinstance(new_obj, list)):
            raise Exception("Both parameters have to either be lists, or dicts")
        handle_lists(label, old_obj, new_obj, indentation)
    else:
        handle_dicts(old_obj, new_obj, indentation)

def handle_lists(label: str, old_list: list, new_list: list, indentation: int):
    if label == "parameters":
        param_stats = split_parameters(old_list, new_list)
        for param in old_list:
            name = param["name"]
            status = param_stats[name]
            if status == "kept":
                print_indented_kept("-", indentation - 2)
                handle_dicts(param, get_param(new_list, name), indentation)
            elif status == "removed":
                print_indented_removed("-", indentation - 2)
                handle_dicts(param, {}, indentation)
        for param in new_list:
            name = param["name"]
            status = param_stats[name]
            if status == "added":
                print_indented_added("-", indentation - 2)
                handle_dicts({}, param, indentation)
    else:
        removed, added, kept = split_lists(old_list, new_list)
        for value in kept:
            print_indented_kept("-", indentation - 2)
            print_indented_kept(value, indentation)
        for value in removed:
            print_indented_removed("-", indentation - 2)
            print_indented_removed(value, indentation)
        for value in added:
            print_indented_added("-", indentation - 2)
            print_indented_added(value, indentation)

def handle_dicts(old_dict: dict, new_dict: dict, indentation: int):
    old_literals, old_objects = split_dict(old_dict)
    new_literals, new_objects = split_dict(new_dict)

    key_stats = split_keys(old_literals, new_literals, old_dict, new_dict)
    for key, status in key_stats.items():
        if status == "kept":
            print_indented_kept(f"{key}: {old_dict[key]}", indentation)
        elif status == "removed":
            print_indented_removed(f"{key}: {old_dict[key]}", indentation)
        elif status == "added":
            print_indented_added(f"{key}: {new_dict[key]}", indentation)
        else:
            print_indented_removed(f"{key}: {old_dict[key]}", indentation)
            print_indented_added(f"{key}: {new_dict[key]}", indentation)

    obj_stats = split_keys(old_objects, new_objects, old_dict, new_dict)
    for key, status in obj_stats.items():
        # the status will be modified due to object comparison
        if status == "removed" or status == "modified" or status == "kept":
            if isinstance(old_dict[key], dict):
                to_yaml_diff(key, old_dict[key], new_dict.get(key, {}), indentation + 2)
            else:
                to_yaml_diff(key, old_dict[key], new_dict.get(key, []), indentation + 2)
        else:
            if isinstance(new_dict[key], dict):
                to_yaml_diff(key, {}, new_dict[key], indentation + 2)
            else:
                to_yaml_diff(key, [], new_dict[key], indentation + 2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception(f"Expected 2 parameters (compared swagger paths), but {len(sys.argv) - 1} were provided.")

    old_swagger = read_swagger(sys.argv[1])
    new_swagger = read_swagger(sys.argv[2])
    
    # paths = find_different_paths(old_swagger, new_swagger)
    # for path in paths:
    #     print("```diff")
    #     to_yaml_diff(path, old_swagger["paths"].get(path, {}), new_swagger["paths"].get(path, {}), 0)
    #     print("```")

    count = 0
    for key, path in new_swagger["paths"].items():
        for method, schema in path.items():
            count += 1

    print(count)
