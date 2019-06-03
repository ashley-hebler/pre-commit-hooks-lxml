from __future__ import print_function
import argparse, sys
from lxml.etree import iterparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--forbidden-attributes', type=lambda s: s.split(','), default=[],
                        help='Comma-separated list of forbidden attribute names')
    args = parser.parse_args(argv)
    matches = list(iterate_attributes(args.filenames))
    return_error_code = 0
    for filename in matches:
        print('target=_blank used with no rel found in {}'.format(filename))
        return_error_code = 1
    return return_error_code

def iterate_attributes(html_filenames):
    for html_filename in html_filenames:
        with open(html_filename, 'rb') as html_file:
            for _, elem in iterparse(html_file, html=True, remove_comments=True):
                print(elem.attrib)
                new_window = False
                includes_rel = False
                for attribute_name in elem.attrib.keys():
                    val = elem.attrib[attribute_name]
                    if attribute_name == 'target' and val = '_blank':
                      new_window = True
                    if attribute_name == 'rel' and val = 'noopener':
                      includes_rel = True
                # yield html_filename, new_window, includes_rel
                if new_window and not includes_rel:
                  yield html_filename
                
            

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
