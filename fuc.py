import json

data={"RecordCountInfo": {"SubdomainCount": 4, "ListCount": 4, "TotalCount": 4}, "RecordList": [{"RecordId": 1565164307, "Value": "felix.dnspod.net.", "Status": "ENABLE", "UpdatedOn": "2023-08-10 01:07:49", "Name": "@", "Line": "默认", "LineId": "0", "Type": "NS", "Weight": None, "MonitorStatus": "", "Remark": "", "TTL": 86400, "MX": 0, "DefaultNS": None}, {"RecordId": 1565164308, "Value": "agatha.dnspod.net.", "Status": "ENABLE", "UpdatedOn": "2023-08-10 01:07:49", "Name": "@", "Line": "默认", "LineId": "0", "Type": "NS", "Weight": None, "MonitorStatus": "", "Remark": "", "TTL": 86400, "MX": 0, "DefaultNS": None}, {"RecordId": 1565168996, "Value": "123.175.168.148", "Status": "ENABLE", "UpdatedOn": "2023-08-17 20:38:36", "Name": "@", "Line": "默认", "LineId": "0", "Type": "A", "Weight": None, "MonitorStatus": "", "Remark": "", "TTL": 600, "MX": 0, "DefaultNS": None}, {"RecordId": 1565168997, "Value": "123.175.168.148", "Status": "ENABLE", "UpdatedOn": "2023-08-17 20:38:46", "Name": "www", "Line": "默认", "LineId": "0", "Type": "A", "Weight": None, "MonitorStatus": "", "Remark": "", "TTL": 600, "MX": 0, "DefaultNS": None}], "RequestId": "14426139-c266-4398-a67d-0afdabd77099"}

print("请求：")
print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': ')))