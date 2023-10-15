from rich.progress import BarColumn, SpinnerColumn, TimeElapsedColumn


VERSION = (0, 1, 0, 'd', 2)


class MSG:
    ERROR = "[red][ERROR][/red] "
    CRITICAL = "[red][CRITICAL][/red] "
    INFO = "[green][INFO][/green] "
    DEBUG = "[blue][DEBUG][/blue] "
    WARNING = "[yellow][WARNING][/yellow] "


class COLOR:
    console = 'dodger_blue3'
    error = 'red'
    panel = 'yellow' 
    
class FMODE:
    READ = 'r'
    READ_BINARY = 'rb'
    WRITE = 'w'
    WRITE_BINARY = 'wb'
    APPEND = 'a'

class EXIT:
    SUCCESS = 0
    NO_INPUT = 1
    MULTIPLE_INPUT = 2
    NO_CONFIGURATION_FILE = 3


progrSet = [SpinnerColumn(finished_text=':thumbs_up-emoji:'),
            "[progress.description]{task.description}",
            BarColumn(finished_style='green'),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "{task.completed:>6d} of {task.total:6d}",
            TimeElapsedColumn()
            ]

progEpilog="- For any information or suggestion please contact " \
    "[bold magenta]Romolo.Politi@inaf.it[/bold magenta]"

CONTEXT_SETTINGS=dict(help_option_names=['-h','--help'])