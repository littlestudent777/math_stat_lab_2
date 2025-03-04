import numpy as np
import pandas as pd
import jinja2

def count_outliers(data):
    Q1 = np.quantile(data, 0.25)
    Q3 = np.quantile(data, 0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return len(outliers)


def print_outliers_table(ns, distributions):
    data = []

    # Fill data list
    for distribution_name, distribution_func in distributions:
        for n in ns:
            values = distribution_func(n)
            outliers_count = count_outliers(values)

            data.append({
                'Distribution': distribution_name,
                'Sample size': n,
                'Outliers': outliers_count
            })

    # Create dataframe from data list
    results = pd.DataFrame(data)

    # Group by distribution and generate LaTeX tables
    for distribution_name, group in results.groupby('Distribution'):
        # Select only 'Sample size' and 'Outliers' columns
        table_data = group[['Sample size', 'Outliers']]

        # Generate LaTeX table
        latex_table = table_data.to_latex(index=False, caption=f"{distribution_name} distribution", label=f"tab:{distribution_name}")
        latex_table = latex_table.replace('\\begin{table}', '\\begin{table}[H] \\centering')
        latex_table = latex_table.replace('\\caption{', '\\caption*{')
        print(latex_table)
