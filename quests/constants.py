CATEGORIES = [
    ('N', 'Naukowa'),
    ('E', 'Edukacyjna'),
    ('O', 'Organizacyjna'),
    ('F', 'Fun Part')
]

TYPES = [
    ('NK', 'Konferencje'),
    ('NA', 'Artykuły'),
    ('ND', 'Debaty'),
    ('NB', 'Badania'),
    ('NS', 'Specjaliści'),
    ('EA', 'Średnia'),
    ('ES', 'Semestry'),
    ('EO', 'Obowiązki Pierwszaka'),
    ('ET', 'Szkolenia'),
    ('EP', 'Staże'),
    ('EC', 'Certyfikaty'),
    ('EB', 'Bierny udział'),
    ('EW', 'Wyjazdy edukacyjne'),
    ('E', 'Specjalne'),
    ('EE', 'Specjaliści'),
    ('OO', 'Organizacje Studenckie'),
    ('OW', 'Wydarzenia'),
    ('OP', 'Praca podczas studiów'),
    ('OE', 'Specjalne'),
    ('OS', 'Specjaliści'),
    ('FW', 'Wyjazdy'),
    ('FI', 'Imprezy integracyjne'),
    ('FA', 'Absurdy'),
    ('FJ', 'Juvenalia'),
    ('FS', 'Specjaliści')
]

# Ta funkcja jednak nie będzie potrzebna -- a może jednak tak???
def check_types_from_specific_category(types, category):
    final_types = []

    for t in types:
        if category in t[0]:
            final_types.append(t)

    return final_types
