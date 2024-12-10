from utils.input_reader import ingest
import part1
import part2

# format options: raw, line, tuple, list
file_format = "line"

def test_part1():
    # do test on example data
    example_data = ingest("example.input", file_format, base_type=int)

    example_result = 7

    assert part1.run(example_data) == example_result

    # if test passed, do the real input
    real_data = ingest("real.input", file_format, base_type=int)

    print("\nPart 1 Results\n----------------\n")
    print(part1.run(real_data))



def test_part2():
    # do test on example data
    example_data = ingest("example.input", file_format, base_type=int)

    example_result = 5

    assert part2.run(example_data) == example_result

    # if test passed, do the real input
    real_data = ingest("real.input", file_format, base_type=int)

    print("\nPart 2 Results\n----------------\n")
    print(part2.run(real_data))



