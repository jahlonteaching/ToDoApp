from todo.model.todo import TodoBook
from todo.view.ui_console import Console


def main():
    book: TodoBook = TodoBook()
    ui: Console = Console(book)
    ui.app_loop()


if __name__ == "__main__":
    main()
