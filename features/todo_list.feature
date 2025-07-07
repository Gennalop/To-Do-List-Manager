Feature: Manage the to-do list

Scenario: Add a task to the to-do list
  Given the to-do list is empty
  When the user adds a task with description "Buy groceries", priority "high", and due date "2025-07-08"
  Then the to-do list should contain a task with description "Buy groceries"

Scenario: List all tasks in the to-do list
  Given the to-do list contains tasks:
    | description     | priority | due_date   | status   |
    | Buy groceries   | high     | 2025-07-08 | pending  |
    | Pay bills       | medium   | 2025-07-09 | pending  |
  When the user lists all tasks
  Then the output should contain:
    """
    Description: Buy groceries, Priority: high, Due Date: 2025-07-08, Status: pending
    Description: Pay bills, Priority: medium, Due Date: 2025-07-09, Status: pending
    """

Scenario: Mark a task as completed
  Given the to-do list contains tasks:
    | description   | priority | due_date   | status   |
    | Buy groceries | high     | 2025-07-08 | pending  |
  When the user marks the task "Buy groceries" as completed
  Then the to-do list should contain a task "Buy groceries" with status "completed"

Scenario: Delete a task from the to-do list
  Given the to-do list contains tasks:
    | description   | priority | due_date   | status   |
    | Buy groceries | high     | 2025-07-08 | pending  |
    | Pay bills     | medium   | 2025-07-09 | pending  |
  When the user deletes the task "Pay bills"
  Then the to-do list should contain only:
    | description   |
    | Buy groceries |

Scenario: Delete all completed tasks from the to-do list
  Given the to-do list contains tasks:
    | description | priority | due_date   | status     |
    | Task 1      | high     | 2025-07-08 | completed  |
    | Task 2      | low      | 2025-07-09 | pending    |
    | Task 3      | medium   | 2025-07-10 | completed  |
  When the user deletes all completed tasks
  Then the to-do list should contain only:
    | description |
    | Task 2 |

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
    | description   |
    | Buy groceries |
    | Pay bills     |
  When the user clears the to-do list
  Then the to-do list should be empty
