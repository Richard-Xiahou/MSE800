
class UniversityConfigurationManager:
    instance = None
    def __new__(cls):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
            cls.university_name = "Massey University"
            cls.academic_year = "2024"
            cls.semester = "Semester 1"
        return cls.instance


university_config1 = UniversityConfigurationManager()
university_config2 = UniversityConfigurationManager()

print(university_config1.university_name)
university_config2.university_name = "Auckland University"
print(university_config1.university_name)
print(university_config1 is university_config2)
