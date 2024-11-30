import csv
import os

# File paths
input_file = "input/data.csv"
output_dir = "output"
database_file = os.path.join(output_dir, "database.md")
log_file = os.path.join(output_dir, "log.md")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def read_csv(filepath):
    """Reads CSV data into a list of dictionaries, with semicolons as delimiter."""
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)

def generate_markdown_table(data, headers):
    """Generates a properly formatted Markdown table."""
    table = []
    table.append("| " + " | ".join(headers) + " |")
    table.append("|" + " | ".join(["-" * len(header) for header in headers]) + "|")
    for row in data:
        row_data = "| " + " | ".join((row.get(header, "") or "") for header in headers) + " |"
        table.append(row_data)
    return "\n".join(table)

def generate_sorted_tables(data):
    """Generates Markdown tables sorted by Name and Date, with Date as first column in the second table."""
    # Sort by name
    sorted_by_name = sorted(data, key=lambda x: x["Name"])
    name_table = generate_markdown_table(sorted_by_name, list(data[0].keys()))

    # Sort by date
    sorted_by_date = sorted(data, key=lambda x: x["Date of death"])
    # Swap headers: "Date of death" will come first
    headers_with_date_first = ["Date of death"] + [header for header in list(data[0].keys()) if header != "Date of death"]
    date_table = generate_markdown_table(sorted_by_date, headers_with_date_first)

    return name_table, date_table

def write_markdown(data):
    """Writes the Markdown database and README files."""
    name_table, date_table = generate_sorted_tables(data)

    # Write database.md
    with open(database_file, "w", encoding="utf-8") as db_file:
        db_file.write("# Database\n\n")
        db_file.write("## **Sorted by Name**\n\n")
        db_file.write(name_table)
        db_file.write("\n\n---\n\n")
        db_file.write("## **Sorted by Date of Passing**\n\n")
        db_file.write(date_table)

    # Write README.md
    with open(log_file, "w", encoding="utf-8") as log:
        log.write("# Database Index\n\n")
        log.write("Welcome to the database repository. Below, you can find quick links to the sorted tables:\n\n")
        log.write("1. [Sorted by Name](database.md#sorted-by-name)\n")
        log.write("2. [Sorted by Date of Passing](database.md#sorted-by-date-of-passing)\n")

# Main script execution
if __name__ == "__main__":
    print("Reading CSV data...")
    csv_data = read_csv(input_file)

    print("Generating Markdown files...")
    write_markdown(csv_data)

    print(f"Markdown files created in '{output_dir}' directory.")