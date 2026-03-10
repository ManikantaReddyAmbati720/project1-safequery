FORBIDDEN = ["delete", "drop", "truncate", "alter", "update", "insert", "create"]

def validate(query):
    lower = query.lower()
    if any(word in lower for word in FORBIDDEN):
        return False, "Destructive operation not allowed"
    if not lower.startswith("select"):
        return False, "Only SELECT allowed"
    return True, "PASS"