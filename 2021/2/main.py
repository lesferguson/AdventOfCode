from utils.input_reader import ingest
import pytest
import part1
import part2

# format options: raw, line, tuple, list
file_format = "tuple"
base_type = str
example_result_part1 = 150
example_result_part2 = 900

example_data = ingest("./example.input", file_format, base_type)
real_data = ingest("./real.input", file_format, base_type)

@pytest.mark.skipif(not example_result_part1, reason="Example 1 not provided")
def test_part1():


    assert part1.run(example_data) == example_result_part1



    print("\nPart 1 Results\n----------------\n")
    print(part1.run(real_data))


@pytest.mark.skipif(not example_result_part2, reason="Example 2 not provided")
def test_part2():

    assert part2.run(example_data) == example_result_part2



    print("\nPart 2 Results\n----------------\n")
    print(part2.run(real_data))



