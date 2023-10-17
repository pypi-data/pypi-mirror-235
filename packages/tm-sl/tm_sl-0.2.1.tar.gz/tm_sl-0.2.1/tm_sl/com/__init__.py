from rich import print, traceback, inspect, print_json
from rich.pretty import pprint
traceback.install(show_locals=False, suppress=['click', 'rich', 'requests', 'urllib3'])
from rich.console import Console
from rich.spinner import Spinner
console = Console()
import json
def c_json(data):
    print_json(json.dumps(data))