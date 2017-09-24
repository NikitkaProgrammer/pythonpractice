'''
Программа переводит возвращаемое значение функции в json.
Можно написать несколько таких декораторов и выбирать в каком
формате возвращать данные.
'''
import json
from functools import wraps #отлично работает и без этого, но пусть будет

def to_json(function_to_json):
    @wraps(function_to_json)
    def wrapper(*args, **kwds):
        return json.dumps(function_to_json(*args, **kwds))
    return wrapper

@to_json
def get_data():
  return {
    'data': 42 #левое значение 
  }
