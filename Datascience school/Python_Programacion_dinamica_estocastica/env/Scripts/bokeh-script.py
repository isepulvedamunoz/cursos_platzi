#!"c:\users\usuario\desktop\platzi\datascience school\python_programacion_dinamica_estocastica\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==2.1.1','console_scripts','bokeh'
__requires__ = 'bokeh==2.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==2.1.1', 'console_scripts', 'bokeh')()
    )
