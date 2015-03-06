import re

def slugify(s):
    """Convert a string to a URL-friendly slug"""
    slug = s.lower()
    slug = re.sub(r'[^a-zA-Z0-9\s]', '', slug)
    slug = re.sub(r'\s', '-', slug)
    return slug
