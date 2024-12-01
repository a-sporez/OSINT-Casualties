import csv
import os
"""
TODO: Handle line breaks within a single cell
TODO: Print date in output file
TODO: Move input and output to archives
TODO: [Optional] Create a function to append the output and move the previous to archive
"""
# File paths
input_file = "input/data.csv"
output_dir = "output"
database_file = os.path.join(output_dir, "database.md")
log_file = os.path.join(output_dir, "log.md")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def read_csv(filepath):
    """Reads CSV data into a list of dictionaries, with flexible delimiter detection."""
    with open(filepath, "r", encoding="utf-8") as file:
        try:
            # Detect delimiter dynamically
            sample = file.read(1024)
            delimiter = ';' if ';' in sample else ','
            file.seek(0)
            reader = csv.DictReader(file, delimiter=delimiter)
            return list(reader)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []

def generate_markdown_table(data, headers):
    """Generates a properly formatted Markdown table with clickable URLs and sanitized text."""
    def sanitize(value):
        """Replaces line breaks with <br> and strips extra whitespace."""
        if value:
            return str(value).replace("\n", "<br>").strip()
        return ""

    table = []
    table.append("| " + " | ".join(headers) + " |")
    table.append("|" + " | ".join(["-" * len(header) for header in headers]) + "|")
    for row in data:
        row_data = []
        for header in headers:
            value = sanitize(row.get(header, "") or "")
            if header == "Profile URL" and value:
                # Convert to Markdown clickable link
                value = f"[Profile]({value})"
            row_data.append(value)
        table.append("| " + " | ".join(row_data) + " |")
    return "\n".join(table)

def generate_sorted_tables(data):
    """Generates Markdown tables sorted by Name and Date, with Date as first column in the second table."""
    try:
        # Sort by name
        sorted_by_name = sorted(data, key=lambda x: x.get("Name", ""))
        name_table = generate_markdown_table(sorted_by_name, list(data[0].keys()))

        # Sort by date
        sorted_by_date = sorted(data, key=lambda x: x.get("Date of death", ""))
        # Swap headers: "Date of death" will come first
        headers_with_date_first = ["Date of death"] + [header for header in list(data[0].keys()) if header != "Date of death"]
        date_table = generate_markdown_table(sorted_by_date, headers_with_date_first)

        return name_table, date_table
    except Exception as e:
        print(f"Error generating sorted tables: {e}")
        return "", ""

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
    if not csv_data:
        print("No data found or an error occurred during reading.")
    else:
        print("Generating Markdown files...")
        write_markdown(csv_data)
        print(f"Markdown files created in '{output_dir}' directory.")
