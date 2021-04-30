![Logo](https://raw.githubusercontent.com/idealista/wildfly_role/master/logo.gif)

# WildFly Ansible Role [![Build Status](https://travis-ci.com/idealista/wildfly_role.png)](https://travis-ci.com/idealista/wildfly_role)

This Ansible role installs a WildFly server in a Debian environment. Based on the instructions present in [this GitHub Gist](https://gist.github.com/sukharevd/6087988).

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

For compatible Ansible versions check [.travis.yml](.travis.yml).
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with Docker as driver and [Goss](http://goss.rocks) as verifier.

This role needs a system with java previously installed. Its really recommended the use of idealista's java role for that purpose: [idealista.java-role](https://github.com/idealista/java_role).

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista/wildfly_role.git
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

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

```sh
pipenv sync
pipenv shell
```

For more information read the [pipenv docs](https://docs.pipenv.org/).


## Built With

![Ansible](https://img.shields.io/badge/ansible-2.9.14-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.0.4-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.16-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/wildfly_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/wildfly_role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.
