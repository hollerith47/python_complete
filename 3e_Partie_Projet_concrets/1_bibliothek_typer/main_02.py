import typer

def main():
    prenom = typer.style("Herman", bold =True, fg=typer.colors.BLUE)
    typer.echo(f"Bonjour {prenom}")



if __name__ == "__main__":
    typer.run(main)