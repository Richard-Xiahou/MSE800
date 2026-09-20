# Observer 
# The Observer defines what an observer must do when it receives an update.
class Observer:
    def update(self):
        pass
# Concrete Observer
# The Concrete Observer is the actual object that receives the notification.
class Student(Observer):
    def __init__(self, name):
        self.name = name
    def update(self):
        print(self.name, "received a notification")

# Subject
# The Subject is the object whose state can change.
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

# Concrete Subject
# The Concrete Subject is the actual subject that changes its state.
class YouTubeChannel(Subject):
    def upload_video(self, title):
        print("New video uploaded:", title)
        self.notify()

# Create Subject
channel = YouTubeChannel()
# Create Observers
student1 = Student("Ali")
student2 = Student("Sara")
student3 = Student("John")
# Subscribe students
channel.attach(student1)
channel.attach(student2)
channel.attach(student3)
# Upload video
channel.upload_video("Python Design Patterns")