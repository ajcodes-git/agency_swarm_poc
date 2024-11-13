from agency_swarm.tools import BaseTool
from pydantic import Field
import matplotlib.pyplot as plt
import seaborn as sns


class ChartGenerationTool(BaseTool):
    def __init__(self):
        sns.set_theme(style="whitegrid")

    def create_bar_chart(self, data, x, y, title="Bar Chart", xlabel="", ylabel=""):
        """
        Generates a bar chart based on the provided data.

        Parameters:
        - data: DataFrame containing the data for the chart
        - x: Column name for x-axis values
        - y: Column name for y-axis values
        - title: Title of the chart
        - xlabel: Label for x-axis
        - ylabel: Label for y-axis
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x=x, y=y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def create_line_chart(self, data, x, y, title="Line Chart", xlabel="", ylabel=""):
        """
        Generates a line chart based on the provided data.

        Parameters:
        - data: DataFrame containing the data for the chart
        - x: Column name for x-axis values
        - y: Column name for y-axis values
        - title: Title of the chart
        - xlabel: Label for x-axis
        - ylabel: Label for y-axis
        """
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x=x, y=y, marker="o")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def create_pie_chart(self, labels, sizes, title="Pie Chart"):
        """
        Generates a pie chart based on the provided data.

        Parameters:
        - labels: Labels for each section of the pie chart
        - sizes: Sizes (values) for each section
        - title: Title of the chart
        """
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
        plt.show()


class GraphGenerationTool(BaseTool):
    pass



# Test tools
import pandas as pd

if __name__ == "__main__":
    # Sample data for demonstration
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [23, 45, 10, 33]
    })

    # Instantiate the ChartGenerator
    chart_generator = ChartGenerationTool()

    # Create a bar chart
    chart_generator.create_bar_chart(data=data, x='Category', y='Values', title="Sample Bar Chart", xlabel="Category", ylabel="Values")

    # Create a line chart (using the same data for simplicity)
    chart_generator.create_line_chart(data=data, x='Category', y='Values', title="Sample Line Chart", xlabel="Category", ylabel="Values")

    # Create a pie chart
    labels = data['Category']
    sizes = data['Values']
    chart_generator.create_pie_chart(labels=labels, sizes=sizes, title="Sample Pie Chart")

