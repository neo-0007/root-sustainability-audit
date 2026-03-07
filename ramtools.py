"""
This will contain all the ramtool functions
will call ramtools as subprocesses
just python wrapper for our tools so we can use codecarbon to monitor usage
"""

import subprocess
from pathlib import Path


def sam_to_ram(sam_file, output_root, tools_dir):
    """
    Convert a SAM file to RAM (ROOT RNTuple format)
    sam_file (str): input SAM file
    output_root (str): output ROOT file
    tools_dir (str): path to ramtools/build/tools
    """

    executable = Path(tools_dir) / "samtoramntuple"

    subprocess.run(
        [str(executable), sam_file, output_root],
        check=True
    )

    print("Converted to RAM")


def split_chromosomes(sam_file, output_prefix, tools_dir):
    """
    Split SAM into chromosome-specific RAM files
    sam_file (str): input SAM file
    output_prefix (str): prefix for output files
    tools_dir (str): path to ramtools/build/tools
    """

    executable = Path(tools_dir) / "samtoramntuple"

    subprocess.run(
        [str(executable), sam_file, output_prefix, "-split"],
        check=True
    )

    print("Chromosome splitting completed")


def query_region(root_file, region, tools_dir):
    """
    Query a genomic region from a RAM file
    root_file (str): RAM ROOT file
    region (str): genomic region (e.g. chr1:1000-2000)
    tools_dir (str): path to ramtools/build/tools
    """

    executable = Path(tools_dir) / "ramntupleview"

    subprocess.run(
        [str(executable), root_file, region],
        check=True
    )

    print(f"Query completed for {region}")