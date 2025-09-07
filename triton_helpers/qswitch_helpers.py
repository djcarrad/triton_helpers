from qcodespp.instrument_drivers.QDevil.QSwitch import QSwitch, QSwitches

def connect_qswitches(which):
    """
    Connect to the pair of QSwitches corresponding to the inner or outer dsub connector.

    Args:
        which (str): The connector used, either 'inner' or 'outer'.
    Returns:
        tuple: A tuple containing the two QSwitch instances.
    Usage:
        qsws = connect_qswitches('outer')
    """
    if which=='outer':
        qs1=QSwitch('qs1','169.254.100.53')
        qs2=QSwitch('qs2','169.254.100.135')
    elif which=='inner':
        qs1=QSwitch('qs1','169.254.100.141')
        qs2=QSwitch('qs2','169.254.100.143')
    else:
        raise ValueError('which must be either "outer" or "inner"')
    return QSwitches([qs1, qs2])