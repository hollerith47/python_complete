import typer

# modification du texte

def main():
    if not False:
        prenom = typer.style("Herman", fg= typer.colors.RED)

    else:
        prenom = typer.style("Herman", fg=typer.colors.BLUE)

    typer.echo(f"Bonjour {prenom}")

if __name__ =="__main__":
    typer.run(main)