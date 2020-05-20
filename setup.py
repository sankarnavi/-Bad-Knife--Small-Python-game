import cx_Freeze
executables = [cx_Freeze.Executable("demogame.py")]
cx_Freeze.setup(name="A bad Apple",
                options={"build_exe": {"packages": ["pygame"],
                                       "include_files": ["apple.png", "knife.png"]}},
                executables=executables)
