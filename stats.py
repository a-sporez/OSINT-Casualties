import csv
import os
import matplotlib.pyplot as plt

# File paths
input_file = "input/data.csv"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

def read_csv(filepath):
    """Reads CSV data into a list of dictionaries."""
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader), reader.fieldnames

def analyze_column_values(data, headers):
    """Analyzes the frequency of values in each column."""
    column_stats = {header: {} for header in headers}
    for row in data:
        for header in headers:
            value = row.get(header, "Unknown").strip()
            column_stats[header][value] = column_stats[header].get(value, 0) + 1
    return column_stats

def create_pie_chart(data, column_name):
    """Creates and saves a pie chart for a column's data."""
    labels = list(data.keys())
    sizes = list(data.values())
    colors = [plt.cm.Paired(i / float(len(labels))) for i in range(len(labels))]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f"Distribution of {column_name}")
    chart_file = os.path.join(output_dir, f"{column_name}_pie_chart.png")
    plt.savefig(chart_file, bbox_inches="tight")
    plt.close()
    return chart_file

def generate_markdown(stats, headers):
    """Generates a Markdown report with statistics and embedded pie charts."""
    markdown = ["# Column Statistics and Pie Charts\n"]
    for header in headers:
        unique_values = len(stats[header])
        if unique_values > 30:
            print(f"Skipping column '{header}' with {unique_values} unique values.")
            continue  # Skip columns with more than 10 unique values

        markdown.append(f"## {header}\n")
        markdown.append("| Value | Count |")
        markdown.append("|-------|-------|")
        for value, count in sorted(stats[header].items(), key=lambda x: x[1], reverse=True):
            markdown.append(f"| {value} | {count} |")
        markdown.append("\n")

        # Add the pie chart
        chart_file = create_pie_chart(stats[header], header)
        markdown.append(f"![{header} Distribution]({chart_file})\n")
    return "\n".join(markdown)

def write_markdown(markdown_content):
    """Writes the Markdown report to a file."""
    output_file = os.path.join(output_dir, "column_stats.md")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(markdown_content)
    print(f"Markdown report with pie charts saved to '{output_file}'")

# Main script execution
if __name__ == "__main__":
    print("Reading CSV data...")
    csv_data, headers = read_csv(input_file)

    print("Analyzing column values...")
    column_stats = analyze_column_values(csv_data, headers)

    print("Generating Markdown report...")
    markdown_content = generate_markdown(column_stats, headers)
    write_markdown(markdown_content)

    print("Done!")