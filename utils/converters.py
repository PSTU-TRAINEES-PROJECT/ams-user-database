def convert_to_uppercase(s: str) -> str:
    return s.upper()

def convert_to_lowercase(s: str) -> str:
    return s.lower()

def is_email_valid(email: str) -> bool:
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
