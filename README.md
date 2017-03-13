![Logo](logo.gif)

# WildFly Ansible role

This Ansible role installs a Wildfly server in a Debian environment. Based on the instructions present in [this GitHub Gist](https://gist.github.com/sukharevd/6087988).

- [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)

## Getting Started

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will install a [WildFly](https://docs.jboss.org/author/display/WFLY10/Documentation) server in a Debian system.

### Prerequisities

Ansible 2.2.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista-tech/wildfly-role.git
  scm: git
  version: 1.0.0
  name: wildfly
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: wildfly }
```

## Usage

Look to the defaults properties file to see the possible configuration properties.

## Testing

Execute ``` molecule test ``` under wildfly-role folder to run the automated tests suite.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista-tech/wildfly-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista-tech](https://github.com/idealista-tech)

See also the list of [contributors](https://github.com/idealista-tech/wildfly-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.
