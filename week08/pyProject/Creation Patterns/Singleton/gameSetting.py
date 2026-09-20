class GameSettings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Settings
            cls._instance.sound = 80
            cls._instance.difficulty = "Easy"

        return cls._instance

# Create two settings objects
settings1 = GameSettings()
settings2 = GameSettings()

# Change settings using settings1
settings1.sound = 50
settings1.difficulty = "Hard"

# Access using settings2
print(settings2.sound)
print(settings2.difficulty)

# Check if they are the same object
print(settings1 is settings2)