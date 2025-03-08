import unittest
import inspect

import todo.model.todo

module_members = [item[0] for item in inspect.getmembers(todo.model.todo)]
todo_defined = "Todo" in module_members
todobook_defined = "TodoBook" in module_members

if todo_defined:
    from todo.model.todo import Todo

if todobook_defined:
    from todo.model.todo import TodoBook


class TestTodoModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if todo_defined:
            cls.todo = Todo
        if todobook_defined:
            cls.todobook = TodoBook

    def setUp(self):
        if todo_defined:
            self.todo_instance = self.todo(1, "Test Todo", "Test Description")
        if todobook_defined:
            self.empty_todobook_instance = self.todobook()
            self.todobook_instance = self.todobook()
            self.todobook_instance.add_todo("Test Todo 1", "Test Description 1")
            self.todobook_instance.add_todo("Test Todo 2", "Test Description 2")

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_has_attributes(self):
        self.assertTrue(hasattr(self.todo_instance, "code_id"))
        self.assertTrue(hasattr(self.todo_instance, "title"))
        self.assertTrue(hasattr(self.todo_instance, "description"))
        self.assertTrue(hasattr(self.todo_instance, "completed"))
        self.assertTrue(hasattr(self.todo_instance, "tags"))

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_has_methods(self):
        self.assertTrue(hasattr(self.todo_instance, "mark_completed"))
        self.assertTrue(hasattr(self.todo_instance, "add_tag"))

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_initialization(self):
        self.assertEqual(self.todo_instance.code_id, 1)
        self.assertEqual(self.todo_instance.title, "Test Todo")
        self.assertEqual(self.todo_instance.description, "Test Description")
        self.assertFalse(self.todo_instance.completed)
        self.assertEqual(self.todo_instance.tags, [])

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_mark_completed(self):
        self.todo_instance.mark_completed()
        self.assertTrue(self.todo_instance.completed)

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_add_tag(self):
        self.todo_instance.add_tag("test_tag")
        self.assertIn("test_tag", self.todo_instance.tags)

    @unittest.skipIf(not todo_defined, "Todo class is not defined")
    def test_todo_class_str(self):
        self.assertEqual(str(self.todo_instance), "1 - Test Todo")

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_has_attributes(self):
        self.assertTrue(hasattr(self.empty_todobook_instance, "todos"))

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_has_methods(self):
        self.assertTrue(hasattr(self.empty_todobook_instance, "add_todo"))
        self.assertTrue(hasattr(self.empty_todobook_instance, "pending_todos"))
        self.assertTrue(hasattr(self.empty_todobook_instance, "completed_todos"))
        self.assertTrue(hasattr(self.empty_todobook_instance, "tags_todo_count"))

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_initialization(self):
        self.assertEqual(self.empty_todobook_instance.todos, {})

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_add_todo(self):
        code_id = self.empty_todobook_instance.add_todo("Test Todo", "Test Description")
        self.assertEqual(code_id, 1)
        self.assertEqual(len(self.empty_todobook_instance.todos), 1)

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_pending_todos(self):
        pending_todos = self.todobook_instance.pending_todos()
        self.assertEqual(len(pending_todos), 2)
        self.assertFalse(any(todo.completed for todo in pending_todos))

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_completed_todos(self):
        self.todobook_instance.todos[1].mark_completed()
        completed_todos = self.todobook_instance.completed_todos()
        self.assertEqual(len(completed_todos), 1)
        self.assertTrue(all(todo.completed for todo in completed_todos))

    @unittest.skipIf(not todobook_defined, "TodoBook class is not defined")
    def test_todobook_class_tags_todo_count(self):
        self.todobook_instance.todos[1].add_tag("tag1")
        self.todobook_instance.todos[1].add_tag("tag2")
        self.todobook_instance.todos[2].add_tag("tag1")
        tags_count = self.todobook_instance.tags_todo_count()
        self.assertEqual(tags_count, {"tag1": 2, "tag2": 1})


if __name__ == "__main__":
    unittest.main()