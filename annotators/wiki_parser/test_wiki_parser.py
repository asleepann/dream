import requests


def main():
    url = 'http://0.0.0.0:8077/model'

    request_data = [{"parser_info": ["find_top_triplets"],
                     "query": [[{"entity_substr": "Jürgen Schmidhuber", "entity_ids": ["Q92735"]}]]}]

    gold_results = [[{'entities_info':
                     {'Jürgen Schmidhuber': {'country of sitizenship': [['Q183', 'Germany']],
                                             'date of birth': [['"+1963-01-17^^T"', '17 January 1963']],
                                             'instance of': [['Q5', 'human']],
                                             'occupation': [['Q15976092', 'artificial intelligence researcher'],
                                                            ['Q1622272', 'university teacher'],
                                                            ['Q82594', 'computer scientist']]},
                      'entity_substr': 'Jürgen Schmidhuber'},
                      'topic_skill_entities_info': {}}]]

    count = 0
    for data, gold_result in zip(request_data, gold_results):
        result = requests.post(url, json=data).json()
        if result == gold_result:
            count += 1
    else:
        print(f"Got {result}, but expected: {gold_result}")

    if count == len(request_data):
        print('Success')


if __name__ == '__main__':
    main()
