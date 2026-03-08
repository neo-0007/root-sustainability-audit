from codecarbon import EmissionsTracker
from pathlib import Path


def monitor_step(step_name, func, *args, **kwargs):

    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    tracker = EmissionsTracker(
        project_name=step_name,
        output_dir=str(output_dir),
        output_file=f"{step_name}.csv"
    )

    tracker.start()

    result = func(*args, **kwargs)

    tracker.stop()

    return result