from setuptools import setup, find_packages
 
setup(
    include_package_data=True,
	name="dataposts",
	version="0.1",
	packages=find_packages(), # permet de récupérer tout les fichiers 
	description="Module to make DataPosts self bot !",
	url="https://dataposts.hostycd.com/module/",
	author="V / Lou du Poitou",
	license="ISC",
	python_requires=">=3.11.2",
    py_modules=["requests"]
)