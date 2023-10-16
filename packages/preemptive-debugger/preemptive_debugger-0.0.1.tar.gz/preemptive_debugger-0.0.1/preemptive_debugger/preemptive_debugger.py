import signal


def debugger_handler(sig, frame):
    breakpoint()


signal.signal(signal.SIGUSR1, debugger_handler)
