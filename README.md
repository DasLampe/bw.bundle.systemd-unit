# Configure [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html) via Bundlewrap

## Config
You can configure your unit via dict, every unit accepts and `unit`, `install` and variable `section_type` section below `sections`.
The `section_type` is extracted from the name, by splitting it at `.` and using the last part.

Default for each unit is `running` and `enabled` `true`.

All unit files are written to `/etc/systemd/system` by default, you can change this by setting `path`.
The default `user` and `group` for unit files are 'root'.

### Special `mount` config
In `mount` units you could use `UUID=` in `What`-Option, it will be translated to `/dev/disk/by-uuid/` path via metadata processor.

## Example Config
```python
node = {
    'bundles': [
        'systemd-unit',
    ],
    'metadata': {
        'systemd-unit': {
            'media-backup.mount': {
                'sections': {
                    'unit': {
                        'Description': 'Mountpoint for /media/backup',
                        'Before': 'local-fs.target',
                    },
                    'mount': {
                        'Type': 'ext4',
                        'Where': '/media/backup',
                        'What': '/dev/sda3',
                    },
                    'install': {
                        'WantedBy': 'multi-user.target',
                    }
                },
            }
        }
    }
}
```
