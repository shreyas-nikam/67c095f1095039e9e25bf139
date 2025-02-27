import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date

st.set_page_config(page_title="QuCreate Derivatives Risk Assessment Tool", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Derivatives Risk Assessment Tool")
st.divider()

# Explanation of the application
st.markdown("""
    ## Welcome to the Derivatives Risk Assessment Tool!

    This interactive application is designed to help you understand the risk associated with derivative portfolios. 
    By adjusting various parameters, you can visualize how different market conditions and derivative specifications 
    impact potential portfolio outcomes. This tool is for educational purposes and uses a synthetic dataset to 
    demonstrate key concepts in derivatives risk management.

    **Learning Outcomes:**
    - Gain a clear understanding of derivatives risk factors.
    - Learn how changes in input parameters affect portfolio risk.
    - Visualize risk using interactive charts and graphs.
    - Understand the sensitivity of derivative positions to market variables.

    Let's start by configuring your synthetic derivative portfolio in the sidebar to the left.
    """)

st.sidebar.header("Portfolio Configuration")

# Input Forms in Sidebar
notional_amount = st.sidebar.number_input("Notional Amount", value=100000, step=10000)
st.sidebar.markdown("Enter the total notional value of the derivative portfolio.")

underlying_asset = st.sidebar.selectbox("Underlying Asset", ['Synthetic Asset A', 'Synthetic Asset B', 'Synthetic Asset C'])
st.sidebar.markdown("Select the underlying asset for the derivative contract.")

option_type = st.sidebar.radio("Option Type", ['Call', 'Put'])
st.sidebar.markdown("Choose the type of option: Call (right to buy) or Put (right to sell).")

strike_price = st.sidebar.number_input("Strike Price", value=100.0, step=1.0)
st.sidebar.markdown("Specify the strike price of the option contract.")

expiration_date = st.sidebar.date_input("Expiration Date", date(2024, 12, 31))
st.sidebar.markdown("Select the expiration date for the option contract.")

st.sidebar.divider()
st.sidebar.header("Risk Factor Adjustment")

volatility = st.sidebar.slider("Volatility (%)", min_value=1.0, max_value=50.0, value=20.0, step=1.0) / 100.0
st.sidebar.markdown("Adjust the volatility of the underlying asset. Higher volatility increases uncertainty.")

interest_rate = st.sidebar.number_input("Interest Rate (%)", value=2.5, step=0.1) / 100.0
st.sidebar.markdown("Enter the risk-free interest rate.")

market_scenarios = st.sidebar.multiselect("Market Scenarios", ['Bull Market', 'Bear Market', 'Stable Market', 'High Volatility'], default=['Stable Market'])
st.sidebar.markdown("Select different market scenarios to assess portfolio risk under various conditions.")

# --- Data Generation and Calculations ---
st.header("Risk Assessment and Visualizations")

# Explanation of Risk Assessment
st.markdown("""
    ### Understanding Derivatives Risk

    Derivatives risk assessment involves evaluating potential losses in a derivative portfolio due to changes in market conditions. 
    Key factors influencing derivative risk include:

    - **Notional Amount**: The total value of the contract, scaling potential gains and losses.
    - **Underlying Asset**: The asset the derivative's value is derived from. Different assets have different risk profiles.
    - **Option Type (Call/Put)**: Determines whether the derivative profits from price increases (Call) or decreases (Put).
    - **Strike Price**: The price at which the option can be exercised. Closer to the current price, the option is more sensitive to price changes.
    - **Expiration Date**: Time until the option expires. Longer timeframes generally increase option value and risk.
    - **Volatility**: Measures the degree of price fluctuation of the underlying asset. Higher volatility increases option value but also risk.
    - **Interest Rate**: Affects the cost of carry and present value calculations for derivatives.
    - **Market Scenarios**: Different economic conditions can significantly impact derivative values.

    Below, we visualize the potential profit and loss (P&L) and risk sensitivity of your synthetic derivative portfolio 
    based on the parameters you've set.
    """)

# Synthetic Data Generation for Visualization
np.random.seed(0) # for reproducibility
asset_prices = np.linspace(strike_price * 0.5, strike_price * 1.5, 100) # Range of asset prices around strike
portfolio_values = []

for price in asset_prices:
    # Simplified Option Payoff Calculation (Illustrative, not Black-Scholes)
    if option_type == 'Call':
        option_payoff = max(0, price - strike_price)
    else: # Put option
        option_payoff = max(0, strike_price - price)

    # Incorporate Volatility and Interest Rate (Simplified impact)
    adjusted_payoff = option_payoff * (1 + volatility) * np.exp(interest_rate) # Example adjustment
    portfolio_value = notional_amount * adjusted_payoff
    portfolio_values.append(portfolio_value)

df_portfolio = pd.DataFrame({'Asset Price': asset_prices, 'Portfolio Value': portfolio_values})


# --- Visualizations ---
st.subheader("Portfolio Value vs. Underlying Asset Price")
st.markdown("This chart shows how the portfolio value changes with the underlying asset price. "
            "It illustrates the potential profit and loss profile of the derivative position.")

fig_line_chart = px.line(df_portfolio, x='Asset Price', y='Portfolio Value',
                         title=f'{option_type} Option Portfolio Value Sensitivity',
                         labels={'Portfolio Value': 'Portfolio Value', 'Asset Price': 'Underlying Asset Price'})
fig_line_chart.add_vline(x=strike_price, line_dash="dash", line_color="red",
                        annotation_text=f"Strike Price: {strike_price}", annotation_position="top right")
fig_line_chart.add_annotation(x=strike_price, y=df_portfolio['Portfolio Value'].max() * 0.9,
                            text="Strike Price Level", showarrow=False, bgcolor="white", bordercolor="black", borderwidth=1, opacity=0.8)

st.plotly_chart(fig_line_chart, use_container_width=True)


# Bar Chart for Market Scenarios (Simplified - illustrative)
st.subheader("Portfolio Risk under Different Market Scenarios")
st.markdown("This bar chart provides a simplified view of how the selected market scenarios might impact the portfolio risk. "
            "Note that this is a qualitative representation for educational purposes.")

scenario_risks = {}
for scenario in market_scenarios:
    if scenario == 'Bull Market':
        scenario_risks[scenario] = 0.2 # Lower risk for call, higher for put (example)
    elif scenario == 'Bear Market':
        scenario_risks[scenario] = 0.3 # Higher risk for call, lower for put (example)
    elif scenario == 'Stable Market':
        scenario_risks[scenario] = 0.1
    elif scenario == 'High Volatility':
        scenario_risks[scenario] = 0.4

df_scenarios = pd.DataFrame(list(scenario_risks.items()), columns=['Market Scenario', 'Risk Level'])

fig_bar_chart = px.bar(df_scenarios, x='Market Scenario', y='Risk Level',
                        title='Risk Level by Market Scenario (Illustrative)',
                        labels={'Risk Level': 'Illustrative Risk Level', 'Market Scenario': 'Market Scenario'},
                        color='Market Scenario') # color to differentiate scenarios
fig_bar_chart.update_layout(showlegend=False) # Hide legend as scenario names are on x-axis

st.plotly_chart(fig_bar_chart, use_container_width=True)

# --- Explanation Section ---
st.subheader("Key Concepts Explained")
st.markdown("""
    - **Option Payoff**: The profit or loss realized when an option is exercised or expires. Call options profit from price increases above the strike price, while put options profit from price decreases below the strike price.
    - **Volatility Impact**: Higher volatility generally increases the value of options because there's a greater chance of the underlying asset's price moving significantly, either profitably or unprofitably. This tool simplifies the impact for visual understanding.
    - **Interest Rate Influence**: Interest rates affect the present value of future payoffs. Higher interest rates can increase the value of call options and decrease the value of put options, but the impact is often complex and depends on various factors.
    - **Market Scenarios and Stress Testing**: Assessing portfolio risk under different market scenarios is crucial for stress testing. It helps understand how the portfolio might perform in extreme or unexpected conditions. This application provides a simplified way to consider these scenarios.

    **Disclaimer**: This tool is for educational purposes only and uses a simplified model for derivative risk assessment. 
    Real-world derivative pricing and risk management are significantly more complex and involve sophisticated models and market data. 
    Consult with financial professionals for actual investment and risk management decisions.
    """)


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
