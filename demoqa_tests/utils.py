from pathlib import Path
import demoqa_tests


def path_to(file_name):
    return str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{file_name}'))