class MyDriver:
    @property
    def commands(self):
        raise NotImplementedError()


class WindowsDriver(MyDriver):
    commands = {
        'dir': {
            '/l': 'lista ze szczegolami',
            '/a': 'ukryte elementy'
        },
        'ipconfig': {
            '/all': 'wszysciusienko',
            '/?': 'komunikat pomocy'
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
        'sl': {
            '-a': 'ludzie krzycza',
            '-l': 'mniejsza wersja',
            '-F': 'lata'
        }
    }
