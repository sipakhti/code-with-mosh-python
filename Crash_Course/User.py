
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

# 9.7 Admin (INHERITANCE)

class Admin(User):
    """Sub Class of Users with special Priviliges"""

    # Constructor
    def __init__(self, first_name, last_name, email, phone_number, age,priviliges = ["can add post","can delete psot","can ban user"]):
        super().__init__(first_name, last_name, email, phone_number, age)
        self.priviliges = Priviliges(priviliges)
    
    # prints out the priviliges of the said role

    
    # Alternate Constructor
    @classmethod
    def from_string(cls, user_string, priviliges_string, seperator="-"):
        """ alternate constructor, takes two strings, first string feeds 
            the parent class and the second string feeds into child class
        """
        first, last, email, phone, age = user_string.split(seperator)
        priviliges = list(priviliges_string.split(seperator))
        
        # adds a line break (\n) at the start of every string item in the list so that displaying it is easy
        for index in range(len(priviliges)):
            priviliges[index] = "\n" + priviliges[index] 

        return cls(first, last, email, phone, int(age), priviliges)



# 9.8 
class Priviliges():
    
    # Constructor
    def __init__(self, priviliges):
        self.priviliges = priviliges

    # prints out the priviliges of the said role
    def show_priviliges(self):
        print(*self.priviliges)
    
    # Alternate Constructor
    @classmethod
    def from_string(cls, priviliges_string, seperator="-"):
        cls.priviliges = priviliges_string.split(seperator)

        return cls.priviliges


hassan = Admin("hassan", "mehmood", "123@gmail.com", "0300xxxxxxx", 21)
umer = Admin.from_string("Umer-Mehmood-456@gmail.com-0321xxxxxxx-24",
                         "dope-can do stuff-can fire bazooka", "-")

hassan.priviliges.show_priviliges()
umer.priviliges.show_priviliges()
