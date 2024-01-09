"""Module for handling email verification services."""


class EmailVerificationService(object):
    """Service for email verification."""

    def __init__(self):
        """Initialize EmailVerificationService."""
        self.emails_verified: set[str] = set()

    def verify_email(self, email: str) -> bool:
        """Verify the given email address.

        :param email: The email address to verify.
        :return: True if the email is verified, False otherwise.
        """
        # Simple example: check if '@' is present in the email
        is_valid = '@' in email
        if is_valid:
            self.emails_verified.add(email)
        return is_valid

    def get_verified_emails(self) -> set[str]:
        """Get the set of verified email addresses.

        :return: A set containing the email addresses that have been verified.
        """
        return self.emails_verified

    def clear_verified_emails(self):
        """Clear the set of verified email addresses."""
        self.emails_verified.clear()
