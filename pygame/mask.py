# Implement the pygame API for the bitmask functions

from pygame._sdl import sdl, ffi
from pygame.surflock import locked
from pygame.color import create_color


class Mask(object):
    """pygame.Mask((width, height)): return Mask

       pygame object for representing 2d bitmask"""

    def __init__(self, size):
        self._mask = sdl.bitmask_create(size[0], size[1])

    def angle(self):
        """angle() -> theta

           Returns the orientation of the pixels"""

    def centroid(self):
        """centroid() -> (x, y)

           Returns the centroid of the pixels in a Mask"""
        pass

    def clear(self):
        """clear() -> None

           Sets all bits to 0"""
        sdl.bitmask_clear(self._mask)

    def connected_component(self, pos=None):
        """connected_component((x,y) = None) -> Mask

            Returns a mask of a connected region of pixels."""
        pass

    def connected_components(self, min=0):
        """connected_components(min = 0) -> [Masks]

           Returns a list of masks of connected regions of pixels."""
        pass

    def convolve(self, othermask, outputmask=None, offset=(0, 0)):
        """convolve(othermask, outputmask = None, offset = (0,0)) -> Mask

           Return the convolution of self with another mask."""
        a = self._mask
        b = othermask._mask
        if outputmask is None:
            outputmask = Mask(a.w + b.w - 1, a.h + b.h - 1)
        sdl.bitmask_convolve(a, b, outputmask._mask, offset[0], offset[1])
        return outputmask

    def count(self):
        """count() -> pixels

           Returns the number of set pixels"""
        return int(sdl.bitmask_count(self._mask))

    def draw(self, othermask, offset):
        """draw(othermask, offset) -> None

           Draws a mask onto another"""
        pass

    def erase(self, othermask, offset):
        """erase(othermask, offset) -> None

           Erases a mask from another"""
        pass

    def fill(self):
        """fill() -> None

           Sets all bits to 1"""
        sdl.bitmask_fill(self._mask)

    def get_at(self, pos):
        """get_at((x,y)) -> int

           Returns nonzero if the bit at (x,y) is set."""
        x, y = pos
        if 0 <= x < self._mask.w and 0 <= y < self._mask.h:
            val = sdl.bitmask_getbit(self._mask, x, y)
        else:
            raise IndexError("%d, %d out of bounds" % pos)
        return val

    def get_bounding_rects(self):
        """get_bounding_rects() -> Rects

           Returns a list of bounding rects of regions of set pixels."""
        pass

    def get_size(self):
        """get_size() -> width,height

           Returns the size of the mask."""
        return self._mask.w, self._mask.h

    def invert(self):
        """invert() -> None

           Flips the bits in a Mask"""
        sdl.bitmask_invert(self._mask)

    def outline(self, every=1):
        """outline(every = 1) -> [(x,y), (x,y) ...]

           list of points outlining an object"""
        pass

    def overlap(self, offset):
        """overlap(othermask, offset) -> x,y

           Returns the point of intersection if the masks overlap with
           the given offset - or None if it does not overlap."""
        pass

    def overlap_area(self, othermask, offest):
        """overlap_area(othermask, offset) -> numpixels

           Returns the number of overlapping 'pixels'."""
        pass

    def overlap_mask(self, othermask, offset):
        """overlap_mask(othermask, offset) -> Mask

            Returns a mask of the overlapping pixels"""
        pass

    def scale(self, new_size):
        """scale((x, y)) -> Mask

            Resizes a mask"""
        output = Mask(new_size)
        output._mask = sdl.bitmask_scale(self._mask, new_size[0], new_size[1])
        return output

    def set_at(self, pos, value):
        """set_at((x,y),value) -> None

           Sets the position in the mask given by x and y."""
        x, y = pos
        if 0 <= x < self._mask.w and 0 <= y < self._mask.h:
            if value:
                sdl.bitmask_setbit(self._mask, x, y)
            else:
                sdl.bitmask_clearbit(self._mask, x, y)
        else:
            raise IndexError("%d, %d out of bounds" % pos)



def from_surface(surf, threshold=127):
    """from_surface(surf, threshold = 127) -> Mask

       Returns a Mask from the given surface"""
    c_surf = surf._c_surface
    output_mask = Mask((surf._w, surf._h))
    # colorkey will be None if we're not using a colorkey
    colorkey = surf.get_colorkey()
    format = surf._c_surface.format
    r, g, b, a = (ffi.new('uint8_t *'), ffi.new('uint8_t *'),
                  ffi.new('uint8_t *'), ffi.new('uint8_t *'))
    with locked(c_surf):
        for y in range(surf._h):
            for x in range(surf._w):
                sdl.SDL_GetRGBA(surf._get_at(x, y), format, r, g, b, a)
                if colorkey is None:
                    # check alpha
                    if a[0] > threshold:
                        sdl.bitmask_setbit(output_mask._mask, x, y)
                else:
                    pixel = (r[0], g[0], b[0], a[0])
                    if pixel == colorkey:
                        sdl.bitmask_setbit(output_mask._mask, x, y)
    return output_mask


def from_threshold(surf, color, threshold=(0, 0, 0, 255), othersurface=None,
                   palette_colors=1):
    """from_threshold(surf, color, threshold = (0,0,0,255), othersurface = None,
                      palette_colors = 1) -> Mask

        Creates a mask by thresholding Surfaces"""
    c_surf = surf._c_surface
    color = create_color(color, surf._c_surface.format)
    if threshold:
        threshold = create_color(threshold, c_surf.format)

    output_mask = Mask((surf._w, surf._h))

    with locked(c_surf):
        if othersurface:
            surf2 = othersurface._c_surf
            with locked(surf2):
                sdl.bitmask_threshold(output_mask._mask, surf, surf2, color,
                                      threshold, palette_colors)
        else:
            sdl.bitmask_threshold(output_mask._mask, surf, ffi.NULL, color,
                                  threshold, palette_colors)
    return output_mask
