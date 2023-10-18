# Django DI

<p style="align: center">
    <a href="https://pypi.org/project/django-di" target="_blank">
        <img src="https://img.shields.io/pypi/v/django-di?label=PyPI" alt="Package version">
    </a>
</p

Django dependency injection inspired by [ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)

---

### Build

Note: these comands assume a valid [`~/.pypirc`](https://packaging.python.org/en/latest/specifications/pypirc/) file is configured.

See the [official packaging docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more info.

```shell
python3 -m pip install --upgrade build twine
python3 -m build
```

Upload to [test.pypi.org](https://test.pypi.org)

```shell
python3 -m twine upload --repository testpypi dist/*
```

Upload to [PyPI](https://pypi.org)

```shell
python3 -m twine upload dist/*
```

