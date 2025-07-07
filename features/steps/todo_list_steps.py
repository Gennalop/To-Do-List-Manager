from behave import *
from datetime import datetime
from todo_list import *

@given("the to-do list is empty")
def step_impl(context):
    context.tasks = []

@when('the user adds a task with description "{desc}", priority "{priority}", and due date "{due_date}"')
def step_impl(context, desc, priority, due_date):
    task = Task(desc, priority, due_date)
    context.tasks.append(task)

@then('the to-do list should contain a task with description "{desc}"')
def step_impl(context, desc):
    assert any(task.description == desc for task in context.tasks)

@given("the to-do list contains tasks:")
def step_impl(context):
    context.tasks = []
    for row in context.table:
        task = Task(
            description=row["description"],
            priority=row.get("priority", "medium"),
            due_date=row.get("due_date", "2025-07-01"),
            status=row.get("status", "pending")
        )
        context.tasks.append(task)

@when("the user lists all tasks")
def step_impl(context):
    context.output = "\n".join(str(task) for task in context.tasks)

@then("the output should contain:")
def step_impl(context):
    expected = context.text.strip()
    actual = "\n".join(str(task) for task in context.tasks).strip()
    for line in expected.splitlines():
        assert line.strip() in actual, f"Missing line: {line.strip()}"

@when('the user marks the task "{desc}" as completed')
def step_impl(context, desc):
    for task in context.tasks:
        if task.description == desc:
            task.status = "completed"

@then('the to-do list should contain a task "{desc}" with status "{status}"')
def step_impl(context, desc, status):
    found = [task for task in context.tasks if task.description == desc and task.status == status]
    assert found, f"No task with description '{desc}' and status '{status}' found"

@when('the user deletes the task "{desc}"')
def step_impl(context, desc):
    context.tasks = [task for task in context.tasks if task.description != desc]

@then("the to-do list should contain only:")
def step_impl(context):
    expected_descriptions = [row["description"] for row in context.table]
    actual_descriptions = [task.description for task in context.tasks]
    assert actual_descriptions == expected_descriptions

@when("the user deletes all completed tasks")
def step_impl(context):
    clean_completed_tasks(context.tasks)

@when("the user clears the to-do list")
def step_impl(context):
    clean_list(context.tasks)

@then("the to-do list should be empty")
def step_impl(context):
    assert len(context.tasks) == 0
