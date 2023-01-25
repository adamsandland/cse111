def miles_per_gallon(e, s, g):
    return (e-s)/g
def lp100k_from_mpg(mpg):
    return 235.215/mpg

def main():
    start_odometer = int(input("Enter the 1st Odometer reading in miles: "))
    end_odometer = int(input("Enter the 2nd Odometer reading in miles: "))
    fuel_usage = float(input("Enter the fuel used during the trip in Gallons: "))
    milesPerGal = miles_per_gallon(end_odometer,start_odometer,fuel_usage)
    print(f"Your fuel usage is {milesPerGal:.1f}mpg or {lp100k_from_mpg(milesPerGal):.2f} liters per 100 kilometers.")

main()