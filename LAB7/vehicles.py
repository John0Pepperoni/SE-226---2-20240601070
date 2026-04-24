class Vehicle:
    vid = ''
    model = ''
    year = 0
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return "VID: " +str(self.vid)+ " Model: " +str(self.model)+ " Year: " +str(self.year)

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        min_year = 2026 - n
        return min_year < self.year < 2026


class Car(Vehicle):
    fuel_type = ''
    doors = 0

    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        x = super().__str__()
        return str(x) + " Fuel: " +str(self.fuel_type)+ " Doors: " +str(self.doors)


class Truck(Vehicle):
    max_load = 0
    axles = 0

    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        x = super().__str__()
        return str(x)+ " Load: " +str(self.max_load)+ "kg Axles: " +str(self.axles)


class Motorcycle(Vehicle):
    engine_cc = 0
    type = ''

    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        x = super().__str__()
        return str(x)+ " EngineCC: " +str(self.engine_cc)+ "cc Type: " +str(self.type)


def save_fleet_to_file(vehicles, filename):
    try:
        with open(filename, 'w') as f:
            for vehicle in vehicles:
                f.write(str(vehicle) + '\n')
    except IOError:
        print("Error writing to file")

def load_fleet_from_file(filename):
    vehicles = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) < 10:
                    continue

                vid = parts[1]
                model = parts[3]
                year = int(parts[5])
                
                vehicle_type_label = parts[6]

                if vehicle_type_label == "Fuel:":
                    fuel_type = parts[7]
                    doors = int(parts[9])
                    vehicles.append(Car(vid, model, year, fuel_type, doors))
                elif vehicle_type_label == "Load:":
                    max_load = parts[7].replace('kg', '')
                    axles = int(parts[9])
                    vehicles.append(Truck(vid, model, year, int(max_load), axles))
                elif vehicle_type_label == "EngineCC:":
                    engine_cc = parts[7].replace('cc', '')
                    moto_type = parts[9]
                    vehicles.append(Motorcycle(vid, model, year, int(engine_cc), moto_type))
    except IOError:
        print("Error reading from file")
    except (ValueError, IndexError):
        print(f"Error parsing line: '{line.strip()}'")
    
    return vehicles
