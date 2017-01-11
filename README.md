## apt

[![Build Status](https://travis-ci.org/Oefenweb/ansible-apt.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-apt) [![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-apt-blue.svg)](https://galaxy.ansible.com/tersmitten/apt)

Manage packages and up(date|grade)s in Debian-like systems.

#### Requirements

* `python-apt`
* `aptitude`

#### Variables

* `apt_manage_sources_list`: [default: `false`]: Whether or not to manage `/etc/apt/sources.list`
* `apt_ubuntu_mirror`: [default: `mirror://mirrors.ubuntu.com/mirrors.txt`]: The mirror to use
* `apt_src_enable`: [default: `true`]: Whether or not to enable source code repositories
* `apt_ubuntu_universe_enable`: [default: `true`]: Whether or not to enable the `universe` repository
* `apt_ubuntu_multiverse_enable`: [default: `true`]: Whether or not to enable the `multiverse` repository
* `apt_ubuntu_backports_enable`: [default: `true`]: Whether or not to enable the `backports` repository
* `apt_ubuntu_partner_enable`: [default: `false`]: Whether or not to enable the `partner` repository
* `apt_ubuntu_extras_enable`: [default: `false`]: Whether or not to enable the `extras` repository (only applies to < 16.04)
* `apt_debian_mirror`: [default: `http://ftp.nl.debian.org/debian/`]: The mirror to use
* `apt_debian_contrib_nonfree_enable`: [default: `false`]: Whether or not to enable the `contrib` `non-free` repository

* `apt_dependencies`: [default: `[python-apt, aptitude]`]: General dependencies for apt modules to work
* `apt_update`: [default: `true`]: Whether or not to update
* `apt_update_cache_valid_time`: [default: `3600`]: Number of seconds the apt cache stays valid
* `apt_upgrade`: [default: `true`]: Whether or not to upgrade
* `apt_upgrade_type`: [default: `dist`]: If yes or safe, performs an aptitude safe-upgrade. If full, performs an aptitude full-upgrade. If dist, performs an apt-get dist-upgrade
* `apt_upgrade_dpkg_options`: [default: `'force-confdef,force-confold'`]: Add `dpkg` options to `apt` command
* `apt_clean`: [default: `true`]: Whether or not to clean
* `apt_dpkg_configure`: [default: `false`]: Whether or not to run `dpkg --configure -a`
* `apt_autoremove`: [default: `true`]: Whether or not to autoremove
* `apt_install`: [default: `[]`]: Packages to install
* `apt_install_state`: [default: `latest`]: State of packages to install (e.g. `present`)
* `apt_remove`: [default: `[]`]: Packages to remove
* `apt_remove_purge`: [default: `false`]: Whether or not to purge

## Dependencies

None

#### Example

```yaml
---
- hosts: all
  roles:
    - apt
```

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [kosssi](https://github.com/kosssi) and [Ansibles](https://github.com/Ansibles))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-apt/issues)!
