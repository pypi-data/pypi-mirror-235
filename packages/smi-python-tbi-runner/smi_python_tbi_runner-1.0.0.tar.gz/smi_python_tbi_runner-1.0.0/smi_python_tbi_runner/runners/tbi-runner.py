import logging

from smi_python_commons.config.application import Application
from smi_python_runner.services.runner_register_service import runner_register_service

log = logging.getLogger(__name__)

logging.info("Loaded module")


# For probing set up: export RUNNERS_PREFIX=smi_python_tbi_runner
class RunnerTbiSubX:

    def __init__(self):
        self.name = "tbi-runner"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        log.info("Command (Loaded module): " + sub_command)
        return 0


def init():
    logging.info("Init loaded module")
    runner_register_service.register(RunnerTbiSubX())
