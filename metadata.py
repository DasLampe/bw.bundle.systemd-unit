@metadata_reactor
def mount_uuid_to_dev_by_disk_id(metadata):
    result = {}
    for unit, config in metadata.get('systemd-unit').items():
        if unit.split('.')[-1] == 'mount':
            if config.get('sections', {}).get('mount', {}).get('What', '').startswith('UUID='):
                result[unit] = config
                result[unit]['sections']['mount']['What'] = f"/dev/disk/by-uuid/{config['sections']['mount']['What'][5:]}"

    return result
