import time
from multiprocessing import Pool
from functools import wraps
from pprint import pprint
from typing import List, Tuple, Any

from resources import category_health_risk, data


def timeit(func):
    """
    decorator to calculate function execution time
    """

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def get_bmi(input_data: dict) -> float:
    """
    calculate bmi using formula:
        BMI(kg/m2) = mass(kg) / height(m)2

    """
    return round(input_data["WeightKg"] / (input_data["HeightCm"] / 100) ** 2, 2)


def calculate_bmi_with_category_health_risk(input_data: dict) -> Tuple[Any, Any]:
    """
    get bmi from calculate_bmi
    calculate bmi related category and health risk from the table category_health_risk
    """

    bmi = get_bmi(input_data)
    for key, value in category_health_risk.items():
        if key[0] < bmi < key[1]:
            return bmi, *value


@timeit
def calculate_bmi_sequentially(input_data: list) -> List[Tuple[Any, Any]]:
    """
    calculate bmi of a million records sequentially
    """

    results = []
    for record in input_data:
        bmi = get_bmi(record)
        for key, value in category_health_risk.items():
            if key[0] < bmi < key[1]:
                results.append((bmi, *value))

    return results


@timeit
def calculate_bmi_in_parallel(input_data: list) -> List[Tuple[Any, Any]]:
    """
    calculate bmi of a million records in parallel using multiprocessing
    """
    with Pool(4) as p:
        result = p.map(calculate_bmi_with_category_health_risk, input_data)
    return result


@timeit
def get_total_overweight_count(input_data: List[dict]) -> int:
    total_count = 0
    for record in input_data:
        bmi = get_bmi(record)
        if bmi > 25.0:
            total_count += 1

    print(f"There are total {total_count} Overweight among total {len(input_data)} ")
    return total_count


if __name__ == "__main__":
    # start running this file directly
    results = calculate_bmi_sequentially(data)
    pprint(results[:10])

    # to speed up process i have used multiprocessing
    results = calculate_bmi_in_parallel(data)

    # get count of total overweight from the data
    get_total_overweight_count(data)
