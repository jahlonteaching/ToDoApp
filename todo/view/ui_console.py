from todo.model.todo import TodoBook


class Console:

    def __init__(self, book: TodoBook):
        self.book: TodoBook = book

    @staticmethod
    def show_welcome_msg():
        print("============================")
        print("WELCOME TO THE TODOBOOK APP")
        print("============================")

    @staticmethod
    def show_menu():
        print("\nOPTIONS:")
        print("1. Add new todo")
        print("2. List all todos")
        print("3. Add tags to todo")
        print("4. List pending todos")
        print("5. List completed todos")
        print("6. Complete todo")
        print("7. Delete todo")
        print("8. Show tags count")
        print("9. Exit program")
        option = int(input("Enter an option: "))
        while option not in range(1, 10):
            print(">>> ERROR: Invalid option. Try again")
            option = int(input("Enter an option: "))
        return option

    def app_loop(self):
        Console.show_welcome_msg()
        end_app: bool = False
        while not end_app:
            option: int = Console.show_menu()
            end_app = self.process_user_option(option)

    def process_user_option(self, option: int) -> bool:
        if option == 1:
            self.add_new_todo()
        elif option == 2:
            self.list_todos()
        elif option == 3:
            self.add_tags_to_todo()
        elif option == 4:
            self.list_pending_todos()
        elif option == 5:
            self.list_completed_todos()
        elif option == 6:
            self.complete_todo()
        elif option == 7:
            self.delete_todo()
        elif option == 8:
            self.show_tags_count()
        elif option == 9:
            self.exit_app()
            return True

        return False

    def exit_app(self):
        print("======================")
        print("=== END OF PROGRAM ===")
        print("======================")

    def show_tags_count(self):
        print("\n=== SHOW TAGS COUNT ===\n")
        tags_count = self.book.tags_todo_count()
        for tag, count in tags_count.items():
            print(f"- Tag '{tag} has {count} todos")

    def delete_todo(self):
        print("\n=== DELETE TODO ===\n")
        self.list_todos()
        todo_code: int = int(input("Enter todo code: "))
        del self.book.todos[todo_code]
        print(f"Todo with code {todo_code} has been deleted")

    def complete_todo(self):
        print("\n=== COMPLETE TODO ===\n")
        self.list_pending_todos()
        todo_code: int = int(input("Enter todo code: "))
        self.book.todos[todo_code].mark_completed()
        print(f"Todo with code {todo_code} has been marked as completed")

    def list_pending_todos(self):
        print("\n=== PENDING TODOS ===")
        pending_todos = self.book.pending_todos()
        if len(pending_todos) > 0:
            for todo in pending_todos:
                print(todo)
        else:
            print("No items to show")

    def list_completed_todos(self):
        print("\n=== COMPLETED TODOS ===")
        completed_todos = self.book.completed_todos()
        if len(completed_todos) > 0:
            for todo in completed_todos:
                print(todo)
        else:
            print("No items to show")

    def add_tags_to_todo(self):
        print("\n=== ADD TAGS TO TODO ===\n")
        self.list_todos()
        todo_code: int = int(input("Enter todo code: "))
        tags: str = input("Enter tags separated by comma: ")
        for tag in tags.split(","):
            self.book.todos[todo_code].add_tag(tag)
        print(f"Tags were added successfully to todo with code {todo_code}")

    def list_todos(self):
        print("\n=== TODO LIST ===")
        if len(self.book.todos) > 0:
            for todo in self.book.todos.values():
                print(todo)
        else:
            print("No items to show")

    def add_new_todo(self):
        print("\n=== ADD NEW TODO ===")
        title: str = input("Enter title: ")
        description: str = input("Enter description: ")
        code_id = self.book.add_todo(title, description)
        print(f"A todo was created successfully with code {code_id}")
