class Slash:
    ...


class Etc(Slash):
    ...


class Sbin(Slash):
    ...


class Tmp(Slash):
    ...


class Users(Slash):
    ...


class Dev(Slash):
    ...


class Initd(Etc):
    ...


class Httpd(Etc):
    ...

class Kit(Users):
    ...


assert issubclass(Kit, Slash)
assert not issubclass(Kit, Etc)
assert issubclass(Httpd, Etc)
assert issubclass(Users, Slash)
