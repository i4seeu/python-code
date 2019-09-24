class School:
  def __init__(self ,  name, district, country, yearofestablishment):
    self.name = name
    self.district = district
    self.country = country
    self.yearofestablishment = yearofestablishment

  def setName(self, name):
    self.name = name
  def getName(self):
    return self.name

  def setDistrict(self, district):
    self.district = district
  def getDistrict(self):
      return self.district

  def setCountry(self, country):
    self.country = country
  def getCountry(self):
    return self.country

  def setYear(self, yearofestablishment):
    self.yearofestablishment = yearofestablishment
  def getYear(self):
    return self.yearofestablishment

school1 = School("Bishop Mackenzie","Lilongwe","Malawi","1944")
school2 = School("St.Andrews","Blantyre","Malawi","1850")

school1.setName("Bishop Mackenzie")
school_name = school1.getName()
print(school_name)

school1.setDistrict("Lilongwe")
school_district = school1.getDistrict()
print(school_district)

school1.setCountry("Malawi")
school_country = school1.getCountry()
print(school_country)

school1.setYear("1944")
school_year = school1.getYear()
print(school_year)

school1.setName("St.Andrews")
school_name = school1.getName()
print(school_name)

school1.setDistrict("Blantyre")
school_district = school1.getDistrict()
print(school_district)

school1.setCountry("RSA")
school_country = school1.getCountry()
print(school_country)

school1.setYear("1850")
school_year = school1.getYear()
print(school_year) 
