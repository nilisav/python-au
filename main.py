def get_files():
    txt_file = open('first.txt', 'r')
    py_file = open('tests.py', 'r')
    return txt_file, py_file


solution, tests = get_files()
result_file = open('new_file.md', 'w')

result_file.write(' # ' + solution.readline() + '\n\n')
result_file.write('+ [' + solution.readline() + ']')
result_file.write('(#' + solution.readline() + ')\n\n')
result_file.write('## ' + solution.readline() + '\n')
result_file.write(solution.readline() + '\n')

# основная программа
result_file.write('```python\n')
result_file.write(solution.read() + '\n')
result_file.write('```\n\n')
solution.close()




# тесты
result_file.write('<details><summary>Test cases</summary><blockquote>\n\n')
result_file.write('```python\n')
result_file.write(tests.read() + '\n')
result_file.write('```\n\n')
result_file.write('</blockquote></details>\n\n')
tests.close()

result_file.close()

if __name__ == '__main__':
    print('Hello')

