import cmd
import sys

from race_monitor.client.client import Client
from race_monitor.settings.settings import logger


def run():
    try:
        Client.connect()
    except KeyboardInterrupt:
            pass


class RaceMonitorShell(cmd.Cmd):

    intro = 'Welcome to the RaceMonitor shell. Type help or ? to list commands.\n'
    prompt = '>> '

    def do_q(self, arg):
        'Exit the system'
        exit()

    def do_exit(self, arg):
        'Exit the system'
        exit()

    def do_run(self, arg):
        'Run and receive messages'
        logger.info("Running and monitoring...")
        run()


if __name__ == '__main__':
    #
    # Main Driver
    #

    logger.debug(str(sys.argv))
    args = sys.argv

    if len(args) > 1:
        # Get rid of the script name
        args.pop(0)

        # Get the first arg (run, shell)
        ccc = args[0]

        if ccc == 'run':
            RaceMonitorShell().do_run(None)

        elif ccc == 'shell':
            RaceMonitorShell().cmdloop()
        else:
            # Default
            RaceMonitorShell().cmdloop()

    elif len(args) == 1:
        # Fully interactive mode
        RaceMonitorShell().cmdloop()
