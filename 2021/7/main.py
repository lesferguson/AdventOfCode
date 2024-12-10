from utils.input_reader import ingest
import pytest
import part1
import part2
from copy import deepcopy


# format options: raw, line, tuple, list
file_format = "list"
base_type = int
example_result_part1 = 37
example_result_part2 = 168

example_data = ingest("./example.input", file_format, base_type)[0]
real_data = ingest("./real.input", file_format, base_type)[0]

@pytest.mark.skipif(not example_result_part1, reason="Example not provided")
def test_part1():
    # Check if the example data gives the expected answer before trying the production data
    assert part1.run(deepcopy(example_data)) == example_result_part1

    # If test passed, perform production run
    print("\nPart 1 Results\n----------------\n")
    print(part1.run(deepcopy(real_data)))

@pytest.mark.skipif(not example_result_part2, reason="Example not provided")
def test_part2():
    # Don't run test if example result isn't provided
    if not example_result_part2:
        pytest.skip()

    # Check if the example data gives the expected answer before trying the production data
    assert part2.run(deepcopy(example_data)) == example_result_part2

    # If test passed, perform production run
    print("\nPart 2 Results\n----------------\n")
    print(part2.run(deepcopy(real_data)))



