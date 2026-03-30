import importlib.metadata
import importlib.util
import sys


def check_dependencies() -> bool:
    packages = [
        'pandas',
        'requests',
        'matplotlib'
    ]

    messages = [
        'Data manipulation ready',
        'Network access ready',
        'Visualization ready'
    ]

    print('Checking dependencies:')
    not_ok = 0
    for package, message in zip(packages, messages):
        spec = importlib.util.find_spec(package)
        if spec:
            try:
                version = importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                print(f'Dependency not found: {package}')
                not_ok += 1
                continue
            print(
                f'[OK] {spec.name} ({version}) - {message}'
            )
        else:
            print(f'Dependency not found: {package}')
            not_ok += 1

    return not_ok == 0


def compare_pip_poetry() -> None:
    print('\nDependency manager comparison:')
    print('pip: installs from requirements.txt (exact versions with ==)')
    print('poetry: installs from pyproject.toml (version ranges like ^)')
    print('pip: no lock file required')
    print('poetry: resolves and locks dependency tree')


def analyse_data() -> object:
    import pandas as pd
    import numpy as np

    np.random.seed(42)

    print("Analyzing Matrix data...")
    data = np.random.randn(1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=['signal'])

    return df


def generate_visualization(df: object) -> None:
    import matplotlib.pyplot as plt
    dest = 'matrix_analysis.png'
    print('Generating visualization...')

    fig, ax = plt.subplots()
    ax.hist(df['signal'], bins=50)
    plt.savefig(dest)
    plt.close()

    print('\nAnalysis complete!')
    print(f'Results saved to: {dest}')


def main() -> None:
    print('LOADING STATUS: Loading programs...\n')

    deps_ok = check_dependencies()
    compare_pip_poetry()

    if not deps_ok:
        print('\nMissing dependencies! Install with:')
        print('pip install -r requirements.txt')
        print('or: poetry install')
        sys.exit(1)

    df = analyse_data()
    generate_visualization(df)


if __name__ == '__main__':
    main()
