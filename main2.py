import random
import time

makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW']
models = ['Corolla', 'Civic', 'Focus', 'Cruze', '3 Series']
registration_statuses = ['Registered', 'Not Registered']
prices = [10000, 15000, 20000, 25000, 30000]
mileages = [50000, 60000, 70000, 80000, 90000]
keys = ['Yes', 'No']
damage_descriptions = ['None', 'Minor', 'Moderate', 'Severe']
transmissions = ['Automatic', 'Manual']
seats = [2, 4, 5]
# fueltypes = ['Gasoline', 'Diesel', 'Electric']

# def generate_car_info():
#     car_info = {
#         'Make': random.choice(makes),
#         'Model': random.choice(models),
#         'Registration Status': random.choice(registration_statuses),
#         'Price': random.choice(prices),
#         'Mileage': random.choice(mileages),
#         'Keys': random.choice(keys),
#         'Damage description': random.choice(damage_descriptions),
#         'Transmission': random.choice(transmissions),
#         'Seats': random.choice(seats),
#         'Fueltype': random.choice(fueltypes)
#     }
#     return car_info

# def main():
#     for _ in range(5):
#         car_info = generate_car_info()
#         output = ', '.join([f"{key}: {value}" for key, value in car_info.items()])
#         print(output)
#         # Simulate delay between outputs
#         time.sleep(1)

# if __name__ == '__main__':
#     main()


import time

# Simulate some long-running process
for i in range(5):
    #print(f"Output {i}, Value {i*10}")
    #Similar to above, print 10 comma seperated values instead of two coma seperated values
    print(f"Output {i}, Output {i*10}, Output {i*20}, Output {i*30}, Output {i*40}, Output {i*50}, Output {i*60}, Output {i*70}, Output {i*80}, Output {i*90}")
    time.sleep(1)

