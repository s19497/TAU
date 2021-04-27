class MyDriver:
    @property
    def commands(self):
        raise NotImplementedError()


class WindowsDriver(MyDriver):
    commands = {
        'dir': {
            '-l': 'lista ze szczegolami',
            '-a': 'ukryte elementy'
        },
        'ipconfig': {
            '-b': 'krowa jest cryborgiem',
            '-d': 'krowa jest martwa'
        },
    }


class LinuxDriver(MyDriver):
    commands = {
        'ls': {
            '-l': 'lista ze szczegolami',
            '-a': 'ukryte elementy'
        },
        'cowsay': {
            '-b': 'krowa jest cryborgiem',
            '-d': 'krowa jest martwa'
        },
    }
