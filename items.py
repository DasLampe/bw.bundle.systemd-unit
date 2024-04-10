files = {}
svc_systemd = {}

actions = {
    'systemctl-daemon-reload': {
        'command': 'systemctl daemon-reload',
        'triggered': True,
        'needs': [
            'tag:systemd_units',
        ],
    },
}

for name, config in node.metadata.get('systemd-unit', {}).items():
    unitPath = config.get('path', '/etc/systemd/system')

    files[f'{unitPath}/{name}'] = {
        'source': 'unit.tpl.j2',
        'content_type': 'jinja2',
        'context': {
            'sections': {key: val for key, val in sorted(config.get('sections', {}).items(), key = lambda ele: ele[0])},
            'section_type': name.split('.')[-1],
        },
        'owner': config.get('user', 'root'),
        'group': config.get('group', 'root'),
        'mode': '0644',
        'triggers': [
            'action:systemctl-daemon-reload',
            f'svc_systemd:{name}:reload'
        ],
        'tags': [
            'systemd_units',
        ],
    }

    svc_systemd[name] = {
        'running': config.get('running', True),
        'enabled': config.get('enabled', True),
        'needs': [
            'action:systemctl-daemon-reload',
        ],
    }
