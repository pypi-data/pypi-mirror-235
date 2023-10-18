"""Book Value Per Share to Price."""


def book_price(
    common_equity_mr0: float,
    common_shares_outstanding_mr0: float,
    close: float,
    report_curr_to_usd: float,
    quote_curr_to_usd: float,
) -> float:
    r"""Book Value Per Share to Price.

    Notes:
        .. math::

            \begin{align}
            {BookToPrice}_n &= \frac
                {\frac{CommonEquity_n}{CommonSharesOutstanding_n}}
                {Close_n}
            \end{align}

    Args:
        common_equity_mr0 (float): book value of common equity.
        common_shares_outstanding_mr0 (float): shares outstanding.
        close (float): close price.
        quote_curr_to_usd (float): the quote currency to_usd conversion.
        report_curr_to_usd (float): the reporting currency to_usd conversion.

    Returns:
        float: Book Value Per Share to Price.
    """
    bvps = common_equity_mr0 * report_curr_to_usd / common_shares_outstanding_mr0
    close *= quote_curr_to_usd

    result = bvps / close

    return result
