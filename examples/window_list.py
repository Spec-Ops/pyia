import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, "..")
import pyia

desktop = pyia.getDesktop()
for window in desktop:
    if not window.accState(0) & pyia.STATE_SYSTEM_INVISIBLE: 
        print window
