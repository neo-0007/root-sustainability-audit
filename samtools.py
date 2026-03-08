import subprocess
from pathlib import Path


def bam_to_sam(bam_file, output_sam):
    """
    Convert BAM file to SAM

    bam_file: input BAM
    output_sam: output SAM
    """

    with open(output_sam, "w") as f:
        subprocess.run(
            ["samtools", "view", "-h", bam_file],
            stdout=f,
            check=True
        )

    print("Converted BAM to SAM")

    return output_sam