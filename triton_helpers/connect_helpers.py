from qcodespp.instrument_drivers.oxford.triton import Triton
from qcodespp.instrument_drivers.oxford.mercuryiPS_serial import MercuryiPS_120
from triton_helpers.qswitch_helpers import connect_qswitches

def connect_all(which):
    """
    Connect to all stationary objects.

    Args:
        which (str): The connector used for the qswitches, either 'inner' or 'outer'.

    Returns:
        tuple: A tuple containing the connected instruments.

    Usage:
        triton, magnet, qs1, qs2 = connect_all('outer')
    """
    triton = Triton(name='triton', address='169.254.100.101', port=33576)
    magnet = MercuryiPS_120(name='magnet', address='com7')
    qs1, qs2 = connect_qswitches(which)

    return triton, magnet, qs1, qs2