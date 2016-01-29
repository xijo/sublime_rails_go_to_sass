import re

class Resolver:
    def run(self, file):
        if self.is_sass(file):
            return self.get_view(file)
        else:
            return self.get_sass(file)

    def is_sass(self, file):
        return re.search(r'\.sass$', file)

    def get_sass(self, file):
        file      = file.replace('/views/', '/assets/stylesheets/')
        parts     = file.split('/')
        parts[-1] = self.transform_to_sass_filename(parts[-1])
        return ['/'.join(parts)]

    def transform_to_sass_filename(self, filename):
        filename = re.sub(r'.html(.erb|.haml|.slim)', '.sass', filename)
        if not filename.startswith('_'):
            filename = ('_' + filename)
        return filename

    def get_view(self, file):
        variants  = []
        for extension in ['slim', 'erb', 'haml']:
            variants += self.build_view_variants(file, extension)
        return variants

    def build_view_variants(self, file, extension):
        variants = []
        file     = file.replace('/assets/stylesheets/', '/views/')
        parts    = file.split('/')
        filename = parts.pop()

        filename = filename.replace('.sass', '.html.' + extension)
        variant = '/'.join(parts) + '/' + filename
        variants.append(variant)

        filename = re.sub(r'^_', '', filename)
        variant = '/'.join(parts) + '/' + filename
        variants.append(variant)

        return variants
