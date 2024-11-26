import pytest
import os
import csv
from task2.solution import count_animals, write_to_csv_file 

@pytest.fixture
def mock_animals_dict():
    return {letter: 0 for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"}


def test_count_animals(mock_animals_dict):
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    animals_count = count_animals(base_url, mock_animals_dict)
    
    assert isinstance(animals_count, dict)
    assert len(animals_count) > 0
    for letter in animals_count.keys():
        assert letter in mock_animals_dict

def test_write_to_csv_file(tmp_path):
    data = {"А": 10, "Б": 20, "В": 30}
    csv_file_path = tmp_path / "beasts.csv"
    
    write_to_csv_file(data, csv_file_path)
    
    assert os.path.exists("task2/beasts.csv")
    
    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        
        assert len(rows) == len(data)
        
        for row in rows:
            letter = row[0]
            count = int(row[1])
            assert letter in data
            assert count == data[letter]
