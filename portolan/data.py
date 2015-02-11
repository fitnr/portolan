ABBRS = {
    'nne': {
        'trad': 'Greco-Tramontana', 'point': 'north-northeast', 'mid': 22.5, 'abbr': 'NNE'
    },
    'swbw': {
        'trad': 'Quarto di Libeccio verso Ponente', 'point': 'southwest by west', 'mid': 236.25, 'abbr': 'SWbW'
    },
    'nwbw': {
        'trad': 'Quarto di Maestro verso Ponente', 'point': 'northwest by west', 'mid': 303.75, 'abbr': 'NWbW'
    },
    'swbs': {
        'trad': 'Quarto di Libeccio verso Ostro', 'point': 'southwest by south', 'mid': 213.75, 'abbr': 'SWbS'
    },
    'nwbn': {
        'trad': 'Quarto di Maestro verso Tramontana', 'point': 'northwest by north', 'mid': 326.25, 'abbr': 'NWbN'
    },
    'ebs': {
        'trad': 'Quarto di Levante verso Scirocco', 'point': 'east by south', 'mid': 101.25, 'abbr': 'EbS'
    },
    'nnw': {
        'trad': 'Maestro-Tramontana', 'point': 'north-northwest', 'mid': 337.5, 'abbr': 'NNW'
    },
    'nbe': {
        'trad': 'Quarto di Tramontana verso Greco', 'point': 'north by east', 'mid': 11.25, 'abbr': 'NbE'
    },
    'sebe': {
        'trad': 'Quarto di Scirocco verso Levante', 'point': 'southeast by east', 'mid': 123.75, 'abbr': 'SEbE'
    },
    'ene': {
        'trad': 'Greco-Levante', 'point': 'east-northeast', 'mid': 67.5, 'abbr': 'ENE'
    },
    'nebn': {
        'trad': 'Quarto di Greco verso Tramontana', 'point': 'northeast by north', 'mid': 33.75, 'abbr': 'NEbN'
    },
    'nebe': {
        'trad': 'Quarto di Greco verso Levante', 'point': 'northeast by east', 'mid': 56.25, 'abbr': 'NEbE'
    },
    'ne': {
        'trad': 'Greco', 'point': 'northeast', 'mid': 45.0, 'abbr': 'NE'
    },
    'ese': {
        'trad': 'Levante-Scirocco', 'point': 'east-southeast', 'mid': 112.5, 'abbr': 'ESE'
    },
    'sebs': {
        'trad': 'Quarto di Scirocco verso Ostro', 'point': 'southeast by south', 'mid': 146.25, 'abbr': 'SEbS'
    },
    'ebn': {
        'trad': 'Quarto di Levante verso Greco', 'point': 'east by north', 'mid': 78.75, 'abbr': 'EbN'
    },
    'nw': {
        'trad': 'Maestro', 'point': 'northwest', 'mid': 315.0, 'abbr': 'NW'
    },
    'sbw': {
        'trad': 'Quarto di Ostro verso Libeccio', 'point': 'south by west', 'mid': 191.25, 'abbr': 'SbW'
    },
    'nbw': {
        'trad': 'Quarto di Tramontana verso Maestro', 'point': 'north by west', 'mid': 348.75, 'abbr': 'NbW'
    },
    'ssw': {
        'trad': 'Ostro-Libeccio', 'point': 'south-southwest', 'mid': 202.5, 'abbr': 'SSW'
    },
    'wnw': {
        'trad': 'Maestro-Ponente', 'point': 'west-northwest', 'mid': 292.5, 'abbr': 'WNW'
    },
    'sbe': {
        'trad': 'Quarto di Ostro verso Scirocco', 'point': 'south by east', 'mid': 168.75, 'abbr': 'SbE'
    },
    'sse': {
        'trad': 'Ostro-Scirocco', 'point': 'south-southeast', 'mid': 157.5, 'abbr': 'SSE'
    },
    'e': {
        'trad': 'Levante', 'point': 'east', 'mid': 90.0, 'abbr': 'E'
    },
    'wbs': {
        'trad': 'Quarto di Ponente verso Libeccio', 'point': 'west by south', 'mid': 258.75, 'abbr': 'WbS'
    },
    'sw': {
        'trad': 'Libeccio', 'point': 'southwest', 'mid': 225.0, 'abbr': 'SW'
    },
    'n': {
        'trad': 'Tramontana', 'point': 'north', 'mid': 0.0, 'abbr': 'N'
    },
    'w': {
        'trad': 'Ponente', 'point': 'west', 'mid': 270.0, 'abbr': 'W'
    },
    's': {
        'trad': 'Ostro', 'point': 'south', 'mid': 180.0, 'abbr': 'S'
    },
    'wsw': {
        'trad': 'Ponente-Libeccio', 'point': 'west-southwest', 'mid': 247.5, 'abbr': 'WSW'
    },
    'wbn': {
        'trad': 'Quarto di Ponente verso Maestro', 'point': 'west by north', 'mid': 281.25, 'abbr': 'WbN'
    },
    'se': {
        'trad': 'Scirocco', 'point': 'southeast', 'mid': 135.0, 'abbr': 'SE'
    }
}

SEGMENTS = {
    0: ABBRS['n'],
    1: ABBRS['nbe'],
    2: ABBRS['nne'],
    3: ABBRS['nebn'],
    4: ABBRS['ne'],
    5: ABBRS['nebe'],
    6: ABBRS['ene'],
    7: ABBRS['ebn'],
    8: ABBRS['e'],
    9: ABBRS['ebs'],
    10: ABBRS['ese'],
    11: ABBRS['sebe'],
    12: ABBRS['se'],
    13: ABBRS['sebs'],
    14: ABBRS['sse'],
    15: ABBRS['sbe'],
    16: ABBRS['s'],
    17: ABBRS['sbw'],
    18: ABBRS['ssw'],
    19: ABBRS['swbs'],
    20: ABBRS['sw'],
    21: ABBRS['swbw'],
    22: ABBRS['wsw'],
    23: ABBRS['wbs'],
    24: ABBRS['w'],
    25: ABBRS['wbn'],
    26: ABBRS['wnw'],
    27: ABBRS['nwbw'],
    28: ABBRS['nw'],
    29: ABBRS['nwbn'],
    30: ABBRS['nnw'],
    31: ABBRS['nbw']
}
