
class UserNotFoundException(Exception):
    def __init__(self, nationality):
        self.nationality = nationality
        super().__init__(f"User with nationality '{nationality}' not found.")

class UserNotFoundExceptionId(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"User with Id '{user_id}' not found.")

class UserDeletionException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Failed to delete user with ID {user_id}.")

class UserUpdateException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Failed to update user with ID {user_id}.")

class UserCreationException(Exception):
    def __init__(self):
        super().__init__("Failed to create user.")
