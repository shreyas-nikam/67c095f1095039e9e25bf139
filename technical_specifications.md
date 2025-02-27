# Derivatives Risk Assessment Tool - Technical Specifications

## Overview
This document provides a detailed technical specification for the Derivatives Risk Assessment Tool, a single-page Streamlit application. This application is designed to assess the risk associated with synthetic derivative portfolios, emphasizing real-time interaction and immediate data-driven insights.

## Learning Outcomes
### Learning Outcomes
- Gain a clear understanding of the key insights derived from the uploaded document.
- Learn how to transform raw data into interactive visualizations using Streamlit.
- Understand the process of data preprocessing and exploration.
- Develop an intuitive, user-friendly application that explains the underlying data concepts.

## Dataset Details
### Dataset Details
- **Source**: A synthetic dataset generated to mimic the structure and characteristics of the uploaded document.
- **Content**: Includes realistic data features such as numeric values, categorical variables, and time-series data, providing a comprehensive sample for data handling.
- **Purpose**: Demonstrates data handling and visualization techniques, allowing users to explore derivatives risk in a controlled environment.

## Functional Specifications

### Input Forms
- **Notional Amount**: Accepts numeric input reflecting the total value of the portfolio.
- **Underlying Asset**: Dropdown list of available synthetic assets.
- **Option Type**: Radio buttons to select types like Call or Put.
- **Strike Price**: Numeric input for the option's strike price.
- **Expiration Date**: Date picker to define the option's expiration.

### Risk Factor Selection
- **Volatility**: Slider to adjust the level of asset volatility.
- **Interest Rate**: Input field for the current risk-free interest rate.
- **Market Scenarios**: Multiselect for various pre-defined market conditions (bull, bear, etc.).

### Visualizations
### Visualizations Details
- **Interactive Charts**: 
  - Dynamic line charts and bar graphs to display potential loss and profit trends.
  - Scatter plots to show correlation between risk factors and portfolio outcomes.
- **Annotations & Tooltips**: Adds detailed insights and explanations on charts, aiding in data interpretation.

### Real-Time Sensitivity Analysis
- Displays changes in portfolio risk when altering any input parameters.
- Updates visualizations in real-time to reflect the selected inputs and calculated risk metrics.

### User Interaction and Documentation
### Additional Details
- **User Interaction**: 
  - Input forms and sliders for parameter adjustment.
  - Real-time updates visible in charts and graphs upon interaction.
- **Documentation**: 
  - Inline help sections and tooltips for guidance through the data exploration process.
  - Built-in explanations of derivative risk concepts to aid learning.

## Application Architecture
- **Streamlit Framework**: Utilizes Streamlit to create a seamless and interactive single-page application.
- **Data Loading**: Reads the synthetic dataset at startup, caches it for efficient access.
- **Data Preprocessing**: Handles necessary data transformations and cleaning before analysis.
- **Visualization Layer**: Leverages Streamlit's built-in support for Plotly and Matplotlib for interactive visualizations.

## How It Explains the Concept
This application demonstrates the principles outlined in derivatives risk management by simulating stress scenarios and evaluating their effects on a fake portfolio. Users gain practical insights into derivative dynamics, enhancing their comprehension of intricate risk management frameworks as detailed in the accompanying document. The real-time sensitivity analysis underscores the document's theory by linking theoretical risk concepts to observable phenomena.

By using a synthetic dataset and established risk metrics, the application provides a tangible exploration of derivative portfolio risks, making abstract theories accessible and comprehensible through visual and interactive means.

## References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly for Python](https://plotly.com/python/)
- [Synthetic Data Generation: Concepts and Techniques](https://towardsdatascience.com/synthetic-data-generation-a-bridge-into-the-future-c19324c04cd2)