# python-package-template
A template repo for creating a Python PyPi package.

### PyPi Inital Setup:
* Create a PyPi account if you don't have one
* Navigate to `Account Settings > Publishing`
* _(If this is your first time you may need to set up 2-Factor Authentication, Recovery Codes, etc.)_
* Fill out the information:
  * **PyPi Project Name:** The package name (This can differ from the repository name)
  * **Owner:** The organization name (Ceiling-Fan-Studios)
  * **Repository Name:** The name of this repository
  * **Workflow Name:** The PyPi upload workflow (pypi-upload.yml)
  * **Environment Name:** Name of the environment (pypi)

### Modifying Local Files:
#### Changes to make in the folder structure:
Initial folder structure:
```
[PROJECT-NAME]
└─ your-package-name
```
* **PROJECT-NAME:** The root project name. No need to touch this as this is just the name of your project.
* **your-package-name:** Rename this folder to the name of your package. This is what will be used to import your package: `import your-package-name`

#### Changes to make in [setup.py](setup.py):
* **name:** The name of the package as defined in PyPi in the previous steps
* **url:** The url to the GitHub repository
* **author:** Your name
* **author_email:** Your email
* **description:** The short description of your package
* **long-description:** The long description of your package
* **classifiers:** Classifies your package based on certain criteria
  * **Development Status**: Current development status
    * **3 - Alpha** : Early stage of development
    * **4 - Beta** : Feature-complete but may have bugs
    * **5 - Production/Stable** : Stable and usable for production release
  * **Intended Audience:** Intended audience for this package
    * **Developers**
    * **Science/Research**
    * **Education**
  * **License:** License under which your package is distributed
    * **MIT LICENSE:** I recommend this, but I don't remember why.
    * **Apache License 2.0**
    * **GNU General Public License (GPL)**
    * **etc.**
  * **Programming Language:** Language of package for compatibility reasons
    * **Python :: 3** : Compatible with Python 3.x
    * **Python :: 3.9** : Compatible specifically with Python 3.9

Changes to make in [pypi-upload.yml](.github/workflows/pypi-upload.yml)
* **jobs.pypi-upload.environment._url_**: Set the package name in the url to the name you defined in PyPi

#### Writing your code:
* Create classes under your folder that you renamed from `your-package-name`.
* Leave the `__init__.py` file - this marks the folder as a package.

### Publishing to PyPi
* In the GitHub Repository, navigate to the _Actions_ tab.
* Run the workflow named _PyPi Upload_: