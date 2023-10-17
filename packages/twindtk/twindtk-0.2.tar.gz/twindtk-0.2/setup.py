from setuptools import setup

setup(
    name="twindtk",
    version="0.2",
    packages=["twindtk", "twindtk.cls", "twindtk.twt"],
    package_data={"windtk": ["assets/*"]},
    install_requires=[
        "ttkbootstrap",
    ],
)


# python setup.py sdist bdist_wheel



# twine upload --repository pypi dist/* --username __token__ --password pypi-AgEIcHlwaS5vcmcCJDBjZTZmZWQyLTBmYmQtNGEzNi1hNjdhLTQxM2U5ZjgzOWFiMwACKlszLCJmMTg4NGRlNC0wOTllLTRhOGMtYTYwZi0zYTdkY2QxN2UzNWMiXQAABiB4VE_ICuov9sMIH8di8eK61W2WYX5ujDPB09gK-F68_A
