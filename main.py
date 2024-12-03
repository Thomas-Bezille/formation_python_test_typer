import typer
from typing import Optional


def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher"),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    """Affiche les fichiers trouvés avec l'extension donnée.

    Args:
        extension (str): Extension que l'on recherche sans le [.] (ex: py)
        directory (Optional[str], optional): Dossier dans lequel rechercher les fichiers.
        delete (bool, optional): --delete ((True) Supprime les fichiers trouvés) | --no-delete ((False) Ne supprime pas les fichiers trouvés) [default: False]
    """
    pass


if __name__ == "__main__":
    typer.run(main)