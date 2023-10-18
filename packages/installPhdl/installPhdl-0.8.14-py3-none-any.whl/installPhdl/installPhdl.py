#!/usr/bin/env python3
import os
import sys
import pathlib
import shutil
import subprocess
import tempfile

#import PyInstaller.__main__

def main():
    print("-- Starting installation of PhotoLibDownloader.")
    print("-- This will take a minute or two. Please be patient ...")
    print("----------------------------------------")

    thePlatform = sys.platform
    theLib = pathlib.Path(__file__).parent.resolve()
    theDir = pathlib.Path(tempfile.mkdtemp())

    print("-- Step 1 of 4: Installing preliminary requirements ...")

    subprocess.check_call([sys.executable,
                           "-m", "pip", "install", '--upgrade', '--quiet', 'pip'])
    subprocess.check_call([sys.executable,
                           "-m", "pip", "install", '--upgrade', '--quiet', 'pyinstaller'])

    theWhl = None
    theName = None
    for d in theLib.glob('*.whl'):
        theWhl = str(d.resolve())
        theName = d.name.split('-')[0]
        break

    if theWhl is None: exit(1)
    print("-- Step 2 of 4: Downloading program scripts and dependencies. Please wait ...")

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--target', str(theDir), '--quiet', theWhl])

    theSubDir = theDir / theName
    if thePlatform.startswith("darwin"):
        theIcon = theSubDir / "Paomedia_Small_N_Flat_Cloud_down.icns"
    elif thePlatform.startswith("win32"):
        theIcon = theSubDir / "Paomedia_Small_N_Flat_Cloud_down.ico"
    else:
        theIcon = "???"

    theData = str(theIcon) + ":."

    if not theIcon.exists: exit(1)
    print("-- Step 3 of 4: Compiling PhotoLibDownloader app. This may take a minute ...")

    os.chdir(theDir)
    theCmd = [
            theName + "/main.py",
            "--workpath", str(theDir / "build"),
            "--distpath", str(theDir / "dist"),
            "--paths", str(theDir),
            "--paths", str(theSubDir),
            "--add-data", str(theData),
            "--icon", str(theIcon),
            "--name", theName,
            "--log-level", "ERROR"
    ]
    if thePlatform.startswith("darwin"):
        theCmd += [
            "--onedir",
            "--windowed"
        ]
    elif thePlatform.startswith("win32"):
        theCmd += [
            "--onedir",
            "--hide-console", "hide-early"
        ]
    else:
        pass

    subprocess.check_call([sys.executable, "-m", "PyInstaller",*theCmd])

    theAppTarget = ""
    if thePlatform.startswith("darwin"):
        theAppSource = theDir / "dist" / f"{theName}.app"

        if not theAppSource.exists: exit(1)
        print("-- Step 3 of 4: Moving PhotoLibDownloader to the ~/Applications folder")

        theAppDir = pathlib.Path('~/Applications').expanduser()
        if not theAppDir.exists():
            pathlib.Path.mkdir(theAppDir)

        theAppTarget = theAppDir / f"{theName}.app"

        if theAppSource.exists():
            if theAppTarget.exists():
                shutil.rmtree(theAppTarget)
            shutil.copytree(theAppSource, theAppTarget)

        if theAppTarget.exists():
            subprocess.Popen(['/usr/bin/open', str(theAppDir)])

            theSymlink = (pathlib.Path('~/Desktop/') / theName).expanduser()
            if theSymlink.exists():
                theSymlink.unlink(True)
            theSymlink.symlink_to(theAppTarget)

    elif thePlatform.startswith("win32"):
        theDirSource = (theDir / "dist") / theName
        theExeSource = pathlib.Path(str(theDirSource) + ".exe")

        if theDirSource.exists() or theExeSource.exists():
            print("-- Step 4 of 4: Moving PhotoLibDownloader to its target folder")
        else:
            exit(1)

        theDirTarget = pathlib.Path('~/' + theName).expanduser()
        theAppTarget = theDirTarget / f"{theName}.exe"

        if theDirSource.exists():
            if theDirTarget.exists():
                shutil.rmtree(theDirTarget)
            shutil.copytree(theDirSource, theDirTarget)
        elif theExeSource.exists():
            if not theDirTarget.exists():
                theDirTarget.mkdir()
            shutil.copy(theExeSource, theDirTarget)

        os.startfile(theDirTarget)

        theShortcut = (pathlib.Path('~/Desktop/') / f"{theName}.url").expanduser()
        if theShortcut.exists():
            theShortcut.unlink(True)

        theFileLink = "file:///" + str(theDirTarget).replace("\\","/")
        with open(theShortcut, mode="w", newline="\r\n") as f:
            f.write("[InternetShortcut]\r\nURL=" + theFileLink)

    else:
        pass

    print("----------------------------------------")
    print("-- PhotoDownloader app has been installed and can be found in")
    print("-- " + str(theAppTarget) )
    print("-- There is also an icon on your desktop")
    print("")
    print("-- Installation finished. This window can be closed.")

if __name__ == '__main__':
    main()
