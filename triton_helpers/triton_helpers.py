def high_temp_mode(parameter,swap_temp=1.25):
    '''
    Switch cryostat to a state safe for temperatures above approx. 1.25 K during a loop.

    Args:
        parameter (Parameter): the parameter to use for comparison. 
            Should be triton.MC, triton.T8, triton.T5 or triton.pid_setpoint
        swap_temp (float): The setpoint temperature in K at which to switch to high temperature mode.
    Usage:
        station.set_measurement(qc.Task(high_temp_mode,triton,1.26))
    '''
    triton=parameter.instrument
    if parameter()>=swap_temp and triton.ask('READ:DEV:TURB1:PUMP:SIG:STATE').endswith('ON'):
        high_temp_mode_now(triton)

def high_temp_mode_now(triton):
    '''
    Switch cryostat to a safe state for high temperatures now.

    Args:
        triton (Instrument): the triton instance.
    '''
    triton.write('SET:DEV:V9:VALV:SIG:STATE:CLOSE')
    triton.write('SET:DEV:V4:VALV:SIG:STATE:OPEN')
    triton.write('SET:DEV:TURB1:PUMP:SIG:STATE:OFF')