import numpy as np
from scipy.stats import norm

from utils import dOne, dTwo



def europeanCall(
    stockPrice,
    strikePrice,
    expiration,
    riskFreeRate,
    volatility
):
    dOneVar = dOne(
        stockPrice,
        strikePrice,
        expiration,
        riskFreeRate,
        volatility
    )
    tOne = stockPrice * norm.cdf(dOneVar)
    dTwoVar = dTwo(
        dOneVar,
        expiration,
        volatility
    )
    fvDiscount = np.exp(-riskFreeRate * expiration)
    tTwo = strikePrice * fvDiscount * (norm.cdf(dTwoVar))


    return np.round((tOne - tTwo), decimals=4)


def europeanPut(
    stockPrice,
    strikePrice,
    expiration,
    riskFreeRate,
    volatility
):
    dOneVar = dOne(
        stockPrice,
        strikePrice,
        expiration,
        riskFreeRate,
        volatility
    )
    tOne = stockPrice * norm.cdf((-1 * dOneVar))


    dTwoVar = dTwo(
        dOneVar,
        expiration,
        volatility
    )
    fvDiscount = np.exp(-riskFreeRate * expiration)
    tTwo = strikePrice * fvDiscount * (norm.cdf((-1 * dTwoVar)))


    return np.round((tTwo - tOne), decimals=4)