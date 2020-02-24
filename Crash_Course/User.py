
class User():

    def __init__(self, first_name, last_name, email, phone_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("NAME: " + self.first_name.title() + " " + self.last_name.title())
        print("AGE: " + self.age)
        print("EMAIL: " + self.email)
        print("PHONE NUMBER: " + self.phone_number)

    @classmethod
    def from_string(cls, user_string, seperator):
        first, last, email, phone, age = user_string.split(seperator)
        return cls(first, last, email, phone, age)

# 9.4
    def increment_login_attempts(self):
        """increments login attempt by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """resets the login attempts to default Value of 0"""
        self.login_attempts = 0

