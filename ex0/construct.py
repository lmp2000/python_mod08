import sys
import os
import site


def inside_venv() -> None:

    print(
        '\nMATRIX STATUS: Welcome to the construct\n'
    )

    print(
        f'Current Python: {sys.executable}'
    )
    print(
        f'Virtual environment: {os.path.basename(sys.prefix)}'
    )
    print(
        f'Environment path: {sys.prefix}'
    )
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print(site.getsitepackages()[0])


def outside_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")


def main() -> None:

    is_venv: bool = (
        sys.prefix != sys.base_prefix
    )

    if is_venv:
        try:
            inside_venv()
        except Exception:
            print('Something went wrong...')
    else:
        try:
            outside_venv()
        except Exception:
            print('Something went wrong...')


if __name__ == '__main__':
    main()