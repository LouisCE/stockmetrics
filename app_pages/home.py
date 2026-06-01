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

    st.header("📊 Dataset summary")

    st.write(
        "StockMetrics uses historical daily price data collected from "
        "Yahoo Finance for two ETFs and the Magnificent Seven technology "
        "companies: Apple, Amazon, Alphabet, Meta, Microsoft, Nvidia, "
        "and Tesla."
    )

    st.write(
        "The current dashboard uses the v2 dataset, which includes "
        "VWRL.L, VUSA.L, AAPL, AMZN, GOOGL, META, MSFT, NVDA, and TSLA. "
        "The analysis is based mainly on adjusted closing prices, daily "
        "returns, volatility, drawdowns, portfolio metrics, and engineered "
        "features for machine learning."
    )

    st.divider()

    st.header("✅ Project validation summary")

    st.markdown(
        """
StockMetrics was built around **five business requirements** and
**four project hypotheses**. These were validated through dashboard
features, exploratory data analysis, portfolio metrics, scenario forecasting,
and machine learning evaluation.
"""
    )

    st.subheader("Business requirements")

    st.markdown(
        """
1. **Historical Market Exploration** — implemented in the Stock Explorer
   page using price charts, daily returns, and return distributions.
2. **Portfolio Risk Comparison** — implemented in the Portfolio Plans page
   using risk-based plans, volatility, returns, and drawdowns.
3. **Predictive Analytics Feature** — implemented through a supervised
   regression model that estimates next-day return.
4. **Scenario-Based Forecasting** — implemented in the Predictor page using
   long-term optimistic, realistic, and pessimistic scenario ranges.
5. **Clear Communication of ML Results** — implemented in the Model
   Performance page using metrics, plots, and feature importance.
"""
    )

    st.subheader("Project hypotheses")

    st.markdown(
        """
1. **Concentrated portfolio plans are riskier than diversified ones but may
   offer greater potential rewards** — validated using portfolio returns,
   volatility, drawdowns, and growth-of-£1 comparisons.
2. **Technology stocks exhibit higher volatility than diversified ETFs** —
   validated using daily return distributions, boxplots, and rolling
   volatility.
3. **Diversified portfolios experience smaller drawdowns than concentrated
   portfolios** — validated using portfolio drawdown and volatility metrics.
4. **Short-horizon return prediction is inherently difficult** — validated
   using Test R², MAE, RMSE, actual-vs-predicted plots, and residual
   analysis.
"""
    )

    st.info(
        "For full business requirement validation, hypothesis validation, "
        "CRISP-DM mapping, and technical project details, see the "
        "[StockMetrics README file]"
        "(https://github.com/LouisCE/stockmetrics/blob/main/README.md).",
        icon="📘",
    )

    st.divider()

    st.header("💡 Core investing principles")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("⏳ Start early")
        st.write(
            "Time is your biggest asset because compounding needs time."
        )
    with c2:
        st.subheader("🧺 Diversify")
        st.write("Spreading exposure can reduce concentration risk.")
    with c3:
        st.subheader("🧘 Think long-term")
        st.write("Time in the market often beats timing the market.")

    st.divider()

    st.header("📚 Quick glossary")
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("🧺 What does it mean to diversify?")
        st.write(
            "Diversifying means spreading your money across different assets, "
            "industries, or regions so that poor performance in one area does "
            "not have such a large impact on your overall portfolio."
        )

        st.subheader("🎢 What is volatility?")
        st.write(
            "Volatility measures how sharply an investment’s price moves up "
            "and down. Higher volatility usually means a bumpier journey."
        )

        st.subheader("💸 What are dividends?")
        st.write(
            "Dividends are payments some companies make to shareholders from "
            "their profits. Some funds distribute them, while others reinvest "
            "them automatically. Broad ETFs such as S&P 500 and All-World "
            "funds often provide exposure to dividend-paying companies."
        )

        st.subheader("💎 What is a blue-chip stock?")
        st.write(
            "A blue-chip stock usually refers to a large, established company "
            "with a strong reputation and long operating history."
        )

    with c2:
        st.subheader("🧲 What is concentration?")
        st.write(
            "Concentration refers to how much of your portfolio is invested "
            "in a single asset or a small group of assets. Higher "
            "concentration can lead to higher potential returns but also "
            "higher risk."
        )

        st.subheader("📉 What is drawdown?")
        st.write(
            "Drawdown is the peak-to-trough percentage decline in a trading "
            "account's value, measuring the maximum loss before a new peak "
            "is reached."
        )

        st.subheader("📅 What is dollar-cost averaging?")
        st.write(
            "Dollar-cost averaging means investing a fixed amount regularly "
            "over time instead of trying to guess the perfect moment to buy."
        )

        st.subheader("📁 What is an ETF?")
        st.write(
            "An ETF, or exchange-traded fund, is a basket of investments that "
            "can be bought and sold like a stock. ETFs can offer instant "
            "diversification."
        )

    st.divider()

    st.header("❓ Frequently asked questions")

    with st.expander("🤔 Why should I invest at all?"):
        st.write(
            "While keeping cash in a bank account feels safe, "
            "**inflation is a 'silent tax'** "
            "that eats away at your buying power over time. "
            "Investing turns your money into "
            "a tool that works for you while you sleep, "
            "giving you the best chance to "
            "outpace rising costs and build long-term wealth."
        )
        st.info(
            "**Did you know?** Historically, the stock market "
            "has often been cited as returning around 10% per year "
            "before inflation over the long term.",
            icon="ℹ️"
        )

    with st.expander("🧭 When should I buy and sell?"):
        st.write(
            "For most people, the 'perfect time' to buy doesn't exist. "
            "Instead, **starting as soon as you can** is usually better "
            "because it gives your money more time to grow. Investing a "
            "set amount every month (called dollar-cost averaging) is a "
            "great way to smooth out the 'bumps' of the market without the "
            "stress of guessing when to buy."
        )
        st.write(
            "Selling is personal. You might sell when you've reached a "
            "specific savings goal (like a house deposit) or if your life "
            "plans change. The secret is to **stick to your plan** and avoid "
            "making quick decisions just because the market had a bad day."
        )
        st.info(
            "**Golden Rule:** Time *in* the market is almost always "
            "better than trying to *time* the market.",
            icon="⏳"
        )

    with st.expander(
        "💰 How much and how often should I invest?"
    ):
        st.write(
            "The right amount and frequency of investing depends on your "
            "personal financial situation, goals, and risk tolerance. \n\n"
            "A common benchmark is to invest 10% to 20% of your take-home pay "
            "monthly, with 15% often cited as an ideal target for long-term "
            "retirement. This is a strategy called dollar-cost averaging, "
            "which can help reduce the impact of market volatility and avoid "
            "trying to time the market. However, the best approach for you "
            "may differ."
        )

    with st.expander("🇺🇸 What is the S&P 500?"):
        st.write(
            "The S&P 500 is a stock market index tracking 500 of the largest "
            "publicly traded companies in the United States, representing "
            "about 80% of the US stock market by capitalization. It is widely "
            "used as a gold standard for measuring the overall performance of "
            "the US stock market and a benchmark for portfolio success.\n\n"
            "This is a popular choice as it provides easy diversification "
            "without much cognitive load for beginners.\n\n"
            "Some beginners choose simple index-based strategies because they "
            "reduce decision fatigue and provide broad market exposure."
        )

    with st.expander("🌍 What is the FTSE All-World fund?"):
        st.write(
            "The Vanguard FTSE All-World fund gives exposure to a broad range "
            "of companies across developed and emerging markets, making it a "
            "simple example of global diversification. Choosing this option "
            "means betting that the world economy will continue to grow over "
            "time.\n\n"
            "This option is even more diversified than the S&P 500, but it "
            "tends to have slightly lower returns because it includes more "
            "exposure to slower, more mature markets."
        )

    with st.expander("⚜️ What is the Magnificent Seven?"):
        st.write(
            "The Magnificent Seven refers to Alphabet, Amazon, Apple, Meta, "
            "Microsoft, Nvidia, and Tesla. These companies have played a "
            "major role in recent US market growth, but they also represent "
            "a more concentrated type of exposure.\n\n"
            "Because these seven companies make up nearly 40% of the S&P 500 "
            "by value, the index's performance is often heavily driven by "
            "just this small group of tech giants.\n\n"
            "To keep things simple, StockMetrics doesn't expand beyond these "
            "seven as individual stocks. The diversification principle is "
            "covered by the S&P 500 and All-World funds while the "
            "concentration principle is illustrated by the Magnificent Seven."
        )

    with st.expander(
        "🏎️ Why is Tesla featured heavily in the Aggressive plan?"
    ):
        st.write(
            "Tesla is used as an example of a more volatile stock. Its price "
            "history helps illustrate how concentration in one high-profile "
            "company can increase both upside potential and downside risk."
        )

    with st.expander(
        "🎭 Why does StockMetrics use scenario ranges instead of one "
        "prediction?"
    ):
        st.write(
            "Financial markets are noisy, especially in the short term. "
            "Scenario ranges help communicate uncertainty more responsibly "
            "than a single ‘magic number’ prediction."
        )

    with st.expander("📱 Does StockMetrics recommend a trading platform?"):
        st.write(
            "StockMetrics does not provide personalised financial advice, "
            "but beginners often look for platforms that are simple and "
            "accessible.\n\n"
            "One commonly used platform is Trading 212 (T212), which is known "
            "for features such as commission-free trading, a user-friendly "
            "interface, fractional shares, a wide range of available assets, "
            "interest on uninvested cash, free ISA accounts in the UK, and "
            "multi-currency investing.\n\n"
            "Trading 212 supports holding multiple currency balances, "
            "including USD, EUR, and GBP. This can help users buy assets in "
            "their native currency, such as buying US stocks with a USD "
            "balance, instead of converting currency for every trade. If "
            "currency is converted in-app, Trading 212 states that its "
            "standard FX fee is 0.15%.\n\n"
            "However, this is **not financial advice**. Always do your own "
            "research and choose a platform that suits your needs."
        )

    with st.expander("🧱 Are there any other assets I can explore?"):
        st.write(
            "Yes, there are many other stocks and ETFs you can explore "
            "beyond the ones featured in StockMetrics. StockMetrics is "
            "designed to be a starting point to build your confidence and "
            "understanding of investing. Once you feel comfortable, you "
            "can research and invest in other companies or funds that "
            "align with your interests. \n\n"
            "Popular assets include Netflix, Walmart, JPMorgan Chase & Co., "
            "Johnson & Johnson, Coca-Cola, PepsiCo, McDonald's, "
            "and Realty Income, as well as physical silver and gold beyond "
            "traditional stocks. \n\n"
            "Always remember to do your own research and consider your risk "
            "tolerance before investing in any asset. "
        )

    st.divider()

    st.header("🧩 Preview of the four risk-based plans")
    st.markdown(
        """
StockMetrics is built around the idea of taking sensible risks.

Each plan below shows a different level of **concentration risk**.

Higher concentration can increase both potential returns and potential
losses. These examples help illustrate how portfolio structure affects
risk and reward.

See the Portfolio Plans page for a more detailed comparison of how
these plans would have performed historically and the trade-offs between
diversification, concentration, and volatility.
"""
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info(
            "🛡️ **Diversified (Low Risk)**\n\n"
            "Global diversification across developed and emerging markets."
        )

    with col2:
        st.success(
            "🎯 **Targeted (Moderate Risk)**\n\n"
            "Focused exposure to large US companies in the S&P 500 "
            "for balance."
        )

    with col3:
        st.warning(
            "🧗 **Concentrated (High Risk)**\n\n"
            "Mix of S&P 500 and Magnificent Seven for higher growth "
            "potential."
        )

    with col4:
        st.error(
            "🌋 **Aggressive (Higher Risk)**\n\n"
            "High concentration with Tesla overweight to illustrate "
            "volatility."
        )
