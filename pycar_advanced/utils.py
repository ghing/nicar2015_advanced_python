import re

def slugify(s):
    """Convert a string to a URL-friendly slug"""
    slug = s.lower().strip()
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', slug)
    slug = re.sub(r'\s', '-', slug)
    slug = re.sub(r'-{2,}', '-', slug)
    return slug
