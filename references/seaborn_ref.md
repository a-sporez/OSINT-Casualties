# Seaborn Cheatsheet

A quick reference guide for the Seaborn library, covering common use cases and functions, with detailed explanations and examples for each function.

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
- **Usage**: Create scatter plots to visualize the relationship between two variables.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`, `y`: Column names for the x and y axes.
  - `hue`: Grouping variable to color points by categories.
  - `style`: Grouping variable to differentiate point styles.
```python
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species", style="species")
plt.title("Scatter Plot Example")
plt.show()
```

### Line Plot
- **Usage**: Create line plots to visualize trends over a continuous variable.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`, `y`: Column names for the x and y axes.
  - `hue`: Grouping variable to create multiple lines.
```python
sns.lineplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.title("Line Plot Example")
plt.show()
```

### Bar Plot
- **Usage**: Create bar plots to compare categorical data.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`, `y`: Column names for the categorical and numeric variables.
  - `hue`: Grouping variable for stacked bars.
```python
sns.barplot(data=data, x="species", y="sepal_length", ci=None, palette="muted")
plt.title("Bar Plot Example")
plt.show()
```

### Histogram
- **Usage**: Display the distribution of a single variable.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`: Column name for the variable.
  - `bins`: Number of bins for the histogram.
  - `kde`: Whether to overlay a kernel density estimate.
```python
sns.histplot(data=data, x="sepal_length", bins=10, kde=True, color="blue")
plt.title("Histogram Example")
plt.show()
```

### Box Plot
- **Usage**: Visualize the distribution of a variable and detect outliers.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`, `y`: Column names for the categorical and numeric variables.
  - `hue`: Grouping variable for split boxes.
```python
sns.boxplot(data=data, x="species", y="sepal_length", palette="Set3")
plt.title("Box Plot Example")
plt.show()
```

### Violin Plot
- **Usage**: Combine box plots and kernel density plots to show data distribution.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `x`, `y`: Column names for the categorical and numeric variables.
  - `hue`: Grouping variable for split violins.
```python
sns.violinplot(data=data, x="species", y="sepal_length", split=True, palette="muted")
plt.title("Violin Plot Example")
plt.show()
```

---

## 3. **Customizing Plots**

### Colors
- **Usage**: Customize plot colors using built-in palettes or custom specifications.
- **Key Palettes**:
  - `'deep'`, `'muted'`, `'bright'`, `'dark'`, `'colorblind'`
```python
sns.set_palette("muted")
sns.barplot(data=data, x="species", y="sepal_length")
plt.title("Custom Palette Example")
plt.show()
```

### Styling
- **Usage**: Change the appearance of plots with styles and contexts.
- **Key Functions**:
  - `sns.set_style`: Options include "darkgrid", "whitegrid", "dark", "white", "ticks".
  - `sns.set_context`: Options include "paper", "notebook", "talk", "poster".
```python
sns.set_style("whitegrid")
sns.set_context("talk")
sns.lineplot(data=data, x="sepal_length", y="sepal_width", hue="species")
plt.title("Styled Plot Example")
plt.show()
```

---

## 4. **Pairplot**
- **Usage**: Generate pairwise scatter plots and histograms for numerical data.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `hue`: Grouping variable for coloring.
  - `diag_kind`: Type of plot for diagonal subplots (e.g., "kde" or "hist").
```python
sns.pairplot(data, hue="species", diag_kind="kde", palette="husl")
plt.show()
```

---

## 5. **Heatmap**
- **Usage**: Visualize matrix-like data (e.g., correlations) as a heatmap.
- **Key Parameters**:
  - `data`: Matrix or 2D array.
  - `annot`: Annotate cells with data values.
  - `cmap`: Color map (e.g., "coolwarm", "viridis").
```python
corr = data.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap Example")
plt.show()
```

---

## 6. **FacetGrid**
- **Usage**: Create grids of plots for different subsets of data.
- **Key Parameters**:
  - `data`: DataFrame containing the data.
  - `col`, `row`: Variables to create columns and rows.
  - `hue`: Grouping variable for plot elements.
```python
g = sns.FacetGrid(data, col="species", height=4)
g.map(sns.histplot, "sepal_length", bins=10, kde=True)
plt.show()
```

---

## 7. **Regression Plots**

### Simple Linear Regression
- **Usage**: Fit and plot a simple linear regression line.
```python
sns.regplot(data=data, x="sepal_length", y="sepal_width", scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Regression Plot Example")
plt.show()
```

### Multiple Regression Plots
- **Usage**: Create regression plots for multiple categories.
```python
sns.lmplot(data=data, x="sepal_length", y="sepal_width", hue="species", height=5, aspect=1.2)
plt.title("Multiple Regression Plot Example")
plt.show()
```

---

## 8. **Saving Figures**
- **Usage**: Save Seaborn plots to image files.
```python
plt.savefig("seaborn_plot.png", dpi=300, bbox_inches="tight")
```

---

## 9. **Common Errors**
- `ValueError: Could not interpret input`: Ensure column names match your dataset.
- `AttributeError: module 'seaborn' has no attribute '...`: Check for typos in function names or outdated Seaborn version.

