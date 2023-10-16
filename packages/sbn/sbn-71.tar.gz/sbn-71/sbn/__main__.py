# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611,C2801


"runtime"


import os
import readline
import sys
import termios
import time
import threading
import traceback


from .methods import parse
from .handler import Broker, Cfg, Client, Errors, Event, command, scan
from .storage import Storage
from .utility import mods


from . import handler
from . import modules


NAME = __file__.split(os.sep)[-2]


Storage.workdir = os.path.expanduser(f"~/.{NAME}")


PIDFILE = os.path.join(Storage.workdir, "sbn.pid")


waitpid = threading.Event()


def cprint(txt):
    print(txt)
    sys.stdout.flush()


handler.output = cprint


class CLI(Client):

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)
        sys.stdout.flush()


class Console(CLI):

    def dispatch(self, evt):
        parse(evt)
        command(evt)
        evt.wait()

    def poll(self) -> Event:
        return self.event(input("> "))


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    with open('/dev/null', 'r', encoding="utf-8") as sis:
        os.dup2(sis.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as sos:
        os.dup2(sos.fileno(), sys.stdout.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as ses:
        os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)
    with open(PIDFILE, "w") as fd:
        fd.write(str(os.getpid()))


def wrap(func) -> None:
    old = None
    try:
        old = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
    Errors.show()


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    Cfg.mod = ",".join(modules.__dir__())
    if "d" in Cfg.opts:
        daemon()
    if "d" in Cfg.opts or "s" in Cfg.opts:
        scan(modules, Cfg.mod, True)
        while 1:
            time.sleep(1.0)
    elif "c" in Cfg.opts:
        if 'v' in Cfg.opts:
            dtime = time.ctime(time.time()).replace("  ", " ")
            print(f"{NAME.upper()} started at {dtime} {Cfg.opts.upper()} {Cfg.mod.upper()}")
        scan(modules, Cfg.mod, "i" not in Cfg.opts, True)
        csl = Console()
        csl.start()
        csl.forever()
    else:
        cli = CLI()
        scan(modules, Cfg.mod)
        evt = cli.event(Cfg.otxt)
        parse(evt)
        command(evt)
        evt.wait()


def wrapped():
    wrap(main)


if __name__ == "__main__":
    wrapped()
