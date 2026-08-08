import random

class Student:
  def __init__ (self,):
    '''test init'''

  def setData(self, name, age, address, id):
    self.name = name; # Type str. It is text name.
    self.age = age; # Type int. It is number age.
    self.address = address; # Type str. It is home place.
    self.id = id; # Type str. It is student ID.

  def showData(self):
    print ("ID: {} | Name: {:<35} | Age: {} | Address: {}".format(self.id, self.name, self.age, self.address));


class StudentManager:
  def __init__ (self,):
    '''test init'''
    self.allStudents = []; # Type list. It holds many students.

  def addOneStudent(self, oneStudent):
    self.allStudents.append(oneStudent);

  def sortWithAge(self):
    self.allStudents.sort(key=lambda s: s.age); # Lambda here. It sorts from small to big.

  def showAll(self):
    print ("\nTotal Students: {} (Sorted by Age)".format(len(self.allStudents)));
    for s in self.allStudents:
      s.showData();


def main():
  ManagerObject = StudentManager()

  rawNames = [
    "Devin Mindul Abeyratne", "Rithika Reddy Aleti", "Daniel Banggawan", "Smriti Bhandari",
    "Shihan Dushantha Fernando Bothalage", "Xiaohui Chen", "Kudzai Jeremy Chiwome", "Ching Man Chu",
    "Yonghui Dai", "Sonaly Celine David", "SHUKLA Debnath", "Tian Deng", "Gurbhej Singh Gill",
    "Pramod Gurung", "Xuerui Huang", "Kalapuge Dona Gaurani Kanishka Jayathilaka", "Nicholas Jones",
    "Lyndon Jugalbot", "Muhammad Zakriya Kareem", "Raj Kumar", "CHOONHO Lee", "Passang Lhamo",
    "Yu Li", "Shuohui Liu", "Songyun Liu", "ziyi Liu", "Pranay Reddy Mamidi", "MEHRIN FERDOUS Meem",
    "Shuyue Meng", "Bilal Ahamad Mohamad Rifas", "Kristian Mukara", "UTHAYA Naganathan", "Seyoung Oh",
    "Ravindu Malshika Fernando Palamandadige", "Chathuri Shyanika Perera", "Eduards Priednieks",
    "Priya Priya", "Qi Qi", "Ashish Rijal", "Keen James Salino", "Vimukthi Samarasekera",
    "Syed Ahnaf Wadud Sami", "Immanuel Santhosh", "Lahiru Thiwanka Maduranga Sarakku Patabendige",
    "Gokulakrishnan Sathyanarayanan Ramprakash", "Ilia Shalygin", "AYUSH Sharma", "Mukul Sharma",
    "Rajesh Sharma", "Yung-Hung Shih", "Anish Shrestha", "Sukhjeet Singh Sukhjeet Singh",
    "Sukhmanbir Singh Sukhmanbir Singh", "Marzana Sultana", "Yan Tan", "Minxuan Tang",
    "Giovani Tedesco Menegat", "CHAW Theingi", "Sandhya Tiwari", "Kamrunnahar Tuly", "Dinesh Upreti",
    "Aleksandr Voitenko", "Bin Wang", "Huanchen Wu", "Pei Wu", "Pingsheng Xiahou", "Ning Xu", "Gaowei Zhang"
  ]

  baseId = 20260001;
  cities = ["Auckland", "Hamilton", "Wellington", "Christchurch"];

  for name in rawNames:
    randAge = random.randint(18, 30);
    randAddr = "{} State Highway, {}".format(random.randint(1, 150), random.choice(cities));
    idStr = "STU{}".format(baseId);
    
    StudentObject = Student()
    StudentObject.setData(name, randAge, randAddr, idStr);
    ManagerObject.addOneStudent(StudentObject);
    
    baseId = baseId + 1;

  ManagerObject.sortWithAge();
  ManagerObject.showAll();


if __name__ == "__main__":
  main()
