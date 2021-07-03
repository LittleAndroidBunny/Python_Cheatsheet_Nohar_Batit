# This script is part of tutorial number 3 of introduction of computer science for EE students at BGU.
# Topics:
#   - default values for function arguments
#   - keyword vs positional arguments
import math


def snr(signal_power: float, noise_power: float = 1, is_db: bool = True) -> float:
    """The function computes the SNR of a signal

    :param float signal_power: input signal power
    :param float noise_power: noise power, default value of 1
    :param  bool is_db: return value in dB or not, default is dB
    :return: the signal snr
    :rtype: float
    """

    if is_db:
        return 10*math.log(signal_power / noise_power, 10)
    else:
        return signal_power / noise_power


print(snr(200, 10, True))
print(snr(200, 10, False))
print(snr(100, noise_power=5))
print(snr(100, is_db=False, noise_power=2))
# print(snr(is_db=1, 100))  # keyword argument must follow positional ones
# print(snr(noise_power=5)) # must use positional arguments
