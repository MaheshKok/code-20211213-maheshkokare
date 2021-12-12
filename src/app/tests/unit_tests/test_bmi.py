import pytest


from main import (
    calculate_bmi_sequentially,
    calculate_bmi_in_parallel,
    get_total_overweight_count,
)


@pytest.fixture
def test_data():
    return (
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 145, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 135, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 175, "WeightKg": 60},
    )


def test_get_bmi_sequentially(test_data):
    results = calculate_bmi_sequentially(test_data)

    assert results == [
        (32.83, "Moderately obese", "Medium risk"),
        (36.62, "Severely obese", "High risk"),
        (42.25, "Very severely obese", "above Very high risk"),
        (19.59, "Normal weight", "Low risk"),
    ]


def test_get_bmi_in_parallel(test_data):
    results = calculate_bmi_in_parallel(test_data)

    assert results == [
        (32.83, "Moderately obese", "Medium risk"),
        (36.62, "Severely obese", "High risk"),
        (42.25, "Very severely obese", "above Very high risk"),
        (19.59, "Normal weight", "Low risk"),
    ]


def test_total_overweight_count(test_data):
    count = get_total_overweight_count(test_data)
    assert count == 3


def test_get_bmi_sequentially_with_empty_lst():
    results = calculate_bmi_sequentially([])
    assert results == []


def test_get_bmi_in_parallel_with_empty_lst():
    results = calculate_bmi_in_parallel([])
    assert results == []
