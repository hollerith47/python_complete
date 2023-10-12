import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="supprime les fichiers trouves"),
         extension: str = typer.Argument("txt", help="Extension a chercher")):
    """
    affiche les fichiers trouvés avec l'extension données
    Args:
        delete:

    Returns:

    """
    typer.echo(f"recherche des fichiers avec l'extension {extension}.")
    """
    #1 facon de faire 
    if delete:
        confirm = typer.confirm("souhaitez-vous vraiment supprimer les fichiers ?")
        if not confirm:
            typer.echo("On annule l'operation.")
            raise typer.Abort()

    print("Suppression des fichiers.")
    """
    if delete:
        typer.echo("Suppression des fichiers.")

@app.command("search")
def search_py():
    main(delete=False, extension="py")

@app.command("delete")
def delete_py():
    main(delete=True, extension="py")

if __name__ == "__main__":
    # typer.run(main)
    app()