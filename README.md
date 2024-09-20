# CyLa Mixture
Replaces some Cyrillic letters with similar Latin ones.


## Build
1. clone project
2. create and activate python venv
3. install requirements
4. build with command:
    ```bash
    pyinstaller -F \
        --name CyLaMixture \
        --add-data "resources/*:resources/" \
        -i resources/Ы.ico \
        cyla_mixture/__main__.py 
    ```
5. executable file will appear in the dist dir



