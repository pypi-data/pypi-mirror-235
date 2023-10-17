### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /crypto
    /econometrics
    /economy
    /fixedincome
    /forex
    /futures
    /news
    /qa
    /stocks
    /ta

Extensions:
    - crypto@0.1.0a2
    - econometrics@0.1.0a2
    - economy@0.1.0a2
    - fixedincome@0.1.0a2
    - forex@0.1.0a2
    - futures@0.1.0a2
    - news@0.1.0a2
    - openbb_charting@0.1.0a2
    - qa@0.1.0a2
    - stocks@0.1.0a2
    - ta@0.1.0a2

    - alpha_vantage@0.1.0a2
    - benzinga@0.1.0a2
    - cboe@0.1.0a2
    - fmp@0.1.0a2
    - fred@0.1.0a2
    - intrinio@0.1.0a2
    - polygon@0.1.0a2
    - quandl@0.1.0a2
    - yfinance@0.1.0a2    """
    # fmt: on
    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def crypto(self):  # route = "/crypto"
        from . import crypto

        return crypto.ROUTER_crypto(command_runner=self._command_runner)

    @property
    def econometrics(self):  # route = "/econometrics"
        from . import econometrics

        return econometrics.ROUTER_econometrics(command_runner=self._command_runner)

    @property
    def economy(self):  # route = "/economy"
        from . import economy

        return economy.ROUTER_economy(command_runner=self._command_runner)

    @property
    def fixedincome(self):  # route = "/fixedincome"
        from . import fixedincome

        return fixedincome.ROUTER_fixedincome(command_runner=self._command_runner)

    @property
    def forex(self):  # route = "/forex"
        from . import forex

        return forex.ROUTER_forex(command_runner=self._command_runner)

    @property
    def futures(self):  # route = "/futures"
        from . import futures

        return futures.ROUTER_futures(command_runner=self._command_runner)

    @property
    def news(self):  # route = "/news"
        from . import news

        return news.ROUTER_news(command_runner=self._command_runner)

    @property
    def qa(self):  # route = "/qa"
        from . import qa

        return qa.ROUTER_qa(command_runner=self._command_runner)

    @property
    def stocks(self):  # route = "/stocks"
        from . import stocks

        return stocks.ROUTER_stocks(command_runner=self._command_runner)

    @property
    def ta(self):  # route = "/ta"
        from . import ta

        return ta.ROUTER_ta(command_runner=self._command_runner)
