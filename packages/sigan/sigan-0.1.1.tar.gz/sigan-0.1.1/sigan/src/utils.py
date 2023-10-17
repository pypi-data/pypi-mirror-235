import json
from pathlib import Path


def sql_obj_to_dict(sql_obj):
    d = dict()
    for col in sql_obj.__table__.columns:
        d[col.name] = getattr(sql_obj, col.name)
    return d


def sql_obj_list_to_dict_list(sql_obj_list):
    return [sql_obj_to_dict(sql_obj) for sql_obj in sql_obj_list]


def read_json(fpath):
    try:
        with open(fpath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return None
    
    
def write_json(fpath, data):
    with open(fpath, 'w') as f:
        json.dump(data, f)
        

def cache_team_id(app_dir, cache: dict):
    target_path = Path(app_dir) / 'team_id_cache.json'
    write_json(target_path, cache)
    

def read_team_id(app_dir):
    target_path = Path(app_dir) / 'team_id_cache.json'    
    return read_json(target_path)   


def cache_alarm_id(app_dir, cache: dict):
    target_path = Path(app_dir) / 'alarm_id_cache.json'
    write_json(target_path, cache)
    

def read_alarm_id(app_dir):
    target_path = Path(app_dir) / 'alarm_id_cache.json'    
    return read_json(target_path)   