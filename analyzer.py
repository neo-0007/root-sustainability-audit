from monitor import monitor_step
from ramtools import sam_to_ram, split_chromosomes, query_region
from download_dataset import download_file
from reporter import generate_report
from samtools import bam_to_sam
import shutil
from pathlib import Path

TOOLS_DIR = "tools"

# Runs each step of the workflow one by one and monitor and record measurements into csv files with codecarbon

def main():
    
    data_url = str(input("Enter the BAM data URL : "))
    
    # Download data , BAM file
    bam_file = monitor_step(
        "download_dataset",
        download_file,
        data_url,
        "data"
    )

    # Convert BAM to SAM since for now ramtools can work only with SAM files
    sam_file = monitor_step(
        "bam_to_sam_conversion",
        bam_to_sam,
        bam_file,
        "data/sample.sam"
    )

    # Convert SAM to RAM ( sequence alignment data stored as RNTuple in root file)
    monitor_step(
        "sam_to_ram_conversion",
        sam_to_ram,
        sam_file,
        "results/output.root",
        TOOLS_DIR
    )

    # Convert SAM to RAM and do chromosome based splitting
    monitor_step(
        "chromosome_split",
        split_chromosomes,
        sam_file,
        "results/output",
        TOOLS_DIR
    )
    
    def multiple_query():

        start = 10000
        step = 500
        region_size = 200

        for i in range(30):

            region_start = start + i * step
            region_end = region_start + region_size

            region = f"chr20:{region_start}-{region_end}"

            query_region(
                "results/output.root",
                region,
                TOOLS_DIR
            )

    # 
    monitor_step(
        "region_query",
        multiple_query,
    )

    # Reads the generated csv files and computes and prints the total metrics
    generate_report()
    
    # Clean up
    # Will not measure this step since this does not count in for computation in real use case
    data_folder = Path("data")
    results_folder = Path("results")
    if data_folder.exists():
        shutil.rmtree(data_folder)
    if results_folder.exists():
        shutil.rmtree(results_folder)

if __name__ == "__main__":
    main()
