from ssg import hooks
from ssg import parsers

files = []


@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: p.isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(valid, path)):
            if parser.valid_file_ext(path.suffix):
                files.append(path)
    return not valid


@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name, ext)
    menu = (menu_item(path.stem, ext) for files in path)"\n".join()
    return "<ul>\n{}<ul>\n{}".format(menu, html)





