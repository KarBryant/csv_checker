from csv_checker.adapters.json_serializer import JSONSerializer
import json

def test_serializer(basic_results):
    serializer = JSONSerializer()
    json_dump = serializer.serialize(basic_results)
    parsed = json.loads(json_dump)

    assert isinstance(json_dump,str)
    assert parsed["column_count"] == 3
    assert parsed["row_count"] == 2




