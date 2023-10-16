import datetime as dt

import polars as pl
from openbb_terminal.stocks import stocks_helper as stocks

from humbldata.helpers import MCHelpers, MessageHelpers, openBBHelpers
from humbldata.tools.mandelbrot_channel.helpers import (
    add_rvol,
    cumdev,
    cumdev_range,
    cumdev_std,
    dataset_start,
    detrend,
    log_mean,
    price_range,
    vol_buckets,
)


class MandelbrotChannel:
    """
    A class used to represent the Mandelbrot Channel.

    Attributes
    ----------
    interval : int
        The interval for the Mandelbrot Channel, default is 1440.
    prepost : bool
        A flag indicating whether to include pre and post market data,
        default is False.
    source : str
        The source of the data, default is 'YahooFinance'.
    weekly : bool
        A flag indicating whether to use weekly data, default is False.
    monthly : bool
        A flag indicating whether to use monthly data, default is False.
    verbose : bool
        A flag indicating whether to print verbose messages for openbb
        stocks.load() command, default is False.
    silent : bool
        A flag indicating whether to suppress all print statements,
        default is False.

    """

    def __init__(
        self,
        interval: int = 1440,
        prepost: bool = False,
        source: str = "YahooFinance",
        weekly: bool = False,
        monthly: bool = False,
        verbose: bool = False,
        silent: bool = False,
    ):
        self.interval = interval
        self.prepost = prepost
        self.source = source
        self.weekly = weekly
        self.monthly = monthly
        self.verbose = verbose
        self.silent = silent

    def calc_mc(
        self,
        symbol: str,
        fromdate: str | dt.datetime = "1950-01-01",
        todate: str | None = None,
        range: str = "1m",  # the window range used in rescaled_range calculation
        RS_method: str = "RS",  # only used if fast is False
        fast: bool = True,  # uses price from first stock data collection vs grabbing the most recent price
        silent: bool = True,
        rvol_factor: bool = True,  # used to select statistics from similar rvol buckets
        **kwargs,  # rvol_method, window, rv_mean for calculate_rvol(), lo_quantile and hi_quantile for vol_buckets() if rvol_factor is True
    ):
        # Step 1: Collect Price Data -------------------------------------------
        # Collect todate
        if todate is None:
            todate = dt.datetime.today().strftime("%Y-%m-%d")
        # Calculate the start date
        fromdate = dataset_start(
            range=range, fromdate=fromdate, todate=todate, return_dt=False
        )
        # Collect Price
        price_df = stocks.load(
            symbol=symbol,
            start_date=fromdate,
            end_date=todate,
            interval=self.interval,
            prepost=self.prepost,
            source=self.source,
            weekly=self.weekly,
            monthly=self.monthly,
            verbose=self.verbose,
        )[["Adj Close", "Open", "High", "Low"]]
        price_df = pl.from_pandas(price_df, include_index=True).lazy()

        # Step 2: Calculate Log Returns + Rvol ---------------------------------
        price_df = MCHelpers.log_returns(df=price_df)

        # if rvol_factor:
        #     rvol = VolatilityEstimators(clean=True, silent=True)

        #     rvol_method = kwargs.get("rvol_method", "std")
        #     window = kwargs.get("window", 30)

        #     price_df = rvol.calculate_rvol(
        #         price_data=price_df,
        #         rvol_method=rvol_method,
        #         window=window,
        #         rv_mean=rv_mean,
        #     )

        # Step 3: Calculate Log Mean Series ------------------------------------
        log_mean_df = log_mean(df=price_df, range=range)

        # Step 4: Calculate Mean De-trended Series -----------------------------
        # Creates a merged dataframe with price_df data, and detrended mean
        out_df = detrend(df=price_df, mean_df=log_mean_df)

        # Step 5: Calculate Cumulative Deviate Series --------------------------
        out_df = cumdev(df=out_df)

        # Step 6: Calculate Mandelbrot Range -----------------------------------
        out_df = cumdev_range(df=out_df)

        # Step 7: Calculate Standard Deviation ---------------------------------
        out_df = cumdev_std(df=out_df)

        # Step 8: Calculate Range (R) & Standard Deviation (S) -----------------
        if rvol_factor:
            # Step 8.1: Calculate Realized Volatility --------------------------
            out_df = add_rvol(df=out_df, **kwargs)

            # Step 8.2: Return Volatility Bucket Stats (calculate vol buckets) -
            vol_stats = vol_buckets(
                df=out_df, lo_quantile=0.3, hi_quantile=0.65
            )

            # Step 8.3: Extract R & S ------------------------------------------
            R = vol_stats.select(pl.col("R")).collect().to_series()
            S = vol_stats.select(pl.col("S")).collect().to_series()
        else:
            # Step 8.1: Extract R & S ------------------------------------------
            R = out_df.select(pl.col("R")).collect().to_series()
            S = out_df.select(pl.col("S")).collect().to_series()

        RS = pl.Series("RS", R / S)
        RS_mean = RS.mean()  # noqa: F841
        RS_min = RS.min()  # noqa: F841
        RS_max = RS.max()  # noqa: F841

        # Step 10: Calculate Rescaled Price Range ------------------------------
        if fast:
            recent_price = (
                out_df.select(pl.col("Adj Close")).last().collect().rows()[0][0]
            )
        else:
            recent_price = openBBHelpers.recent_price(symbol)  # noqa: F841

        # Step 10.1: Extract Cumulative Deviate Max/Min Columns
        if rvol_factor:
            cumdev_max = (
                vol_stats.select(pl.col("cumdev_max")).collect().to_series()
            )
            cumdev_min = (
                vol_stats.select(pl.col("cumdev_min")).collect().to_series()
            )
        else:
            cumdev_max = (
                out_df.select(pl.col("cumdev_max")).collect().to_series()
            )
            cumdev_min = (
                out_df.select(pl.col("cumdev_min")).collect().to_series()
            )

        self.top_price, self.bottom_price = price_range(
            df=out_df,
            fast=fast,
            RS=RS,
            RS_mean=RS_mean,
            RS_max=RS_max,
            RS_min=RS_min,
            recent_price=recent_price,
            cumdev_max=cumdev_max,
            cumdev_min=cumdev_min,
            RS_method=RS_method,
            rvol_factor=rvol_factor,
        )

        if not fast and not silent:
            # Create the message
            MessageHelpers.log_message(
                f"'[deep_sky_blue1]{range}[/deep_sky_blue1]' Mandelbrot Channel:\n Symbol: [green]{symbol}[/green] \n Date: [green]{dt.datetime.now()}[/green] \n Bottom Range: [green]{self.bottom_price}[/green] -- Last Price: [green]{recent_price}[/green] -- Top Range: [green]{self.top_price}[/green]",
                "success",
            )

        return self
