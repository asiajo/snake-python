import cx_Freeze
import os

# creating here the executable file.

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

executables = [cx_Freeze.Executable("Main.py")]

cx_Freeze.setup(name="Snake",
                options={
                    "build_exe": {
                        "packages": ["pygame"],
                        "include_files":  ["Food.py", "Functions.py", "Levels.py", "Screens.py", "Snake.py",
                                           "Variables.py", "media/screens/background_800.png",
                                           "media/heads/head_down.png", "media/heads/head_eat_down.png",
                                           "media/heads/head_down_dead.png", "media/food/mouse.png",
                                           "media/screens/lost.png", "media/screens/welcome.png",
                                           "media/heads/head_down.jpg"],
                    }

                },

                description="Well known snake game with implemented graphic",
                executables=executables

                )
