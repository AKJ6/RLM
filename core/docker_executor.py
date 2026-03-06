import subprocess
from config.settings import DOCKER_IMAGE

def run_python(code):

    command = [
        "sudo",
        "docker",
        "run",
        "--rm",
        DOCKER_IMAGE,
        "python",
        "-c",
        code
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.stdout + result.stderr