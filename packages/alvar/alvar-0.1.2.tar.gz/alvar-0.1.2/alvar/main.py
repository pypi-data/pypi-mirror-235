from typing import Tuple, List

import numpy as np


def allan_variance(
    data: np.ndarray,
    f: float,
    max_clusters: int = 100
) -> Tuple[np.ndarray, np.ndarray]:
    """
    :param data: Array of samples
    :type data: np.ndarray
    :param f: Measure frequency in Hz
    :type f: float
    :param max_clusters: Max number of computing clusters
    :type max_clusters: int
    :return: Tuple of taus and allan variance
    """
    tau0 = 1 / f  # sample period [s]
    data_integral = np.cumsum(data) * tau0
    n = len(data_integral)  # number of sample data
    m_max = 2 ** np.floor(np.log2(n / 2))
    m = np.logspace(np.log10(1), np.log10(m_max), num=max_clusters)
    m = np.ceil(m)
    m = np.unique(m)
    m = m.astype(int)
    tau = m * tau0  # cluster duration

    # Compute allan variance
    allan_var = np.zeros(len(m))
    for i, mi in enumerate(m):
        allan_var[i] = np.sum(
            (data_integral[2 * mi: n] - 2 * data_integral[mi: n - mi] + data_integral[0: n - 2 * mi]) ** 2
        )
    allan_var /= (2 * tau ** 2) * (n - 2 * m)
    return tau, allan_var


def db_to_absolute(data: List) -> np.ndarray:
    """
    :param data: Data in dBm
    :return: converted dBm to absolute dimension
    """
    return 0.001 * 10 ** (np.array(data)/10)
