"""
Home page.

Purpose, audience, and beginner-friendly investing principles.
"""

from __future__ import annotations

import streamlit as st


def render() -> None:
    st.title("🏁 Welcome to StockMetrics")

    st.markdown(
        """
> **“The stock market is a device for transferring money from the
> impatient to the patient.”**
> **— Warren Buffett**
"""
    )

    st.divider()

    st.header("Your beginner-friendly investing dashboard")

    st.write(
        "StockMetrics is designed as a guide for beginner investors who want "
        "to understand the basics of investing without getting "
        "lost in the noise."
    )

    st.image(
        "documentation/dashboard/home_hero.png",
        caption=(
            "StockMetrics helps beginner investors understand risk, "
            "returns, and uncertainty."
        ),
        use_container_width=True,
    )

    st.divider()

    st.header("What is the purpose of StockMetrics and who is it for?")

    st.markdown(
        """
Learning to invest can feel intimidating and overwhelming:
unfamiliar terms, endless strategies, and conflicting advice
often lead to **analysis paralysis**.

**StockMetrics** exists to help beginners start sooner by:
1. explaining what matters in plain English (and omitting the noise),
2. focusing on a small curated set of tickers,
3. comparing simple risk-based portfolio plans,
4. showing forecast-style **scenario ranges** (not promises).

To keep things simple and educational, StockMetrics focuses on a small set
of popular tech stocks and ETF funds, but the core principles apply broadly.
The goal is to build intuition and confidence,
not to provide a one-size-fits-all recommendation.

Ultimately, StockMetrics is designed to be a stepping stone:
you can later customise your portfolio or explore other
companies and sectors, but StockMetrics helps you start sooner
with clarity and confidence.
"""
    )

    st.divider()

    st.header("💡 Core investing principles")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("⏳ Start early")
        st.write(
            "Time is your biggest advantage because compounding needs time."
        )
    with c2:
        st.subheader("🧘 Think long-term")
        st.write("Time in the market often beats timing the market.")
    with c3:
        st.subheader("🧺 Diversify")
        st.write("Spreading exposure can reduce concentration risk.")

    st.divider()

    st.header("Quick glossary")
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### What does it mean to diversify?")
        st.write(
            "Diversifying means spreading your money across different assets, "
            "industries, or regions so that poor performance in one area does "
            "not have such a large impact on your overall portfolio."
        )

        st.markdown("### What is volatility?")
        st.write(
            "Volatility measures how sharply an investment’s price moves up "
            "and down. Higher volatility usually means a bumpier journey."
        )

        st.markdown("### What is drawdown?")
        st.write(
            "Drawdown is the peak-to-trough percentage decline in a trading "
            "account's value, measuring the maximum loss before a new peak "
            "is reached."
        )

        st.markdown("### What is dollar-cost averaging?")
        st.write(
            "Dollar-cost averaging means investing a fixed amount regularly "
            "over time instead of trying to guess the perfect moment to buy."
        )

    with c2:
        st.markdown("### What is an ETF?")
        st.write(
            "An ETF, or exchange-traded fund, is a basket of investments that "
            "can be bought and sold like a stock. ETFs can offer instant "
            "diversification."
        )

        st.markdown("### What are dividends?")
        st.write(
            "Dividends are payments some companies make to shareholders from "
            "their profits. Some funds distribute them, while others reinvest "
            "them automatically."
        )

        st.markdown("### What is a blue-chip stock?")
        st.write(
            "A blue-chip stock usually refers to a large, established company "
            "with a strong reputation and long operating history."
        )

    st.divider()

    st.header("Frequently asked questions")

    with st.expander("What is the S&P 500?"):
        st.write(
            "The S&P 500 is a stock market index tracking 500 of the largest "
            "publicly traded companies in the United States. It is widely "
            "used as a benchmark for the broader US stock market."
        )

    with st.expander("What is FTSE All-World fund?"):
        st.write(
            "The Vanguard FTSE All-World fund gives exposure to a broad range "
            "of companies across developed and emerging markets, making it a "
            "simple example of global diversification."
        )

    with st.expander("What is the Magnificent Seven?"):
        st.write(
            "The Magnificent Seven refers to Alphabet, Amazon, Apple, Meta, "
            "Microsoft, Nvidia, and Tesla. These companies have played a "
            "major role in recent US market growth, but they also represent "
            "a more concentrated type of exposure."
        )

    with st.expander(
        "Why is Tesla featured heavily in the Aggressive plan?"
    ):
        st.write(
            "Tesla is used as an example of a more volatile stock. Its price "
            "history helps illustrate how concentration in one high-profile "
            "company can increase both upside potential and downside risk."
        )

    with st.expander(
        "Why does StockMetrics use scenario ranges instead of one prediction?"
    ):
        st.write(
            "Financial markets are noisy, especially in the short term. "
            "Scenario ranges help communicate uncertainty more responsibly "
            "than a single ‘magic number’ prediction."
        )

    with st.expander("Does StockMetrics recommend a trading platform?"):
        st.write(
            "StockMetrics does not provide personalised financial advice, "
            "but beginners often look for platforms that are simple and "
            "accessible.\n\n"
            "One commonly used platform is Trading 212 (T212), which is known "
            "for features such as commission-free trading, a user-friendly "
            "interface, fractional shares, a wide range of available assets, "
            "interest on uninvested cash, and free ISA accounts in the UK.\n\n"
            "However, this is **not financial advice**. Always do your own "
            "research and choose a platform that suits your needs. "
            "**Capital is at risk.**"
        )

    st.divider()

    st.header("Four risk-based plans")
    st.markdown(
        """
Risk in StockMetrics refers to **how concentrated** a portfolio is.
All plans are equity-based and may experience significant short-term
volatility.
"""
    )

    plans = [
        (
            "Diversified (Low Risk)",
            "100% Vanguard FTSE All-World (Dist) (VWRL.L)",
        ),
        (
            "Targeted (Moderate Risk)",
            "100% Vanguard S&P 500 (Dist) (VUSA.L)",
        ),
        (
            "Concentrated (High Risk)",
            "75% Vanguard S&P 500 (Dist) (VUSA.L) + 25% Magnificent Seven",
        ),
        (
            "Aggressive (Higher Risk)",
            "50% Vanguard S&P 500 (Dist) (VUSA.L) + 25% Magnificent Six + "
            "25% Tesla (TSLA)",
        ),
    ]
    for name, desc in plans:
        st.markdown(f"- **{name}:** {desc}")

    st.divider()

    st.info(
        "Educational use only. StockMetrics is not financial advice. "
        "Forecasts are scenario ranges to illustrate uncertainty."
    )
