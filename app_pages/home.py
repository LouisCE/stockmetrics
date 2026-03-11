"""
Home page.

Purpose, audience, and beginner-friendly investing principles.
"""

from __future__ import annotations

import streamlit as st


def render() -> None:
    st.title("🏁 Welcome to StockMetrics")
    st.subheader("Clarity for beginner investors in fifteen minutes or less")

    st.markdown(
        """
> *“The stock market is a device for transferring money from the impatient to the patient.”*  
> — Warren Buffett
"""
    )

    st.markdown(
        """
Learning to invest can feel intimidating and overwhelming:
unfamiliar terms, endless strategies, and conflicting advice
often lead to **analysis paralysis**.

**StockMetrics** exists to help beginners start sooner by:
- explaining what matters (and what doesn’t) in plain English,
- focusing on a small curated set of tickers,
- comparing simple risk-based portfolio plans,
- showing forecast-style **scenario ranges** (not promises).
"""
    )

    st.divider()

    st.header("Core investing principles")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### ⏳ Start early")
        st.write("Time is your biggest advantage because compounding needs time.")
    with c2:
        st.markdown("### 🧘 Think long-term")
        st.write("Time in the market often beats timing the market.")
    with c3:
        st.markdown("### 🧺 Diversify")
        st.write("Spreading exposure can reduce concentration risk.")

    st.divider()

    st.header("Four risk-based plans")
    st.markdown(
        """
Risk in StockMetrics refers to **how concentrated** a portfolio is.
All plans are equity-based and may experience significant short-term volatility.
"""
    )

    plans = [
        ("Diversified (Low Risk)", "100% All-World fund (VWRP.L)"),
        ("Targeted (Moderate Risk)", "100% S&P 500 fund (VUAG.L)"),
        ("Concentrated (High Risk)", "75% S&P 500 + 25% Magnificent Seven"),
        ("Aggressive (Higher Risk)", "50% S&P 500 + 25% Magnificent Six + 25% Tesla"),
    ]
    for name, desc in plans:
        st.markdown(f"- **{name}:** {desc}")

    st.divider()

    st.info(
        "Educational use only. StockMetrics is not financial advice. "
        "Forecasts are scenario ranges to illustrate uncertainty."
    )
