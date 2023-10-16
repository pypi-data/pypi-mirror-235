import logging

from smi_python_commons.config.application import Application

log = logging.getLogger(__name__)


class TBIRunner:

    def __init__(self):
        self.name = "tbi-runner"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        log.info("Command: " + sub_command)
        return 0
