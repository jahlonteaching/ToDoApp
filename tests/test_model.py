import pytest
import inspect

import todo.model.todo


module_members = [item[0] for item in inspect.getmembers(todo.model.todo)]
todo_defined = "Todo" in module_members
todobook_defined = "TodoBook" in module_members


if todo_defined:
    from todo.model.todo import Todo

if todobook_defined:
    from todo.model.todo import TodoBook


@pytest.fixture
def todo():
    return Todo(1, "Test Todo", "Test Description")


@pytest.fixture
def empty_todobook():
    return TodoBook()


@pytest.fixture
def todobook():
    todobook = TodoBook()
    todobook.add_todo("Test Todo 1", "Test Description 1")
    todobook.add_todo("Test Todo 2", "Test Description 2")
    return todobook


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_has_attributes(todo):
    assert hasattr(todo, "code_id")
    assert hasattr(todo, "title")
    assert hasattr(todo, "description")
    assert hasattr(todo, "completed")
    assert hasattr(todo, "tags")


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_has_methods(todo):
    assert hasattr(todo, "mark_completed")
    assert hasattr(todo, "add_tag")


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_initilization(todo):
    assert todo.code_id == 1
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert not todo.completed
    assert todo.tags == []


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_mark_completed(todo):
    todo.mark_completed()
    assert todo.completed


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_add_tag(todo):
    todo.add_tag("test_tag")
    assert "test_tag" in todo.tags


@pytest.mark.skipif(not todo_defined, reason="Todo class is not defined")
def test_todo_class_str(todo):
    assert str(todo) == "1 - Test Todo"


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_has_attributes(empty_todobook):
    assert hasattr(empty_todobook, "todos")


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_has_methods(empty_todobook):
    assert hasattr(empty_todobook, "add_todo")
    assert hasattr(empty_todobook, "pending_todos")
    assert hasattr(empty_todobook, "completed_todos")
    assert hasattr(empty_todobook, "tags_todo_count")


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_initilization(empty_todobook):
    assert empty_todobook.todos == {}


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_add_todo(empty_todobook):
    code_id = empty_todobook.add_todo("Test Todo", "Test Description")
    assert code_id == 1
    assert len(empty_todobook.todos) == 1


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_pending_todos(todobook):
    pending_todos = todobook.pending_todos()
    assert len(pending_todos) == 2
    assert not any(todo.completed for todo in pending_todos)


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_completed_todos(todobook):
    todobook.todos[1].mark_completed()
    completed_todos = todobook.completed_todos()
    assert len(completed_todos) == 1
    assert all(todo.completed for todo in completed_todos)


@pytest.mark.skipif(not todobook_defined, reason="TodoBook class is not defined")
def test_todobook_class_tags_todo_count(todobook):
    todobook.todos[1].add_tag("tag1")
    todobook.todos[1].add_tag("tag2")
    todobook.todos[2].add_tag("tag1")
    tags_count = todobook.tags_todo_count()
    assert tags_count == {"tag1": 2, "tag2": 1}
