import numpy as np
import pandas as pd

class PortfolioStats:

    def __init__(self, prices: pd.DataFrame, log: bool = False, annualization_factor: int = 252) -> None:

        """
        Description:
            Initializes the PortfolioStats class with price data and options for calculations.
        
        Parameters:
            prices (pd.DataFrame): Price data for assets.
            log (bool): Whether to use log returns. Defaults to False.
            annualization_factor (int): Factor for annualizing returns and risk. Defaults to 252.
        """

        self._prices = prices
        self._log = log
        self._annualization_factor = annualization_factor

        if self._log:
            self.returns = np.log(self._prices).diff()[1:]
        else:
            self.returns = self._prices.pct_change()[1:]

        self.info = self._calculate()

    def _calculate(self) -> pd.DataFrame:

        """
        Description:
            Calculates key portfolio statistics for each asset.
        
        Returns:
            pd.DataFrame: Portfolio statistics for each asset.
        """

        info = pd.DataFrame(
            columns=["SHARPE", "CUMU_RET", "ANN_RET", "ANN_VOL", "MAX_DD"], 
            index=[col for col in self.returns]
        )

        for col in self.returns:
            data = self.returns[col]
            
            if not self._log: 
                cumu_ret = self._get_simple_cumu_ret(data)
                max_dd = self._get_simple_dd(data)
            else: 
                cumu_ret = self._get_log_cumu_ret(data)
                max_dd = self._get_log_dd(data)

            info.loc[col] = {
                "SHARPE": self._get_sharpe(data),
                "CUMU_RET": cumu_ret,
                "ANN_RET": self._get_ann_ret(data),
                "ANN_VOL": self._get_ann_risk(data),
                "MAX_DD": max_dd
            }
            
        return info
    
    def _get_ann_ret(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the annualized return for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Annualized return.
        """
        
        return data.mean() * self._annualization_factor

    def _get_ann_risk(self, data: pd.Series) -> float:
        
        """
        Description:
            Calculates the annualized volatility for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Annualized volatility.
        """

        return data.std() * np.sqrt(self._annualization_factor)
    
    def _get_simple_cumu_ret(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the simple cumulative return for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Simple cumulative return.
        """

        return ((1 + data).cumprod() - 1).iloc[-1]
    
    def _get_log_cumu_ret(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the logarithmic cumulative return for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Logarithmic cumulative return.
        """

        return data.cumsum().iloc[-1]
    
    def _get_simple_dd(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the simple maximum drawdown for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Simple maximum drawdown.
        """

        g = (1 + data).cumprod() - 1
        return (g - g.cummax()).min()
    
    def _get_log_dd(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the logarithmic maximum drawdown for a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Logarithmic maximum drawdown.
        """

        g = data.cumsum()
        return (g - g.cummax()).min()
    
    def _get_sharpe(self, data: pd.Series) -> float:

        """
        Description:
            Calculates the Sharpe ratio of a given returns series.
        
        Parameters:
            data (pd.Series): Return data for an asset.
        
        Returns:
            float: Sharpe ratio.
        """

        er = self._get_ann_ret(data)
        vol = self._get_ann_risk(data)

        return er / vol