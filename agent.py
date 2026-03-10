from planner import plan
from generator import generate
from validator import validate
from executor import execute

def run(query):
    p = plan(query)
    sql = generate(p)
    valid, msg = validate(sql)
    if not valid:
        return msg
    return execute(sql)