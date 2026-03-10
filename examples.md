\# Example Interactions



\## Example 1

User: Show me recent orders

Planner: orders table, order by date desc, limit 10

Generator: SELECT \* FROM orders ORDER BY order\_date DESC LIMIT 10

Validator: PASS

Executor: Returned 10 rows



\## Example 2

User: Delete all users

Validator: REJECTED – destructive operation not allowed



\## Example 3

User: Total revenue per customer

Planner: SUM(total\_amount), GROUP BY customer\_id

Generator: SELECT customer\_id, SUM(total\_amount) FROM orders GROUP BY customer\_id LIMIT 100

Validator: PASS

