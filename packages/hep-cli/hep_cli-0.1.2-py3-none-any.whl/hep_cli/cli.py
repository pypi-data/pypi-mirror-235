
from rich.console import Console
from rich.table import Table
console = Console()


from rich import print
from rich.panel import Panel
def main():
    console.print(Panel.fit("Hello, World! I'm a CLI! I'm alive!"))
    table = Table(title="Star Wars Movies")

    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")

    table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
    table.add_row("May 19, 2005", "Star Wars Ep. 111: Revenge of the Sith", "$868,390,560")
    table.add_row("May 16, 2002", "Star Wars Ep. 11: Attack of the Clones", "$653,779,618")

    console.print(table)
    

def run_app():
    main()
    
if __name__ == '__main__':
    main()