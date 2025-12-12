import random
import string

class RandomDataGenerator:
    """
    Provides random data values based on the strategy defined in config.json.
    Strategies include: name, email, sentence, date, number.
    """

    @staticmethod
    def random_name():
        """
        Provides random data values based on the strategy defined in config.json.
        Strategies include: name, email, sentence, date, number.
        """
        first = random.choice(["Alex", "Maya", "Saif", "Ravi", "Lina", "Omar"])
        last = ''.join(random.choices(string.ascii_lowercase, k=7))
        return f"{first} {last.capitalize()}"

    @staticmethod
    def random_date():
        """
        Produce a random date between 2023 and 2026.
        Format: YYYY-MM-DD
        """
        year = random.randint(2023, 2026)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

    @staticmethod
    def random_email():
        """
        Create a random email using 8 random characters + random domain.
        """
        name = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = random.choice(["example.com", "mail.com", "test.org"])
        return f"{name}@{domain}"

    @staticmethod
    def random_number(min_v=1, max_v=9999):
        """
        Return a random number between min_v and max_v.
        """
        return str(random.randint(min_v, max_v))

    @staticmethod
    def random_sentence():
        """
        Build a random 6-word sentence from given keywords.
        """
        words = ["client", "approved", "report", "deadline", "priority", "pending"]
        return " ".join(random.choices(words, k=6)).capitalize() + "."

    # Mapping of strategy name to method
    STRATEGIES = {
        "name": random_name.__func__,
        "date": random_date.__func__,
        "email": random_email.__func__,
        "sentence": random_sentence.__func__
    }

    @classmethod
    def generate(cls, strategy: str):
        """
        Generate a value depending on strategy type.

        Examples:
            "name" - generates name
            "email" - generates email
            "number:100:500" - number between 100–500
        """
        # Handle number generation format: number:min:max
        if ":" in strategy:
            name, min_v, max_v = strategy.split(":")
            if name == "number":
                return cls.random_number(int(min_v), int(max_v))
        # Otherwise use strategy from STRATEGIES dict
        return cls.STRATEGIES[strategy]()
