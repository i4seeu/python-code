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

