import asyncio
import datetime as dt

import polars as pl

from humbldata.helpers import MCHelpers, MessageHelpers, openBBHelpers
from humbldata.tools.mandelbrot_channel.helpers import (
    add_rvol,
    collect_price_data,
    cumdev,
    cumdev_range,
    cumdev_std,
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
        live_price: bool = True,  # uses price from first stock data collection vs grabbing the most recent price
        rvol_factor: bool = True,  # used to select statistics from similar rvol buckets
        df: pl.LazyFrame
        | None = None,  # used to pass in a dataframe instead of collecting dat, useful in histocial_mc()
        **kwargs,  # rvol_method, window, rv_mean for calculate_rvol(), lo_quantile and hi_quantile for vol_buckets() if rvol_factor is True
    ):
        # Store the settings for later use
        self.symbol = symbol
        self.range = range
        self.fromdate = fromdate
        self.todate = todate
        self.live_price = live_price
        self.RS_method = RS_method
        self.rvol_factor = rvol_factor

        # Step 1: Collect Price Data -------------------------------------------
        price_df = collect_price_data(self, df=df)

        # Step 2: Calculate Log Returns + Rvol ---------------------------------
        price_df = MCHelpers.log_returns(df=price_df)

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
        if live_price:
            recent_price = openBBHelpers.recent_price(symbol)  # noqa: F841
        else:
            recent_price = round(
                out_df.select(pl.col("Adj Close"))
                .last()
                .collect()
                .rows()[0][0],
                4,
            )

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

        if not self.silent:
            # Create the message
            mc_date = (
                out_df.tail(1).select("date").collect().to_series()[0].date()
            )

            MessageHelpers.log_message(
                f"'[deep_sky_blue1]{range}[/deep_sky_blue1]' Mandelbrot Channel:\n Symbol: [green]{symbol}[/green] \n Date: [green]{mc_date}[/green] \n Bottom Range: [green]{self.bottom_price}[/green] -- Last Price: [green]{recent_price}[/green] -- Top Range: [green]{self.top_price}[/green]",
                "success",
            )

        return self

    async def calc_mc_async(self, df, **kwargs):
        self.calc_mc(
            symbol=self.symbol,
            fromdate=self.fromdate,
            todate=self.todate,
            range=self.range,
            RS_method=self.RS_method,
            live_price=self.live_price,
            rvol_factor=self.rvol_factor,
            df=df,
            **kwargs,
        )
        close_price = (
            df.select(pl.col("Adj Close")).last().collect().to_series()[0]
        )
        return close_price, self.top_price, self.bottom_price

    async def historical_mc(
        self,
        symbol: str,
        fromdate: str | dt.datetime = "1950-01-01",
        todate: str | None = None,
        range: str = "1m",  # the window range used in rescaled_range calculation
        RS_method: str = "RS",  # only used if fast is False
        live_price: bool = True,  # uses price from first stock data collection vs grabbing the most recent price
        rvol_factor: bool = True,  # used to select statistics from similar rvol buckets
        df: pl.LazyFrame
        | None = None,  # used to pass in a dataframe instead of collecting dat, useful in histocial_mc()
        **kwargs,  # rvol_method, window, rv_mean for calculate_rvol(), lo_quantile and hi_quantile for vol_buckets() if rvol_factor is True
    ):
        # Store the settings for later use in historical()
        self.symbol = symbol
        self.range = range
        self.fromdate = fromdate
        self.todate = todate
        self.live_price = live_price
        self.RS_method = RS_method
        self.rvol_factor = rvol_factor

        # Generate a list of dates between fromdate and todate
        start = dt.datetime.strptime(self.fromdate, "%Y-%m-%d").date()
        end = dt.datetime.strptime(self.todate, "%Y-%m-%d").date()
        dates = pl.date_range(start=start, end=end, eager=True, name="date")
        # Step 1: Collect Price Data -------------------------------------------
        price_df = collect_price_data(self, df=df)

        # Step 2: Create a list of tasks ---------------------------------------
        tasks = [
            asyncio.create_task(
                self.calc_mc_async(
                    df=price_df.filter(pl.col("date") <= date), **kwargs
                )
            )
            for date in dates
        ]
        # Gather the results of all tasks
        results = await asyncio.gather(*tasks)
        # Convert the results to a Polars DataFrame
        out_df = pl.DataFrame(
            {
                "date": dates,
                "bottom_price": [result[2] for result in results],
                "close_price": [result[0] for result in results],
                "top_price": [result[1] for result in results],
            }
        )
        return out_df
