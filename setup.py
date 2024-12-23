from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extensions (Cython modules)
extensions = [
    Extension("dual_autodiff_x.dual", ["dual_autodiff_x/dual.pyx"]),
]


# Call setup with cythonized extensions
setup(
    name='dual_autodiff_x',
    ext_modules=cythonize(extensions,
    compiler_directives={'language_level': "3"}),
    packages=["dual_autodiff_x"],
    package_dir={"": "./"},



    zip_safe=False,
)