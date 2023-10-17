"""
-- Urheberrechtshinweis --
* Copyright © Manuel Staufer 2023
* Erstellt am 22.07.2023
*
* Alle Inhalte dieses Quellcodes sind urheberrechtlich geschützt.
* Das Urheberrecht liegt, soweit nicht anders gekennzeichnet,
* bei Manuel Staufer.
*
* Jede Art der Vervielfältigung, Verbreitung, Vermietung, Verleihung,
* öffentlichen Zugänglichmachung oder andere Nutzung
* Bedarf der ausdrücklichen Zustimmung von Manuel Staufer.
*
* Alle Rechte vorbehalten.
"""


# IMPORTS
import json, os, shutil


# CREATE DIRECTORY FUNCTION
def createDirectory(path: str):
    os.mkdir(path)


# DELETE DIRECTORY FUNCTION
def deleteDirectory(path: str):
    shutil.rmtree(path)


# EXISTS DIRECTORY FUNCTION
def existsDirectory(path: str):
    return True if os.path.exists(path) else False


# EXISTS FILE FUNCTION
def existsFile(path: str):
    return True if os.path.isfile(path) else False


# FILECONFIGURATION CLASS
class FileConfiguration:
    """
    Methods
    -------
    setOption(key, value)
        Set Data to Config
    removeOption(key):
        Remove Data from Config
    getOption(key):
        Return Data from Config
    getOptions():
        Return Config

    """


    def __init__(self, path: str):
        """
        Parameters
        ----------
        path : str
            Path from Config

        """
        self.path = path
        self.data = {}
        if os.path.exists(self.path):
            try:
                self.loadFile()
            except FileNotFoundError:
                pass


    def setOption(self, key: str, value):
        """
        Parameters
        ----------
        key : str
            Key
        value : any
            Value

        """
        self.data[key] = value


    def removeOption(self, key: str):
        """
        Parameters
        ----------
        key : str
            Key

        """
        try:
            del self.data[key]
        except KeyError:
            return


    def getOption(self, key: str):
        """
        Parameters
        ----------
        key : str
            Key

        Returns
        -------
        Option -> Data from JSON

        """
        try:
            return self.data[key]
        except KeyError:
            return


    def getOptions(self):
        """
        Returns
        -------
        FileConfiguration -> Data from JSON

        """
        return self.data if self.path.endswith(".json") else False


    def saveFile(self):
        """
        """
        with open(self.path, "w") as outfile:
            json.dump(self.data, outfile)


    def loadFile(self):
        """
        """
        with open(self.path) as outfile:
            self.data = json.load(outfile)