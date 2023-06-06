def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def _extract_lower(phrase):
    return list(filter(str.islower, phrase))
