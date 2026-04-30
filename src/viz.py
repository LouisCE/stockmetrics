"""
Plotting visualisation helpers (Plotly) used across Streamlit pages.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px

from src.config import format_ticker_label


def line_prices(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Price history line chart for one ticker."""
    d = df[df["Ticker"] == ticker].sort_values("Date")
    label = format_ticker_label(ticker)
    currency_symbol = "£" if ticker.endswith(".L") else "$"

    fig = px.line(
        d,
        x="Date",
        y="Adj_Close",
        title=f"{label} — Price history ({currency_symbol})",
    )
    fig.update_layout(
        yaxis_title=f"Price ({currency_symbol})",
        xaxis_title="Date",
    )
    fig.update_xaxes(tickformat="%d/%m/%Y")
    return fig


def line_returns(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Daily returns line chart for one ticker."""
    d = df[df["Ticker"] == ticker].sort_values("Date").copy()
    label = format_ticker_label(ticker)

    if "return_1d" not in d.columns:
        d["return_1d"] = d["Adj_Close"].pct_change()

    fig = px.line(
        d,
        x="Date",
        y="return_1d",
        title=f"{label} — Daily return",
    )
    fig.update_layout(
        yaxis_title="Daily return",
        xaxis_title="Date",
    )
    fig.update_xaxes(tickformat="%d/%m/%Y")
    return fig


def hist_returns(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Histogram of daily returns for one ticker."""
    d = df[df["Ticker"] == ticker].sort_values("Date").copy()
    label = format_ticker_label(ticker)

    if "return_1d" not in d.columns:
        d["return_1d"] = d["Adj_Close"].pct_change()

    fig = px.histogram(
        d.dropna(),
        x="return_1d",
        nbins=60,
        title=f"{label} — Return distribution",
    )
    fig.update_layout(
        xaxis_title="Daily return",
        yaxis_title="Count",
    )
    fig.update_xaxes(tickformat=".2%")
    return fig
