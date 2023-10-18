import time

from numba import prange, njit, typed
import numpy as np
from typing_extensions import Literal


@njit('(float32[:],)')
def benford_correlation(data: np.ndarray) -> float:
    """
    Jitted compute of the correlation between the Benford's Law distribution and the first-digit distribution of given data.

    Benford's Law describes the expected distribution of leading (first) digits in many real-life datasets. This function
    calculates the correlation between the expected Benford's Law distribution and the actual distribution of the
    first digits in the provided data.

    .. note::
       Adapted from `tsfresh <https://tsfresh.readthedocs.io/en/latest/_modules/tsfresh/feature_extraction/feature_calculators.html#benford_correlation>`_.

    :param np.ndarray data: The input 1D array containing the time series data.
    :param int threshold: The threshold value used for the comparison.
    :return float: The correlation coefficient between the Benford's Law distribution and the first-digit distribution in the
    input data. A higher correlation value suggests that the data follows the expected distribution more closely.

    :examples:
    >>> data = np.array([1, 8, 2, 10, 8, 6, 8, 1, 1, 1]).astype(np.float32)
    >>> benford_correlation(data=data)
    >>> 0.6797500374831786
    """

    data = np.abs(data)
    benford_distribution = np.array([np.log10(1 + 1 / n) for n in range(1, 10)])
    first_vals, digit_ratio = np.full((data.shape[0]), np.nan), np.full((9), np.nan)
    for i in prange(data.shape[0]):
        first_vals[i] = (data[i] // 10 ** (int(np.log10(data[i])) - 1 + 1))

    for i in range(1, 10):
        digit_ratio[i-1] = np.argwhere(first_vals == i).shape[0] / data.shape[0]

    return np.corrcoef(benford_distribution, digit_ratio)[0, 1]












# #
data = np.array([1, 8, 2, 10, 8, 6, 8, 1, 1, 1]).astype(np.float32)
benford(data=data)
# #data = np.random.randint(0, 10, (1000,)).astype(np.float32)
#
# start = time.time()
# for i in range(1):
#     results = time_since_previous(data=data, threshold=7.0, above=False, sample_rate=2.0)
# #print(results)
# print(time.time() - start)
