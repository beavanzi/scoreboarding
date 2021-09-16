import io

from fileops import append_lines_to_memory
from registers import Registers
from search import search


def run_tests():
    ## Cases de teste - mocks
    mock_file_four_instructions = io.StringIO("ld r1, (12)rb\nld r3, (16)rb\naddd r4, r2, r1\nsubd r5, r4, r2")
    mock_file_only_values = io.StringIO("8\n9\n90")

    memory_assert_four_instructions = [['ld', 'r1', '12', 'rb'], ['ld', 'r3', '16', 'rb'], ['addd', 'r4', 'r2', 'r1'],
                                       ['subd', 'r5', 'r4', 'r2']]
    memory_assert_only_values = [['8'], ['9'], ['90']]

    cases = dict([('success', (mock_file_four_instructions, memory_assert_four_instructions)),
                  ('only_values', (mock_file_only_values, memory_assert_only_values))])

    test_append_lines_to_memory(cases)
    test_search(cases)


def test_append_lines_to_memory(cases):
    for case, tuple in cases.items():
        if case == 'success':
            memory = append_lines_to_memory(tuple[0])
            assert memory == tuple[1]
        if case == 'only_values':
            memory = append_lines_to_memory(tuple[0])
            assert memory == tuple[1]


def test_search(cases):
    mock_regs = Registers()

    for case, tuple in cases.items():
        if case == "success":
            instruction_assert = tuple[1][0]
            search(tuple[1], mock_regs)
            assert mock_regs.ir == instruction_assert
        if case == 'only_values':
            instruction_assert = None
            search(tuple[1], mock_regs)
            assert mock_regs.ir == instruction_assert