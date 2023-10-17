import json
from typing import Dict, List, Union, Any, Callable
from argparse import ArgumentParser
from pprint import pprint


def match_dict(pre_list: List[Dict[str, Any]],
               post_list: List[Dict[str, Any]],
               index_keys: List[str],
               compare_keys: List[Union[str, None]] = None,
               compare_func: Union[Callable, None] = None,):
    """
    Match pre/post dict list by given index keys, and compare the given compare keys by given compare function
    :param pre_list: List of dict
    :param post_list: List of dict
    :param index_keys: List of keys which will be used as index
    :param compare_keys: List of keys which will be used as compare keys
    :param compare_func: Function which will be used to compare the given compare keys
    :return: List of dict which contains pre/post items and compare result
    """
    # construct pre/post mapping
    pre_mapping = dict()
    post_mapping = dict()

    for pre_item in pre_list:
        key = tuple(pre_item.get(key, None) for key in index_keys)
        pre_mapping[key] = pre_item

    for post_item in post_list:
        key = tuple(post_item.get(key, None) for key in index_keys)
        post_mapping[key] = post_item

    result_list = list()
    # check all pre item
    for pre_key, pre_item in pre_mapping.items():
        post_item = post_mapping.get(pre_key, {})
        new_item = dict()
        keys = pre_item.keys()

        for key in keys:
            new_item[f'pre_{key}'] = pre_item[key]
            new_item[f'post_{key}'] = post_item.get(key, None)
        result_list.append(new_item)

    # check post item which not in pre
    for post_key, post_item in post_mapping.items():
        if post_key not in pre_mapping:
            new_item = dict()
            keys = post_item.keys()
            for key in keys:
                new_item[f'pre_{key}'] = None
                new_item[f'post_{key}'] = post_item[key]
            result_list.append(new_item)

    if not compare_keys:
        return result_list

    # add result
    def _default_compare_func(_item: dict, _chk_keys: List[str]):
        """
        default compare function: just check the if the given keys/values are equal
        """
        _result = 'PASSED'
        for _chk_key in _chk_keys:
            if _item.get(f'pre_{_chk_key}') != _item.get(f'post_{_chk_key}'):
                _result = "FAILED"
                break
        _item['result'] = _result

    if not compare_func:
        compare_func = _default_compare_func
    for result_item in result_list:
        compare_func(result_item, compare_keys)
    return result_list


def main():
    parser = ArgumentParser()
    parser.add_argument('-p', '--pre', type=str, required=True, help='Pre data file')
    parser.add_argument('-P', '--post', type=str, required=True, help='Post data file')
    parser.add_argument('-i', '--index', nargs='+', required=True, help='Index keys')
    parser.add_argument('-c', '--compare', nargs='+', required=True, help='Compare keys')
    args = parser.parse_args()
    pre_file = args.pre
    post_file = args.post
    index_keys = args.index
    compare_keys = args.compare

    with open(pre_file, 'r') as f:
        pre_list = json.load(f)

    with open(post_file, 'r') as f:
        post_list = json.load(f)

    result_list = match_dict(pre_list, post_list, index_keys, compare_keys)
    pprint(result_list)


def test():
    PRE_LIST = [
        {'name': "Alice", "age": 18, "gender": "Female", "dept": "IT"},
        {'name': "Bob", "age": 19, "gender": "Male", "dept": "Sales"},
        {'name': "Cindy", "age": 20, "gender": "Female", "dept": "IT"},
    ]

    POST_LIST = [
        {'name': "Alice", "age": 18, "gender": "Female", "dept": "IT"},
        {'name': "Bob", "age": 29, "gender": "Male", "dept": "Sales"},
        {'name': "David", "age": 21, "gender": "Male", "dept": "Marketing"},
    ]

    index_keys = ['name', 'gender']
    compare_keys = ['age', 'dept']

    result_list = match_dict(PRE_LIST, POST_LIST, index_keys, compare_keys)
    pprint(result_list)


if __name__ == '__main__':
    main()
