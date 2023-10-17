
"""all
"""
import crocodile.toolbox as tb
from crocodile.core import List
import machineconfig.jobs.python_linux_installers as inst
import machineconfig.jobs.python_generic_installers as gens
import platform
from typing import Optional


def get_cli_py_installers(dev: bool = False):
    path = tb.P(inst.__file__).parent
    gens_path = tb.P(gens.__file__).parent
    if dev:
        path = path.joinpath("dev")
        gens_path = gens_path.joinpath("dev")
    return path.search("*.py", filters=[lambda x: "__init__" not in str(x)]) + gens_path.search("*.py", filters=[lambda x: "__init__" not in str(x)])


def get_installed_cli_apps():
    if platform.system() == "Windows": apps = tb.P.home().joinpath("AppData/Local/Microsoft/WindowsApps").search("*.exe", not_in=["notepad"])
    elif platform.system() == "Linux": apps = tb.P(r"/usr/local/bin").search("*")
    else: raise NotImplementedError("Not implemented for this OS")
    apps = tb.L([app for app in apps if app.size("kb") > 0.1 and not app.is_symlink()])  # no symlinks like paint and wsl and bash
    return apps


def install_logic(py_file: tb.P, version: Optional[str] = None):
    try:
        old_version = tb.Terminal().run(f"{py_file.stem} --version", shell="powershell").op.replace("\n", "")
        tb.Read.py(py_file)["main"](version=version)
        new_version = tb.Terminal().run(f"{py_file.stem} --version", shell="powershell").op.replace("\n", "")
        if old_version == new_version: return f"😑 {py_file.stem}, same version: {old_version}"
        else: return f"🤩 {py_file.stem} updated from {old_version} === to ===> {new_version}"
    except Exception as ex:
        print(ex)
        return f"Failed at {py_file.stem} with {ex}"


def main(installers: Optional[list[tb.P]] = None, safe: bool = False):
    if safe:
        from machineconfig.jobs.python.check_installations import apps_summary_path
        apps_dir = apps_summary_path.readit()
        if platform.system().lower() == "windows":
            apps_dir.search("*").apply(lambda app: app.move(folder=tb.P.get_env().WindowsApps))
        elif platform.system().lower() == "linux":
            tb.Terminal().run(f"sudo mv {apps_dir.as_posix()}/* /usr/local/bin/").print_if_unsuccessful(desc="MOVING executable to /usr/local/bin", strict_err=True, strict_returncode=True)
        else: raise NotImplementedError(f"I don't know this system {platform.system()}")
        apps_dir.delete(sure=True)
        return None

    if not isinstance(installers, list):
        installers_concrete = get_cli_py_installers(dev=False)
    else:
        installers_concrete = List(installers)
        # res = installers_concrete[:4]

    install_logic(installers_concrete.list[0])  # try out the first installer alone cause it will ask for password, so the rest will inherit the sudo session.

    # summarize results
    res: tb.List[str] = installers_concrete.slice(start=1).apply(install_logic, jobs=10)
    from rich.console import Console
    console = Console()
    print("\n")
    console.rule("Same version apps")
    print(f"{res.filter(lambda x: 'same version' in x).print()}")
    print("\n")
    console.rule("Updated apps")
    print(f"{res.filter(lambda x: 'updated from' in x).print()}")
    print("\n")
    console.rule("Failed apps")
    print(f"{res.filter(lambda x: 'Failed at' in x).print()}")

    print("\n")
    print("Completed Installation".center(100, "-"))
    print("\n" * 2)


if __name__ == '__main__':
    main()
