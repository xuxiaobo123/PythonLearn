import json
from jsonpath_rw import jsonpath, parse

jsonStr = '''
{
    "leihou": {
        "testers": [
            {
                "id": "101",
                "name": "xxb",
                "addr": "广东汕头",
                "age": 27
            },
             {
                "id": "102",
                "name": "yzp",
                "age": 28
            },
            {
                "id": "103",
                "name": "zxr",
                "addr": "广东韶关",
                "age": 16
            },
             {
                "id": "104",
                "name": "pss",
                "addr": "湖南",
                "age": 20
            }
        ],
        "corder": [
            {
                "id": "105",
                "name": "zrb",
                "age": 17
            },
             {
                "id": "106",
                "name": "yw",
                "age": 25
            }
        ]
    },
 "avg": 25
} 
'''

# 3:加载为json对象
json_obj = json.loads(jsonStr)

# 4：采用parse创建jsonpath对象（得到所有的testers的name）
jsonpath_expr = parse('$.leihou.testers[*].name')

# 5：通过jsonPath检索json后返回匹配的数据，类型是DatumInContext的list
datumInContexts = jsonpath_expr.find(json_obj)
# 采用列表推导式检索出所有匹配的值
values = [datum.value for datum in datumInContexts]
print(values)
# 输出结果为：['xxb', 'yzp', 'zxr', 'pss']

# 案例2：提取索引为3的testers的name
jsonpath_expr = parse('$.leihou.testers[2].name')
datumInContexts = jsonpath_expr.find(json_obj)
print(datumInContexts)
values = [datum.value for datum in datumInContexts]
print(values)
# 结果为：['zxr']