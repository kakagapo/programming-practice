# Python programming language

- https://docs.python.org/3/tutorial/index.html
- [The Python Standard Library](https://docs.python.org/3/library/index.html)

The below set of commands is used to create the requirements.txt (this is the easy way) file and then use it to setup the requirements. More info can be found @ [pip documentation](https://pip.pypa.io/en/stable/user_guide/).

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

You probably should adjust the generate file to fit your needs.

Example output of `python -m pip freeze`

```
certifi==2022.9.24
charset-normalizer==2.1.1
idna==3.4
requests==2.28.1
urllib3==1.26.12
```