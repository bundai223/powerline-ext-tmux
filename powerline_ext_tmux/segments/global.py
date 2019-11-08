# vim:set fileencoding=utf-8 noexpandtab tabstop=4 shiftwidth=4:noet

from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.bindings.tmux import get_tmux_output


def mouse_mode(pl, symbol='🐭'):
	'''Return the mouse mode of tmux
	:param string symbol:
		mouse mode symbol
	'''
	session_output = get_tmux_output(pl, 'show-options', '-g', 'mouse')
	if not session_output:
		return None
	mouse_mode = session_output.rstrip().split(' ')[1]

	return symbol if mouse_mode == 'on' else None

