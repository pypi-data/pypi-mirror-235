# `PortfolioStats`

A python class to compute key portfolio statistics for assets based on their price data.

## Introduction

`PortfolioStats` provides an organized method to calculate and view various portfolio metrics such as the Sharpe Ratio, cumulative returns, annualized returns, annualized volatility, and maximum drawdown.

## Parameters

- **prices** (`pd.DataFrame`): Price data for assets
- **log** (`bool`): Indicator to use logarithmic returns. Default is `False`.
- **annualization_factor** (`int`): Factor to annualize returns and risk. Default is `252` (number of trading days in a year).

## Calculations

### Returns

Using simple returns:
$$r_{t} = \frac{P_{t} - P_{t-1}}{P_{t-1}}$$

Using logarithmic returns:
$$ r_{t} = ln \Bigl(\frac{P_{t}}{P_{t-1}}\Bigl)$$

Where:
- $P_{t}$ is the price of the asset at time $t$

### Sharpe Ratio

$$\frac{E\bigl[r\bigl] \times A}{\sigma{\bigl[r\bigl]} \times \sqrt{A}}$$

Where:
- $E\bigl[r\bigl]$ is the expected return of the asset.
- $\sigma{\bigl[r\bigl]}$ is the standard deviation (risk) of the returns.

### Cumulative Returns

Using simple returns:
$$\text{Cumulative Return} = \prod^T_{i=1}(1+r_{i}) - 1$$

Using logarithmic returns:
$$\text{Cumulative Return} = \sum^T_{i=1} r_{i}$$

### Annualized Return

$$\text{Annualized Return} = E\bigl[r\bigl] \times \text{ }A$$

### Annualized Volatility

$$\text{Annualized Volatility} = \sigma{\bigl[r\bigl]} \times \sqrt{A}$$

### Maximum Drawdown

Using simple returns:
$$ \text{MDD} = \min \left( \frac{\text{CR}_{\text{trough}}}{\text{CR}_{\text{peak}}} - 1 \right) $$

Using logarithmic returns:
$$\text{MDD} = \min \left( \text{CLR} - \text{CLR (max up to now)} \right)$$

Where:
- $\text{CR}$ is the cumulative simple return series.
- $\text{CLR}$ is the cumulative logarithmic return series.

## Usage

Initialize the class with price data and optional parameters. Access the `.info` attribute to view the calculated portfolio statistics.