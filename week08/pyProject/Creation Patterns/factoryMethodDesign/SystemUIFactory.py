# Operating System UI Factory
from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT PRODUCT
#    Defines the common interface for the products
#    定义Button 和 Checkbox  的基类, 这些基类本身继承自ABC.
# ==========================================

class Button(ABC):
  @abstractmethod
  def create(self):
    pass

class Checkbox(ABC):
  @abstractmethod
  def create(self):
    pass


# ==========================================
# 2. CONCRETE PRODUCTS
#    分别继承自Button　和  Checkbox
# ==========================================
class WindowsButton(Button):
  def create(self):
    print("windows button created")

class WindowsCheckbox(Checkbox):
  def create(self):
    print("windows checkbox created")

class MacButton(Button):
  def create(self):
    print("mac button created")

class MacCheckbox(Checkbox):
  def create(self):
    print("mac checkbox created")

# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
#    继承自ABC
# ==========================================
class SystemUIFactory(ABC):
  @abstractmethod
  def create_button(self):
    pass

  @abstractmethod
  def create_checkbox(self):
    pass

# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================
class WindowsFactory:
  def create_button(self):
      return WindowsButton()
  def create_checkbox(self):
      return WindowsCheckbox()

class MacFactory:
  def create_button(self):
      return MacButton()
  def create_checkbox(self):
      return MacCheckbox()

# ==========================================
# 5. CLIENT
# ==========================================
factory_w = WindowsFactory()
button = factory_w.create_button()
Checkbox = factory_w.create_checkbox()

button.create()
Checkbox.create()

#  ======== relationship ==========
#
#             Abstract Factory
#                    │
#       ┌────────────┴────────────┐
#       ↓                         ↓
# WindowsFactory              MacFactory
#       │                         │
#       ├── WindowsButton         ├── MacButton
#       │                         │
#       └── WindowsCheckbox       └── MacCheckbox