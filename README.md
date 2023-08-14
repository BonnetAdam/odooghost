# OdooGhost
*Making Odoo development a breeze.*  

OdooGhost is a powerful tool tailored for streamlining the development and deployment of Odoo instances. It offers an integrated solution that harnesses the power of Docker for orchestrating and managing these instances. With both a Command Line Interface (CLI) and an upcoming web interface, managing Odoo stacks has never been simpler.

## Features

- **Fine-grained Configuration**: Customize each Odoo instance with configuration files, tailoring settings to fit your specific needs.
- **Holistic Instance Management**: With just a few commands, you can create, update, start, stop, and even delete Odoo instances straight from the CLI.

## Installation
To kickstart your OdooGhost journey:
1. Clone the repository: `git clone git@github.com:remyz17/odooghost.git`.
2. Install the required packages: `poetry install`.

## Usage

### Initial Setup
Before diving deep into OdooGhost, ensure you set it up properly. Use the `setup` command and specify your working directory:
```
odooghost setup /you/working/dir
```
### Crafting a Stack
To bring your Odoo instance to life, you first need to define its blueprint - the stack configuration file. Samples to guide your creation can be found in the repository.
```
odooghost stack create you-stack-config.yaml
```

## Contribute
Have ideas or enhancements for OdooGhost? We'd love to see them! Create a Pull Request to join in the journey of making Odoo development smoother for everyone.

## License
Licensed under the [MIT License](LICENSE).
