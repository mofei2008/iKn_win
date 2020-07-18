from jsonschema import validate

result = {
    "code" : 0,
    "name": "中国",
    "msg": "login success!",
    "password": "aaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "username": "test"
}
#校验数据格式设定
schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "test demo",
    "description": "validate result information",
    "type": "object",
    "properties": {
        "code": {
            "description": "error code",
            "type": "integer"
        },
        "name": {
            "description": "name",
            "type": "string"
        },
        "msg":
        {
            "description": "msg",
            "type": "string"
        },
        # "password":
        # {
        #     "description": "error password",
        #     "maxLength": 20,
        #     "pattern": "^[a-f0-9]{20}$",  # 正则校验a-f0-9的16进制，总长度20
        #     "type": "string"
        # }
    },
    "required": [
        "code","name", "msg", "password"
    ]
}
# {
#     "$schema": "http://json-schema.org/draft-04/schema#",
#     "title": "book info",
#     "description": "some information about book",
#     "type": "object",
#     "properties": {
#         "id": {
#             "description": "The unique identifier for a book",
#             "type": "integer",
#             "minimum": 1
#         },
#         "name": {
#             "type": "string",
#             "pattern": "^#([0-9a-fA-F]{6}$",
#             "maxLength": 6,
#             "minLength": 6
#         },
#         "price": {
#             "type": "number",
#             "multipleOf": 0.5,
#             "maximum": 12.5,
#             "exclusiveMaximum": true,
#             "minimum": 2.5,
#             "exclusiveMinimum": true
#         },
#         "tags": {
#             "type": "array",
#             "items": [
#                 {
#                     "type": "string",
#                     "minLength": 5
#                 },
#                 {
#                     "type": "number",
#                     "minimum": 10
#                 }
#             ],
#             "additionalItems": {
#                 "type": "string",
#                 "minLength": 2
#             },
#             "minItems": 1,
#             "maxItems": 5,
#             "uniqueItems": true
#         }
#     },
#     "minProperties": 1,
#     "maxProperties": 5,
#     "required": ["id","name","price"]
# }
# validate校验, 跟assert断言一个意思
validate(instance=result, schema=schema)

