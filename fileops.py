def read_file_to_memory(file_path):
    file = open(file_path, "r")
    memory = append_lines_to_memory(file)
    file.close()
    return memory


def append_lines_to_memory(opened_file):
    memory = []

    for line in opened_file:
        line = line.replace(',', '').replace('(', '').replace(')', ' ')
        values = line.split()
        memory.append(values)

    return memory
