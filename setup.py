import setuptools

with open("README.md", "r") as file:
    readme = file.read()

setuptools.setup(
	name="pylink",
	version="1.0.0",
	author="Devesh Singh",
	author_email="connect.world12345@gmail.com",
	description="pylink is a python program which helps you to shorten link with a single command without any registration or using any API Key.Its also provide option to expand any link available on internet on wide range of domain names.",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/TechUX/pylink",
	license="MIT",
	classifiers=["License :: OSI Approved :: MIT License"],
	packages=["pylink"],
	include_package_data=True,
	python_requires='>=2.0',

)
