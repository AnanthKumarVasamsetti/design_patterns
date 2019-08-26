"""
Observer: This design pattern notifies the subject upon any changes that take place in on the subscribed object.

Example: In the following example user's will subscribe to blog when ever there is an update on that blog all the users
         who are subscribed to it will be notified.
"""

class Observer:
    
    def __init__(self):
        pass

    def notify(self):
        pass

class Blog():
    
    def __init__(self, name):
        self.name = name
        self.subscribed_users = []
        self.content = ""
    
    def add_user(self, user_object):
        self.subscribed_users.append(user_object)
    
    def remove_user(self, user_object):
        self.subscribed_users.remove(user_object)

    def update_blog(self, latest_content):
        self.content = latest_content
        self.notify_users()
    
    def notify_users(self):
        for user in self.subscribed_users:
            print(user.name)
            user.notify(self.name, self.content)

class User(Observer):

    def __init__(self, name):
        self.name = name
    
    def subscribe(self, blog_object):
        blog_object.add_user(self)
    
    def notify(self, blog_name, blog_content):
        print(blog_name + " has been updated it's content to " + blog_content)

if __name__ == "__main__":
    techcrunch = Blog("Techcrunch")
    youtube = Blog("Youtube")

    user1 = User('user1')
    user2 = User('user2')

    techcrunch.add_user(user1)
    techcrunch.add_user(user2)

    youtube.add_user(user1)
    youtube.add_user(user2)

    techcrunch.update_blog("News: S technologies, first company to reach 1 trillion dollar mark")
    youtube.update_blog("Video: First mars colony inaugural ceremony")

    techcrunch.remove_user(user1)

    techcrunch.update_blog("Gadget: Apple released it's new iPhone 20")
    youtube.update_blog("Video: Live from Google headquarters")
