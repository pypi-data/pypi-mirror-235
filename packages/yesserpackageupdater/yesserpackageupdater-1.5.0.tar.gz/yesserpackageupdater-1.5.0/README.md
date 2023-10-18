
# PIP Package Updater by yesseruser

This is a simple package updater that updates all outdated packages when run.  
Install by running:

``` sh
python -m pip install yesserpackageupdater
```

in CMD or PowerShell on Windows or

``` sh
python3 -m pip install yesserpackageupdater
```

in Mac/Linux's default terminal.

You can use it by running:  

``` sh
yesserpackageupdater
```

in CMD, PowerShell or your OS' default terminal.

~This package only works on Windows.~  
This package works on any operating system since update 1.1.5

If you're running the package from a python file, please **use a subprocess** instead of importing and calling the `update_packages` function. This is because the package can update itself and it can result in an error because of the code changing.
## What's Changed
* Added logging into a file. by @yesseruser in https://github.com/yesseruser/YesserPackageUpdater/pull/33
* Added --log-debug and --clear-log arguments. by @yesseruser in https://github.com/yesseruser/YesserPackageUpdater/pull/34
* The message shown when yesserpackageupdater is outdated when using the script on Windows now displays correctly. by @yesseruser in https://github.com/yesseruser/YesserPackageUpdater/pull/35

Use `--log-debug` to log debug logs. Use `--clear-log` to clear the log file before logging into it.
The log file can be found at `<package install location (do not copy)>/logs`.
You can find the package install location by running:
```
pip show yesserpackageupdater
``` 
on Windows or
```
pip3 show yesserpackageupdater
```
on Unix-based systems (Linux, Mac, etc.) 
and adding `/yesserpackageupdater` to the value shown next to `Location:`

**Full Changelog**: https://github.com/yesseruser/YesserPackageUpdater/compare/1.4.4...1.5.0
