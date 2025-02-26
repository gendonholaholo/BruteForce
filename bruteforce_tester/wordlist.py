import logging

class Wordlist:
    def __init__(self, username_file=None, password_file=None):
        self.usernames = self.load_from_file(username_file) if username_file else ["admin", "user", "guest"]
        self.passwords = self.load_from_file(password_file) if password_file else ["password123", "admin123", "qwerty", "123456"]
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            logging.warning(f"File not found: {filename}, using default values.")
            return []
