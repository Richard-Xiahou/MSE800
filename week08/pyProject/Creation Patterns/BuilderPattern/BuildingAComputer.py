# ==========================================
# 1. CLIENT
# ==========================================
class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def show_details(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("Storage:", self.storage)

# ==========================================
# 2. BUILDER / CONCRETE BUILDER
# ==========================================
class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self
    def set_ram(self, ram):
        self.ram = ram
        return self
    def set_storage(self, storage):
        self.storage = storage
        return self
    def build(self):
        return Computer(
            self.cpu,
            self.ram,
            self.storage
        )

# ==========================================
# 3. DIRECTOR 
# ==========================================
class ComputerDirector:
    def build_basic_computer(self, builder):
        builder.set_cpu("Intel i5")
        builder.set_ram("8 GB")
        builder.set_storage("512 GB SSD")
        return builder.build()

builder= ComputerBuilder()
director = ComputerDirector()
computer = director.build_basic_computer(builder)
computer.show_details()