# preemptive_debugger

A simple method to interactively preempt a running script to run a debugger

![preemptive_debugger](https://github.com/tylerlum/preemptive_debugger/assets/26510814/347fa015-0174-4e1d-b26f-a55b707ced47)

# Installing

Install:

```
pip install preemptive_debugger
```

# Usage

In one terminal, create a file called `test.py` with the following:

```
import preemptive_debugger

import time

for i in range(10_000):
    print(f"i = {i}")
    time.sleep(0.1)
```

Run this code with:

```
python3 test.py
```

In another terminal, run:

```
kill -SIGUSR1 $(pgrep -f "python3 test.py")
```

This will preempt the running script and start a debugger in the original terminal, which can be used to analyze what is happening. This is very useful when you have a script that is stuck or doing strange things. Without this package, if you want to see what is going on in the script, you would typically need to stop the script, modify the code, and try your best to reproduce the result (or wait a long time to have the issue come back up). With this package, adding just one line (`import preemptive_debugger`), you can easily start a debugger whenever you want to look into what is happening in a python program.

# Notes

I have tried some alternative methods to interactively choose when to start a debugger, but they didn't work well. Some pip packages I have tried:

- `keyboard`: Tried to start a debugger when a keyboard key was pressed, but I got this error which was very inconvenient:

```
ImportError: You must be root to use this library on linux.
```

- `pynput`: Tried to start a debugger when a keyboard key was pressed, but I realized this starts a new thread to run the handler. This does not allow me to properly analyze the state of the program I am interested in.

- `madbg`: Tried attaching to the script with `madbg attach <pid>`, but this only worked for very simple scripts. For any nontrivial script, I got this error:

```
pyinjector.api.LinuxInjectorPermissionError: Injector failed with -8 calling injector_attach: PTRACE_ATTACH error : Operation not permitted
Failed attaching to process due to permission error.
This is most likely due to ptrace scope limitations applied to the kernel for security purposes.
Possible solutions:
 - Rerun as root
 - Temporarily remove ptrace scope limitations usin
`echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`
 - Persistently remove ptrace scope limitations by editing /etc/sysctl.d/10-ptrace.conf
More details can be found here: https://stackoverflow.com/q/19215177/2907819')
```

Running with `sudo`, I got this error:

```
pyinjector.api.InjectorError: Injector failed with -5 calling injector_inject: dlopen failed
```
