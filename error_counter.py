import sys

def compare_csv_files(file1_path, file2_path):
    num_differences = 0
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        for line1, line2 in zip(file1, file2):
            if line1.strip() != line2.strip():
                num_differences += 1
    return num_differences

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file1_path>")
        sys.exit(1)
    
    file1_path = sys.argv[1]
    file2_path = "./datasets/adults/adults_clean.csv"

    differences = compare_csv_files(file1_path, file2_path)
    print(f'Number of different lines: {differences}')