class School:
  def __init__(self ,  name, district, country, yearofestablishment):
    self.name = name
    self.district = district
    self.country = country
    self.yearofestablishment = yearofestablishment

school1 = School("Bishop Mackenzie","Lilongwe","Malawi","1944")
school2 = School("St.Andrews","Blantyre","Malawi","1850")

print(school1.name)
print(school1.district)
print(school1.country)
print(school1.yearofestablishment)

print(school2.name)
print(school2.district)
print(school2.country)
print(school2.yearofestablishment)