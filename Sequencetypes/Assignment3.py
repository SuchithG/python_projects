"""
Collection Assignment - Initialize a list of countries with three countries in the list
- add an country at the end of the list
- remove an country using index
- add a county in the middle of the list 
"""

country_list = ["India", "Pakistan", "Canada"]

country_list.append("Brazil")

del country_list[1]

country_list.insert(2, "Germany")

country_list = set(country_list)

country_list.update(["France"])

print(country_list)