import json

data=None

print("请求：")
print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': ')))