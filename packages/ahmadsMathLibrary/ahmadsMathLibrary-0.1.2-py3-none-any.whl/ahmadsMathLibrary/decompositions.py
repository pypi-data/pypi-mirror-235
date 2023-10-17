
def fft(y):
    N = len(y)
    if N == 1:
        y_hat = y
        return y_hat
    elif N&(N-1):
        raise ValueError('N is not a power of 2')
    else:
        evens = y[::2]
        odds = y[1::2]
        DFT = np.zeros(N//2, dtype=complex)
        for k in range(N//2):
            DFT[k] = np.exp(-2*np.pi*1j*(k)/N)
        u = fft(evens)
        v = DFT * fft(odds)
        y_hat = np.concatenate((u+v, u-v))
        return y_hat