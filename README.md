## apt [![Build Status](https://travis-ci.org/Oefenweb/ansible-apt.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-apt)

Manage packages and up(date|grade)s in Debian-like systems.

#### Requirements

* `python-apt`
* `aptitude`

#### Variables

* `apt_dependencies` [default: `[python-apt, aptitude]`]: General dependencies for apt modules to work
* `apt_update`: [default: `true`]: Whether or not to update
* `apt_update_cache_valid_time` [default: `3600`]: Number of seconds the apt cache stays valid
* `apt_upgrade` [default: `true`]: Whether or not to upgrade
* `apt_upgrade_type` [default: `dist`]: If yes or safe, performs an aptitude safe-upgrade. If full, performs an aptitude full-upgrade. If dist, performs an apt-get dist-upgrade
* `apt_clean` [default: `true`]: Whether or not to clean
* `apt_autoremove` [default: `true`]: Whether or not to autoremove
* `apt_install`: [default: `[]`]: Packages to install
* `apt_remove`: [default: `[]`]: Packages to remove
* `apt_remove_purge` [default: `false`]: Whether or not to purge

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

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-apt/issues)!
