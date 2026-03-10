print("SafeQuery Agent Demo Started")

user_query = input("Enter your query: ").strip()
print("You entered:", user_query)

# -------------------------
# Simple Safety Validator
# -------------------------
FORBIDDEN_KEYWORDS = [
    "delete", "drop", "truncate", "alter", "update", "insert", "create"
]

def is_unsafe(text: str) -> bool:
    t = text.lower()
    return any(word in t for word in FORBIDDEN_KEYWORDS)

# If user asks for unsafe action, block it
if is_unsafe(user_query):
    print("\nPlanner Output: (blocked) unsafe intent detected")
    print("Generator Output: (no SQL generated)")
    print("Validator Output: REJECTED — destructive operation not allowed (SELECT-only mode)")
    print("Executor Output: NOT RUN (blocked by validator)")
else:
    # Safe demo path (you can improve later)
    print("\nPlanner Output: Table = orders")
    print("Generator Output: SELECT * FROM orders LIMIT 10")
    print("Validator Output: PASS")
    print("Executor Output: Returned 10 rows")