from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        highest_salary = 0
        for job in self.jobs_list:
            if 'max_salary' in job and job['max_salary'].isnumeric():
                highest_salary = max(highest_salary, int(job['max_salary']))
        return highest_salary

    def get_min_salary(self) -> int:
        lowest_salary = 100000
        for job in self.jobs_list:
            if 'min_salary' in job and job['min_salary'].isnumeric():
                lowest_salary = min(lowest_salary, int(job['min_salary']))
        return lowest_salary

    def job_validation(self, job: Dict):
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError("Faltam informações de salário mínimo e máximo")

    def salary_validation(self, value: Union[int, str]) -> int:
        try:
            return int(value)
        except (ValueError, TypeError):
            raise ValueError("Entrada inválida")

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        self.job_validation(job)
        min_salary = self.salary_validation(job['min_salary'])
        max_salary = self.salary_validation(job['max_salary'])
        if min_salary > max_salary:
            raise ValueError("Entrada inválida")
        return min_salary <= self.salary_validation(salary) <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
