from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, newline='') as file:
            self.jobs_list = [row for row in csv.DictReader(file)]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
