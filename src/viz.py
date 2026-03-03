"""
Plotting visualisation helpers (Plotly) used across Streamlit pages.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px


def line_prices(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Adj Close line chart for one ticker."""
    d = df[df["Ticker"] == ticker].sort_values("Date")
    fig = px.line(d, x="Date", y="Adj_Close", title=f"{ticker} — Adjusted Close")
    fig.update_layout(yaxis_title="Adjusted Close", xaxis_title="Date")
    return fig


def line_returns(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Daily returns line chart for one ticker (uses return_1d if present)."""
    d = df[df["Ticker"] == ticker].sort_values("Date").copy()
    if "return_1d" not in d.columns:
        d["return_1d"] = d["Adj_Close"].pct_change()
    fig = px.line(d, x="Date", y="return_1d", title=f"{ticker} — Daily Return")
    fig.update_layout(yaxis_title="Return", xaxis_title="Date")
    return fig


def hist_returns(df: pd.DataFrame, ticker: str) -> "px.Figure":
    """Histogram of daily returns for one ticker."""
    d = df[df["Ticker"] == ticker].sort_values("Date").copy()
    if "return_1d" not in d.columns:
        d["return_1d"] = d["Adj_Close"].pct_change()
    fig = px.histogram(d.dropna(), x="return_1d", nbins=60, title=f"{ticker} — Return Distribution")
    fig.update_layout(xaxis_title="Return", yaxis_title="Count")
    return fig
