# vim: set fileencoding=utf-8 noexpandtab tabstop=4 shiftwidth=4

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import os, re, string

from powerline.bindings.tmux import get_tmux_output

@requires_segment_info
class MouseModeSegment(Segment):

    def __call__(self, pl, segment_info):
        return self.mouse_mode(pl)

    def mouse_mode(self, pl, symbol='🐭'):
        '''Return the mouse mode of tmux
        :param string symbol:
            mouse mode symbol
        '''
        session_output = get_tmux_output(pl, 'show-options', '-g', 'mouse')
        if not session_output:
            return None
        mouse_mode = session_output.rstrip().split(' ')[1]

        return symbol if mouse_mode == 'on' else None

mouse_mode = with_docstring(MouseModeSegment(),
'''Return the status of a mouse mode.
''')
