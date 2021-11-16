total = int(input("Enter number of apartments: "))
floors = int(input("Enter number of floors: "))
apartment = int(input("Enter number of apartment: "))
if apartment > 0 and floors > 0 and apartment <= total and total % floors == 0:
    apartmentPerFloor = total / floors
    floor = int(apartment // apartmentPerFloor)
    if apartment % apartmentPerFloor == 0:
        print(floor)
    else:
        print(floor + 1)




