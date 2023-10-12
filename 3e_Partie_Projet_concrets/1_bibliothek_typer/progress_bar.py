import time
import typer


def main():
    chiffre = range(1000)
    with typer.progressbar(chiffre) as progress:
        for _ in progress:
            time.sleep(0.03)

    typer.secho("fin du script.", fg= typer.colors.BRIGHT_GREEN)


if __name__ =="__main__":
    typer.run(main)