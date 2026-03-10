import csv
from pathlib import Path


def generate_report(energy_dir="results"):
    energy_dir = Path(energy_dir)

    total_energy = 0.0
    total_emissions = 0.0
    total_duration = 0.0

    csv_files = list(energy_dir.glob("*.csv"))

    if not csv_files:
        print("No result files found")
        return

    outfile = open("report.txt", "a")

    # Read first file to extract system information
    with open(csv_files[0]) as f:
        reader = csv.DictReader(f)
        first_row = next(reader)

        print("\nSYSTEM INFORMATION")
        outfile.write("\nSYSTEM INFORMATION\n")

        print(f"cpu_model: {first_row['cpu_model']}")
        outfile.write(f"cpu_model: {first_row['cpu_model']}\n")

        print(f"cpu_count: {first_row['cpu_count']}")
        outfile.write(f"cpu_count: {first_row['cpu_count']}\n")

        print(f"ram_total_size_gb: {first_row['ram_total_size']}")
        outfile.write(f"ram_total_size_gb: {first_row['ram_total_size']}\n")

        print()
        outfile.write("\n")

    # Process each step
    for file in csv_files:

        with open(file) as f:
            reader = csv.DictReader(f)

            for row in reader:
                duration = float(row["duration"])
                energy = float(row["energy_consumed"])
                emissions = float(row["emissions"])

                total_duration += duration
                total_energy += energy
                total_emissions += emissions

                print(f"\nSTEP: {file.stem}")
                outfile.write(f"\nSTEP: {file.stem}\n")

                print(f"duration_seconds: {duration}")
                outfile.write(f"duration_seconds: {duration}\n")

                print(f"energy_consumed_kwh: {energy}")
                outfile.write(f"energy_consumed_kwh: {energy}\n")

                print(f"emissions_kg: {emissions}")
                outfile.write(f"emissions_kg: {emissions}\n")

    print("\nTOTALS")
    outfile.write("\nTOTALS\n")

    print(f"total_duration_seconds: {total_duration}")
    outfile.write(f"total_duration_seconds: {total_duration}\n")

    print(f"total_energy_kwh: {total_energy}")
    outfile.write(f"total_energy_kwh: {total_energy}\n")

    print(f"total_emissions_kg: {total_emissions}")
    outfile.write(f"total_emissions_kg: {total_emissions}\n")

    outfile.close()