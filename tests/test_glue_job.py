from src.glue_job import process_data


def test_process_data():
    result = process_data()

    assert result == [20, 40, 60, 80, 100]