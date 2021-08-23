#!/usr/bin/env python
import glob
import os
import time

try:
    # Try to import the latest agent libraries
    from datadog_checks.base import AgentCheck
except ImportError:
    # if the above failed, the check is running in Agent version < 6.6.0
    from checks import AgentCheck

__version__ = "1.0.0"


class NewestFileAgeCheck(AgentCheck):
    def check(self, instance):
        list_of_files = glob.glob(self.instance["file_pattern"])
        latest_file = max(list_of_files, key=os.path.getmtime)
        age_in_seconds = time.time() - os.path.getmtime(latest_file)
        age_in_hours = int(age_in_seconds / 3600)
        self.gauge(
            self.instance["name"] + ".newest_file_age.hours",
            age_in_hours,
            self.instance.get("tags", []),
        )
