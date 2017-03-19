# The conf_tests module
# Copyright (C) 2014  Neil Muller
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301  USA

from .helpers import gen_test_image, test_conformance

from .test_lines import (test_horz_line, test_horz_line_width,
                         test_vert_line, test_vert_line_width,
                         test_lines, test_lines_width,
                         test_lines_function)

from .test_transforms import (test_flip, test_scale, test_rotate, test_chop,
                              test_rotozoom, test_flip_subsurface,
                              test_chop_subsurface)
from .test_shapes import (test_rect, test_polygon, test_hollow_circles,
                          test_filled_circles, test_filled_ellipses_1,
                          test_filled_ellipses_2, test_hollow_ellipses,
                          test_filled_circles_limits)
from .test_surface import test_scroll
from .test_blending import (test_rgba_add, test_rgba_sub, test_rgba_min,
                            test_rgba_max, test_rgba_mult, test_rgb_mult,
                            test_blend_mult)
from .test_smoothscale import (test_int_smoothscale, test_x_smoothscale,
                               test_y_smoothscale, test_varied_smoothscale,
                               test_subsurface_smoothscale)

conformance_tests = {
    'test_rgba_add': test_rgba_add,
    'test_rgba_sub': test_rgba_sub,
    'test_rgba_min': test_rgba_min,
    'test_rgba_max': test_rgba_max,
    'test_rgba_mult': test_rgba_mult,
    'test_rgb_mult': test_rgb_mult,
    'test_blend_mult': test_blend_mult,
    'horz1': test_horz_line,
    'horz_widths': test_horz_line_width,
    'vert1': test_vert_line,
    'vert_widths': test_vert_line_width,
    'lines': test_lines,
    'lines_width': test_lines_width,
    'lines_func': test_lines_function,
    'scale': test_scale,
    'flip': test_flip,
    'flip_subsurface': test_flip_subsurface,
    'rotate': test_rotate,
    'rect': test_rect,
    'polygon': test_polygon,
    'scroll': test_scroll,
    'smooth_int': test_int_smoothscale,
    'smooth_x': test_x_smoothscale,
    'smooth_y': test_y_smoothscale,
    'smooth_varies': test_varied_smoothscale,
    'smooth_subsurface': test_subsurface_smoothscale,
    'chop': test_chop,
    'chop_subsurface': test_chop_subsurface,
    'rotozoom': test_rotozoom,
    'hollow_circles': test_hollow_circles,
    'filled_circles': test_filled_circles,
    'filled_ellipses_1': test_filled_ellipses_1,
    'filled_ellipses_2': test_filled_ellipses_2,
    'hollow_ellipses': test_hollow_ellipses,
    'limit_circles': test_filled_circles_limits,
}


__all__ = [conformance_tests, gen_test_image, test_conformance]
