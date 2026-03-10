def generate(plan):
    return f"SELECT * FROM {plan['table']} LIMIT {plan['limit']}"