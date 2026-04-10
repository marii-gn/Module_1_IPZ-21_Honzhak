import pytest
import os
from main import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        {'country': 'Ukraine', 'area': 603628.0, 'population': 41000000},
        {'country': 'Poland', 'area': 312696.0, 'population': 38000000}
    ]

@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "test_data.txt"
    f.write_text("Ukraine, 603628, 41000000\nPoland, 312696, 38000000")
    return str(f)

def test_read_data(temp_file):
    data = read_population_data(temp_file)
    assert len(data) == 2
    assert data[0]['country'] == 'Ukraine'

@pytest.mark.parametrize("sort_func, key", [
    (sort_by_area, 'area'),
    (sort_by_population, 'population')
])
def test_sorting(sample_data, sort_func, key):
    sorted_data = sort_func(sample_data)
    assert sorted_data[0][key] >= sorted_data[1][key]