class ParkingLot:
    def __init__(self):
        """
        Initializes the ParkingLot object.

        Parameters:
            None

        Returns:
            None
        """
        self.levels = {
            'A': [{'occupied': False, 'vehicle_number': None} for _ in range(20)],
            'B': [{'occupied': False, 'vehicle_number': None} for _ in range(20)]
        }

    def find_nearest_spot(self):
        """
        Finds the nearest parking spot.

        This function iterates over the levels and spots in the parking lot. It checks if a spot is unoccupied and has no vehicle parked in it. If such a spot is found, it returns a dictionary with the level and spot number. If no available spot is found, it returns -1.

        Returns:
            - A dictionary containing the level and spot number if a spot is found.
            - -1 if no available spot is found.
        """
        for level, spots in self.levels.items():
            for i, spot in enumerate(spots):
                if spot['occupied'] is False and spot['vehicle_number'] is None:
                    return {'level': level, 'spot': i+1 if level == 'A' else i+21}
        return -1

    def park_vehicle(self, vehicle):
        """
        Park a vehicle in the parking lot.

        Parameters:
            vehicle (any): The vehicle to be parked.

        Returns:
            int or dict: Returns -2 if the vehicle is already parked, -1 if there are no available spots, 
            or a dictionary containing the level and spot number where the vehicle is parked.
        """
        # Check if already parked
        if isinstance(self.retrieve_vehicle(vehicle), dict):
            return -2

        nearest_spot = self.find_nearest_spot()
        if nearest_spot != -1:
            spot = (
                nearest_spot['spot'] - 1) % 20 if nearest_spot['spot'] > 20 else (nearest_spot['spot'] - 1)
            self.levels[nearest_spot['level']][spot] = {
                'occupied': True, 'vehicle_number': vehicle}
            return nearest_spot
        return -1

    def retrieve_vehicle(self, vehicle):
        """
        Retrieves a vehicle from the parking lot.

        Parameters:
            vehicle (str): The vehicle number to retrieve.

        Returns:
            dict or int: If the vehicle is found, returns a dictionary with the level and spot of the vehicle. If the vehicle is not found, returns -1.
        """
        for level, spots in self.levels.items():
            for i, spot in enumerate(spots):
                if spot['occupied'] is True and spot['vehicle_number'] == vehicle:
                    return {'level': level, 'spot': i+1 if level == 'A' else i+21}
        return -1

    def unpark_vehicle(self, vehicle):
        """
        Unparks a vehicle from the parking lot.

        Parameters:
            vehicle (str): The license plate number of the vehicle to be unparked.

        Returns:
            dict or int: If the vehicle is successfully unparked, returns the parking details dictionary. 
                The parking details dictionary contains the spot number and level of the parking spot 
                from which the vehicle was unparked. If the vehicle is not found in the parking lot, 
                returns -1.
        """
        parking_details = self.retrieve_vehicle(vehicle)
        if parking_details != -1:
            spot = (parking_details['spot'] - 1) % 20 if parking_details['spot'] > 20 else (
                parking_details['spot'] - 1)
            self.levels[parking_details['level']][spot] = {
                'occupied': False, 'vehicle_number': None}
            return parking_details
        return -1


def main():
    """
    Runs the main function of the Parking Lot System.

    This function executes a loop that displays a menu and prompts the user for their choice. 
    The available menu options are:
    1. Park a vehicle
    2. Retrieve parking spot
    3. Unpark a vehicle
    4. See all parking spots
    5. Exit

    The function uses an instance of the ParkingLot class to perform the requested actions based 
    on the user's input. The user is prompted to enter a choice from 1 to 5. Based on the choice, 
    the function takes appropriate actions such as parking a vehicle, retrieving a parking spot, 
    unparking a vehicle, displaying all parking spots, or exiting the program.

    Parameters:
        None

    Returns:
        None
    """
    parking_lot = ParkingLot()

    print('\n', "*"*90)
    print("*"*36, "Parking Lot System", "*"*36)
    print("*"*90)

    while True:
        print("\nMenu:")
        print("1. Park a vehicle")
        print("2. Retrieve parking spot")
        print("3. Unpark a vehicle")
        print("4. See all parking spots")
        print("5. Exit")

        case = input("Enter your choice (1-5): ")

        if case == '1':
            vehicle = input("Enter Vehicle number: ")
            park = parking_lot.park_vehicle(vehicle)
            if park == -2:
                print(f"Vehicle {vehicle} is already parked.")
            elif park == -1:
                print("All the spots are occupied. No spot available.")
            else:
                print(f"Vehicle {vehicle} parked at : {park}")

        elif case == '2':
            vehicle = input("Enter Vehicle number: ")
            spot = parking_lot.retrieve_vehicle(vehicle)
            if spot == -1:
                print(f"Vehicle {vehicle} is not parked in Parking Lot.")
            else:
                print(f"Vehicle {vehicle} is parked at: {spot}")

        elif case == '3':
            vehicle = input("Enter Vehicle number: ")
            parking_details = parking_lot.unpark_vehicle(vehicle)
            if parking_details == -1:
                print("Vehicle must be parked in order to do unpark.")
            else:
                print(f"Vehicle {vehicle} is unparked.")
                print(f"{parking_details} is vacated and empty now.")

        elif case == '4':
            print(f"Here's all parking spots: \n{parking_lot.levels}")

        elif case == '5':
            print("Exiting the 'Parking Lot System'...")
            break

        else:
            print("Please enter valid Menu choice (1-5)")


if __name__ == '__main__':
    main()
