import json
from csv_empty_pruner import transform
def test_transform():
    value='[{"a":""},{"a":"x"}]'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert '"x"' in json.dumps(result,ensure_ascii=False)
