from typing import Optional


class EmailVerificationService:
    def __init__(self):
        self.emails_verified = set()

    def verify_email(self, email: str) -> bool:
        # Простой пример: проверяем, что '@' есть в email
        is_valid = '@' in email
        if is_valid:
            self.emails_verified.add(email)
        return is_valid

    def get_verified_emails(self) -> set:
        return self.emails_verified

    def clear_verified_emails(self):
        self.emails_verified.clear()
