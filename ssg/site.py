from pathlib import Path
import os

class Site:
    """
    Class to generate configuration values 
    and to create root structure of our static site.
    """

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        """
        Create Directory
        """
        self.path = path
        self.directory = f"{self.dest}/{path.relative_to(self.source)}"

        os.mkdir(directory, parents=True, exists_ok=True)
    
    def build(self, path):

        self.path = path
        os.mkdir(self.dest, parents=True, exists_ok=True)

        for path in self.source.rglob("*"):
            if path == directory:
                create_dir(path)

            

