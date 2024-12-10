from utils.input_reader import ingest
import pytest
import part1
import part2


# format options: raw, line, tuple, list
file_format = "line"
base_type = str
example_result_part1 = 4512
example_result_part2 = 1924

example_data = ingest("./example.input", file_format, base_type)
real_data = ingest("./real.input", file_format, base_type)

@pytest.mark.skipif(not example_result_part1, reason="Example not provided")
def test_part1():
    # Check if the example data gives the expected answer before trying the production data
    assert part1.run(example_data.copy()) == example_result_part1

    # If test passed, perform production run
    print("\nPart 1 Results\n----------------\n")
    print(part1.run(real_data.copy()))

@pytest.mark.skipif(not example_result_part2, reason="Example not provided")
def test_part2():
    # Don't run test if example result isn't provided
    if not example_result_part2:
        pytest.skip()

    # Check if the example data gives the expected answer before trying the production data
    assert part2.run(example_data.copy()) == example_result_part2

    # If test passed, perform production run
    print("\nPart 2 Results\n----------------\n")
    print(part2.run(real_data.copy()))



