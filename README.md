# Yaml8

## Project Description

Python package to make getting yaml easier and cleaner

## Installation

To install with pip <br>

```
$ pip install Yaml8
```

## Usage

```python
y = Yaml(f"{os.path.dirname(os.path.realpath(__file__))}/app.yaml")

env = os.getenv('env')

@y.value(f"project-{env}.session-id")
def sessionId(): pass

print(sessionId)
```

## Credits

<table>
  <tr>
        <td align="center"><a href="https://github.com/appdevin"><img src="https://avatars1.githubusercontent.com/u/34540492?s=460&u=6b2d7e8346afc28bfd8e591d93fd548895c720af&v=4" width="100px;" alt=""/><br /><sub><b>Jeyavishnu</b></sub></a><br />
    </td>
  </tr>
</table>

## License

Distributed under the MIT License. See `LICENSE` for more information.
