from vehicles import *

vehicles = []
c1 = Car("abcd", "mustagn", 2020, "Electric", 4)
c2 = Car("efgh", "mustagn", 2020, "gas", 4)

t1 = Truck("ijkl", "mustagn", 2023, "100000", 8)
t2 = Truck("mnop", "mustagn", 2023, "100000", 8)

m1 = Motorcycle("qrst", "mustagn", 2020, "990", "sport")
m2 = Motorcycle("uvwx", "mustagn", 2020, "990", "sport")


vehicles.append(c1)
vehicles.append(c2)
vehicles.append(t1)
vehicles.append(t2)
vehicles.append(m1)
vehicles.append(m2)

for vehicle in vehicles:
    print(vehicle)

save_fleet_to_file(vehicles, "vehicles.txt")

print("\nLoading fleet from file...")
loaded_vehicles = load_fleet_from_file("vehicles.txt")

print(f"{len(loaded_vehicles)} vehicles loaded.")

print("\n--- All Vehicles Loaded From File --- ")
for vehicle in loaded_vehicles:
    print(vehicle)

print("\n--- Recent Vehicles (Last 4 Years) --- ")
for vehicle in loaded_vehicles:
    if vehicle.is_new(4):
        print(vehicle)

print("\n--- Electric Cars Only --- ")
for vehicle in loaded_vehicles:
    if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
        print(vehicle)
