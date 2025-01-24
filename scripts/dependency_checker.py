import subprocess


def check_dependency(package):
    # Check if the package is installed; if not, install it
    try:
        __import__(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is not installed. Installing now...")
        # Use subprocess to install the missing package
        subprocess.run(["pip", "install", package])


if __name__ == "__main__":
    dependencies = ['pandas', 'scikit-learn', 'Flask', 'joblib', 'numpy', 'matplotlib']
    for dep in dependencies:
        check_dependency(dep)