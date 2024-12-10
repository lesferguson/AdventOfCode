from collections import defaultdict


def base_type_conversion(value, base_type):
    try:
        return base_type(value)
    except ValueError:
        return value


# ingest and format data as necessary for functions
def ingest(filename, file_format, base_type=str):
    """
    file_format types:
    raw: raw
    line: line separated
    tuple: tuple per line
    list: comma seperated list per line, if only 1 line, only return the list for that line
    grid: return a dictionary of coordinate keys, with the value of that coord in the values



    :param filename:
    :param file_format:
    :param base_type:
    :return:
    """
    if file_format == "raw":
        data = open(filename).read()
    elif file_format == "line":
        data = [base_type_conversion(line.strip().strip(), base_type) for line in open(filename).readlines()]
    elif file_format == "tuple":
        data = [tuple([col for col in line.strip().split()]) for line in open(filename).readlines()]
    elif file_format == "list":
        data = [[base_type_conversion(val, base_type) for val in line.strip().split(",")] for line in
                open(filename).readlines()]
        if len(data) == 1:
            data = data[0]
    elif file_format == "grid":
        data = {}
        for j, line in enumerate(open(filename).readlines()):
            for i, value in enumerate(line.strip()):
                data[(i, j)] = base_type_conversion(value, base_type)

    return data
