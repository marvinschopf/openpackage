import pathlib
import cson
import urllib.request
import zipfile
import subprocess
import os
import ssl

class Package:

    data_path = ""
    rawdata_str = ""
    rawdata = {}
    name = "package"
    version = "1.0.0"
    install_type = "command"
    description = "Package"
    install_steps = ["echo test"]


    # Start setters

    def setDataPath(self, data_path):
        self.data_path = data_path

    def setRawdataStr(self, rawdata_str):
        self.rawdata_str = rawdata_str

    def setRawdata(self, rawdata):
        self.rawdata = rawdata

    def setName(self, name):
        self.name = name

    def setVersion(self, version):
        self.version = version

    def setInstallType(self, install_type):
        self.install_type = install_type

    def setDescription(self, description):
        self.description = description

    def setInstallSteps(self, install_steps):
        self.install_steps = install_steps

    # End setters
    # Start getters

    def getDataPath(self):
        return self.data_path

    def getRawdataStr(self):
        return self.rawdata_str

    def getRawdata(self):
        return self.rawdata

    def getName(self):
        return self.name

    def getVersion(self):
        return self.version

    def getInstallType(self):
        return self.install_type

    def getDescription(self):
        return self.description

    def getInstallSteps(self):
        return self.install_steps

    # End getters


    def parseData(self):
        if self.getRawdata() != {}:
            if self.getRawdata()["name"] and self.getRawdata()["name"] != "":
                self.setName(self.getRawdata()["name"])
            if self.getRawdata()["description"] and self.getRawdata()["description"] != "":
                self.setDescription(self.getRawdata()["description"])
            if self.getRawdata()["version"] and str(self.getRawdata()["version"]) != "":
                self.setVersion(str(self.getRawdata()["version"]))
            if self.getRawdata()["install_type"] and self.getRawdata()["install_type"] != "":
                self.setInstallType(self.getRawdata()["install_type"])
            if self.getRawdata()["steps"] and self.getRawdata()["steps"] != []:
                self.setInstallSteps(list(self.getRawdata()["steps"]))

    def loadFromFile(self, file_name, absolute = False):
        self.setDataPath(file_name)
        if not absolute:
            homedir = str(pathlib.Path.home())
            if not homedir[-1:] == "/":
                homedir = homedir + "/"
            homedir = homedir + ".openpackage/packages/"
            self.setDataPath(homedir + file_name)
        with open(self.data_path) as data_file:
            self.setRawdataStr(data_file.read())
            data_file.close()
        self.setRawdata(cson.loads(self.getRawdataStr()))
        self.parseData()

    def installByZip(self, name, log = True):
        if log:
            print("--Installing via zip file(s)")
        for step in self.getInstallSteps():
            url = step
            targetName = name + "-" + url.split("/")[-1]
            targetDirectory = targetName.replace(".zip", "")
            if log:
                print("--Saving", url, "to", targetName)
            if url.startswith("https://"):
                if log:
                    print("--Warning: We are not using any certificate validation!")
                gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                with urllib.request.urlopen(url, context=gcontext) as u, \
                        open(targetName, 'wb') as f:
                    f.write(u.read())
            else:
                urllib.request.urlretrieve(url, targetName)
            if log:
                print("--Extracting", targetName)
            zip_ref = zipfile.ZipFile(targetName, 'r')
            zip_ref.extractall(targetDirectory)
            zip_ref.close()
            if log:
                print("--Done with artefact", targetDirectory)

    def installByCommand(self, log = True):
        if log:
            print("--Installing via command(s)")
            print("--Detected cwd:", os.getcwd())
        for step in self.getInstallSteps():
            command = step
            commandList = command.split(" ")
            if log:
                print("--Executing command:", command)
            process = subprocess.Popen(commandList, cwd = os.getcwd())
            process.wait()
            if log:
                print("--Done executing command:", command)

    def install(self, name, log = True):
        if log:
            print("--Loading packages")
        self.loadFromFile(name + ".cson", absolute = False)
        if self.getInstallType() == "zip":
            self.installByZip(name = name, log = log)
        elif self.getInstallType() == "command":
            self.installByCommand(log = log)
        else:
            print("--Unknown install method:", self.getInstallType())
        print("--Installed", self.getName())
