import argparse

def analyze_code(file_path):
    try:
        with open(file_path, 'r') as file1:
            lines = file1.readlines()

        empty_lines, hash_comments, triple_quotes, line_count = 0, 0, 0, 0
        flag, flag_count, lines_to_exclude = False, 0, []

        for line in lines:
            stripped_line = line.strip()
            line_count += 1

            if stripped_line == "":
                lines_to_exclude.append(1)
                empty_lines += 1
                continue
            elif stripped_line.startswith("#"):
                lines_to_exclude.append(1)
                hash_comments += 1
                continue

            triple_quotes_marker = '"""'
            if str(line)[0:3] == triple_quotes_marker and not flag:
                flag_count = line_count
                flag = True
                continue
            elif str(line)[0:3] == triple_quotes_marker and flag:
                lines_to_exclude.append(line_count - flag_count + 1)
                triple_quotes += line_count - flag_count + 1
                flag = False
                continue
            elif str(line)[-4:-1] == triple_quotes_marker and flag:
                lines_to_exclude.append(line_count - flag_count + 1)
                triple_quotes += line_count - flag_count + 1
                flag = False

        total_lines = len(lines)
        actual_lines = total_lines - sum(lines_to_exclude)

        return total_lines, actual_lines, sum(lines_to_exclude), hash_comments, triple_quotes, empty_lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


def print_code_analysis(total_lines, actual_lines, excluded_lines, hash_comments, triple_quotes, empty_lines):
    print("""
 ____                       _
|  _ \ ___ _ __   ___  _ __| |_
| |_) / _ \ '_ \ / _ \| '__| __|
|  _ <  __/ |_) | (_) | |  | |_
|_| \_\___| .__/ \___/|_|   \__|
          |_|
    """)

    print(f"\n\nTotal lines of your code: {total_lines}\n")
    print(f"Actual lines of your code: {actual_lines}\n")
    print(f"Number of lines excluded from your code: {excluded_lines}\n\n")
    print(f"Number of lines with hash (#) comments: {hash_comments}\n")
    print(f'Number of lines with triple quotes (\"\"\") comments: {triple_quotes}\n')
    print(f'Number of empty lines in your code: {empty_lines}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code Analyzer')
    parser.add_argument('--path', type=str, help='Path of the file to analyze')
    args = parser.parse_args()
    
    analysis_results = analyze_code(args.path)
    if analysis_results:
        print_code_analysis(*analysis_results)
