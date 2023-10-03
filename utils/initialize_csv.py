import csv

def initialize_csv():
    """Create an initial parcels.csv file with headers."""
    with open('data/parcels.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Parcel Number', 'Parcel Weight', 'Parcel Category'])

if __name__ == "__main__":
    initialize_csv()
    print("parcels.csv initialized successfully!")
