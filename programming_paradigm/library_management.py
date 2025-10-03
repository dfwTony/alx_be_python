# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title          # public
        self.author = author        # public
        self._is_checked_out = False  # private (convention: leading underscore)

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # was not checked out

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

