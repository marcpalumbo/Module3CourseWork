counties = ["Arapahoe","Denver","Jefferson"]

# if counties[1] == 'Denver':
    #print(counties[1])

#for county in counties:
  #  print(county)



#for num in range(5):
 #   print(num)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict:
 #       print(county)

for county,voters in counties_dict.items():
    print(county, "county has", voters,"registered voters")


   