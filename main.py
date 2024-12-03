import typer
from typing import Optional
from pathlib import Path


app = typer.Typer()

@app.command("run")
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher"),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    """Affiche les fichiers trouvés avec l'extension donnée.

    Args:
        extension (str): Extension que l'on recherche sans le [.] (ex: py)
        directory (Optional[str], optional): Dossier dans lequel rechercher les fichiers.
        delete (bool, optional): --delete ((True) Supprime les fichiers trouvés) | --no-delete ((False) Ne supprime pas les fichiers trouvés) [default: False]
    """
    
    if directory:
        directory = Path(directory) # type: ignore
    else:
        directory = Path.cwd() # type: ignore
    
    if not directory.exists(): # type: ignore
        typer.secho(f"Le dossier '{directory}' n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit()
    
    files = directory.rglob(f"*.{extension}") # type: ignore
    if delete:
        typer.confirm("Vouvez-vous vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}.", fg=typer.colors.RED)
    else:
        typer.secho(f"Fichier trouvés avec l'extension {extension}:", bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_WHITE)
        for file in files:
            typer.echo(file)

@app.command()
def search(extension: str):
    main(extension=extension, directory=None, delete=False)

@app.command()
def delete(extension: str):
    main(extension=extension, directory=None, delete=True)

if __name__ == "__main__":
    app()