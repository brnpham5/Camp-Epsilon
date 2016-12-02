from distutils.core import setup
import py2exe
import os


#This is for pygame modules used to play sounds to be included when creating exe
origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll","sdl_ttf.dll"): # "sdl_ttf.dll" added by arit.
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL

#Set up command for exe
#Options puts necessary files into exe rather than folder and compress it
#Console uses GameState file as main for exe. Dest_base is to name exe
#zipfile so that we dont have a zip file with needed libraries.
setup(
    options = {'py2exe':{'bundle_files': 2,"compressed":True}},
    console = [{'script':'GameState.py','dest_base': 'CampEpsilon'}],
    zipfile = None,
    )
