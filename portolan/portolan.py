from .data import ABBRS, SEGMENTS


def _by_(key, degree=None, abbr=None):
    if not any([degree, abbr]):
        raise ValueError("Requires an argument")

    if degree:
        return _by_degree(key, degree)

    if abbr:
        return _by_abbr(key, abbr)


def _by_abbr(key, abbr):
    return ABBRS[abbr.lower()][key]


def _by_degree(key, degree):
    # 11.25 is 1/32 of a circle.
    # rotate by half that (5.625) because the 0th segment straddles the origin
    x = int(((degree + 5.625) % 360) / 11.25)
    return SEGMENTS[x][key]


def point(degree=None, abbr=None):
    return _by_('point', degree=degree, abbr=abbr)


def traditional(degree=None, abbr=None):
    return _by_('trad', degree=degree, abbr=abbr)


def abbr(degree):
    return _by_degree('abbreviation', degree)


def degrees(abbr):
    mid = middle(abbr)
    return (mid - 5.625) % 360, mid, mid + 5.625


def middle(abbr):
    return _by_abbr('mid', abbr)


def range(abbr):
    a, _, b = degrees(abbr)
    return (a, b)
