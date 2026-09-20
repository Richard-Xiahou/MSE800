# 2.1 Factory Method Design Pattern

from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT PRODUCT
# ==========================================
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


# ==========================================
# 2. CONCRETE PRODUCTS
# ==========================================
class Email:
  def send(self):
    print("This is a notification from an organisation via email");

class SMS:
  def send(self):
    print("This is a notification from an organisation via SMS");

class PushNotification:
  def send(self):
    print("This is a notification from an organisation via PushNotification");


# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
# ==========================================
class NotificationFactory:
   @abstractmethod
   def create_notification(self):
    pass


# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================

# Concrete Factory
class EmailFactory:
  def create_notification(self):
    return Email()

class SMSFactory:
  def create_notification(self):
    return SMS()

class PushNoteFactory:
  def create_notification(self):
    return PushNoteFactory()


# ==========================================
# 5. CLIENT
# ==========================================
factory = SMSFactory()
notice = factory.create_notification()
notice.send()
