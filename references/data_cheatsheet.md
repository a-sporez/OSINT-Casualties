### Working with Datasets in Python

Once you have found a suitable dataset, you can use Python to analyze it. Below is an example of how to load and analyze a CSV dataset using pandas:

```python
import pandas as pd

# Load dataset
url = 'URL_TO_YOUR_DATASET.csv'
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())

# Basic information about the dataset
print(df.info())

# Descriptive statistics
print(df.describe())

# Example: Counting the number of deaths per year
deaths_per_year = df.groupby('Year')['Deaths'].sum()
print(deaths_per_year)
```

Replace `'URL_TO_YOUR_DATASET.csv'` with the actual URL or file path of your dataset. The example assumes the dataset has columns named 'Year' and 'Deaths'.

### Visualization

To visualize the data, you can use libraries like matplotlib or seaborn:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting deaths per year
plt.figure(figsize=(10, 6))
sns.lineplot(data=deaths_per_year)
plt.title('Mental Health Drug Deaths per Year in Canada')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.show()
```

Sure! Here's a comprehensive cheatsheet for using the `pandas` library in Python, which is widely used for data manipulation and analysis.

### Pandas Cheatsheet

#### Importing Pandas
```python
import pandas as pd
```

#### Creating DataFrames

- **From a dictionary:**
  ```python
  data = {'col1': [1, 2], 'col2': [3, 4]}
  df = pd.DataFrame(data)
  ```

- **From a CSV file:**
  ```python
  df = pd.read_csv('file_path.csv')
  ```

- **From an Excel file:**
  ```python
  df = pd.read_excel('file_path.xlsx', sheet_name='Sheet1')
  ```

#### Viewing DataFrame

- **Display first n rows:**
  ```python
  df.head(n)
  ```

- **Display last n rows:**
  ```python
  df.tail(n)
  ```

- **Get DataFrame info:**
  ```python
  df.info()
  ```

- **Get summary statistics:**
  ```python
  df.describe()
  ```

#### Selecting Data

- **Select a column:**
  ```python
  df['column_name']
  ```

- **Select multiple columns:**
  ```python
  df[['col1', 'col2']]
  ```

- **Select rows by index:**
  ```python
  df.iloc[0]  # First row
  df.iloc[0:5]  # First 5 rows
  ```

- **Select rows by condition:**
  ```python
  df[df['column_name'] > value]
  ```

#### Data Manipulation

- **Add new column:**
  ```python
  df['new_column'] = df['col1'] + df['col2']
  ```

- **Drop column:**
  ```python
  df.drop('column_name', axis=1, inplace=True)
  ```

- **Rename columns:**
  ```python
  df.rename(columns={'old_name': 'new_name'}, inplace=True)
  ```

- **Filter rows:**
  ```python
  df_filtered = df[df['column_name'] > value]
  ```

- **Sort DataFrame:**
  ```python
  df.sort_values('column_name', ascending=False, inplace=True)
  ```

#### Handling Missing Values

- **Check for missing values:**
  ```python
  df.isnull().sum()
  ```

- **Drop rows with missing values:**
  ```python
  df.dropna(inplace=True)
  ```

- **Fill missing values:**
  ```python
  df.fillna(value, inplace=True)
  ```

#### Grouping and Aggregation

- **Group by column:**
  ```python
  grouped = df.groupby('column_name')
  ```

- **Aggregate data:**
  ```python
  df.groupby('column_name').agg({'col1': 'sum', 'col2': 'mean'})
  ```

- **Apply multiple functions:**
  ```python
  df.groupby('column_name').agg(['sum', 'mean'])
  ```

#### Merging and Joining

- **Concatenate DataFrames:**
  ```python
  pd.concat([df1, df2], axis=0)  # Vertical
  pd.concat([df1, df2], axis=1)  # Horizontal
  ```

- **Merge DataFrames:**
  ```python
  pd.merge(df1, df2, on='common_column')
  ```

- **Join DataFrames:**
  ```python
  df1.join(df2.set_index('key'), on='key')
  ```

#### Exporting Data

- **To CSV:**
  ```python
  df.to_csv('file_path.csv', index=False)
  ```

- **To Excel:**
  ```python
  df.to_excel('file_path.xlsx', sheet_name='Sheet1', index=False)
  ```

This cheatsheet covers the most common operations you might need when working with pandas.

# Matplotlib Cheatsheet

A quick reference guide for the Matplotlib library, covering common use cases and functions.

---

## 1. **Getting Started**
```python
import matplotlib.pyplot as plt
```

### Basic Plot
```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Basic Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

### Common Imports
```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## 2. **Plot Types**

### Line Plot
```python
plt.plot(x, y, label="Line Label")
plt.legend()
plt.show()
```

### Scatter Plot
```python
plt.scatter(x, y, c="red", label="Scatter Label")
plt.legend()
plt.show()
```

### Bar Plot
```python
plt.bar(categories, values, color="blue")
plt.show()
```

### Histogram
```python
plt.hist(data, bins=10, color="green")
plt.show()
```

### Pie Chart
```python
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.show()
```

---

## 3. **Figure and Axes**

### Create Subplots
```python
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)
plt.show()
```

### Set Figure Size
```python
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.show()
```

---

## 4. **Styling**

### Colors
- Named colors: `'red'`, `'blue'`, `'green'`
- Hex codes: `'#FF5733'`
- RGB tuples: `(0.1, 0.2, 0.5)`

### Linestyles
- Solid: `'-'`
- Dashed: `'--'`
- Dotted: `':'`

### Markers
- Circle: `'o'`
- Square: `'s'`
- Star: `'*'`

### Combine Styles
```python
plt.plot(x, y, color="red", linestyle="--", marker="o")
```

---

## 5. **Annotations and Text**

### Add Title and Labels
```python
plt.title("Title")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
```

### Annotate Points
```python
plt.annotate("Point A", xy=(x, y), xytext=(x+1, y+1),
             arrowprops=dict(facecolor='black', shrink=0.05))
```

---

## 6. **Legends**

### Add Legend
```python
plt.plot(x, y, label="Label 1")
plt.legend(loc="upper left")
```

### Customize Legend
```python
plt.legend(title="Legend Title", loc="best")
```

---

## 7. **Advanced Features**

### Logarithmic Scale
```python
plt.xscale("log")
plt.yscale("log")
```

### Twin Axes
```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, "g-")
ax2.plot(x, y2, "b-")
plt.show()
```

### Grid
```python
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
```

---

## 8. **Saving Figures**
```python
plt.savefig("figure.png", dpi=300, bbox_inches="tight")
```

---

## 9. **Common Errors**
- `ValueError: x and y must have same first dimension`: Ensure `x` and `y` have the same length.
- `RuntimeError: Invalid DISPLAY`: If using Matplotlib on a server, use a backend like `Agg`:
  ```python
  import matplotlib
  matplotlib.use('Agg')
  ```

# Seaborn Cheatsheet

A quick reference guide for the Seaborn library, covering common use cases and functions.

---

## 1. **Getting Started**
```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Example Dataset
```python
data = sns.load_dataset("iris")
```

---

## 2. **Plot Types**

### Scatter Plot
```python
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.show()
```

### Line Plot
```python
sns.lineplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.show()
```

### Bar Plot
```python
sns.barplot(data=data, x="species", y="sepal_length")
plt.show()
```

### Histogram
```python
sns.histplot(data=data, x="sepal_length", bins=10, kde=True)
plt.show()
```

### Box Plot
```python
sns.boxplot(data=data, x="species", y="sepal_length")
plt.show()
```

### Violin Plot
```python
sns.violinplot(data=data, x="species", y="sepal_length")
plt.show()
```

---

## 3. **Customizing Plots**

### Colors
- Use built-in palettes: `'deep'`, `'muted'`, `'bright'`, `'dark'`, `'colorblind'`
```python
sns.set_palette("muted")
```

### Styling
```python
sns.set_style("whitegrid")  # Options: "darkgrid", "whitegrid", "dark", "white", "ticks"
```

### Context
```python
sns.set_context("talk")  # Options: "paper", "notebook", "talk", "poster"
```

---

## 4. **Pairplot**

### Create Pairplot
```python
sns.pairplot(data, hue="species", diag_kind="kde")
plt.show()
```

---

## 5. **Heatmap**

### Correlation Heatmap
```python
corr = data.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

---

## 6. **FacetGrid**

### Create a FacetGrid
```python
g = sns.FacetGrid(data, col="species")
g.map(sns.histplot, "sepal_length")
plt.show()
```

---

## 7. **Regression Plots**

### Simple Linear Regression
```python
sns.regplot(data=data, x="sepal_length", y="sepal_width")
plt.show()
```

### Multiple Regression Plots
```python
sns.lmplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.show()
```

---

## 8. **Saving Figures**
```python
plt.savefig("seaborn_plot.png", dpi=300, bbox_inches="tight")
```

---

## 9. **Common Errors**
- `ValueError: Could not interpret input`: Ensure column names match your dataset.
- `AttributeError: module 'seaborn' has no attribute '...`: Check for typos in function names or outdated Seaborn version.