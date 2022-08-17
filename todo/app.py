from todo.model.todo import TodoBook
from todo.view.ui_console import Console


if __name__ == "__main__":
    book: TodoBook = TodoBook()
    ui: Console = Console(book)
    ui.app_loop()
