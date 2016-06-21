# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_fitz')).lstrip('.')
        return importlib.import_module(mname)
    _fitz = swig_import_helper()
    del swig_import_helper
elif version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fitz', [dirname(__file__)])
        except ImportError:
            import _fitz
            return _fitz
        if fp is not None:
            try:
                _mod = imp.load_module('_fitz', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fitz = swig_import_helper()
    del swig_import_helper
else:
    import _fitz
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


import os                     
VersionFitz = "1.9a"          
VersionBind = "1.9.1"         
VersionDate = "2016-06-21 07:58:18"        

class Document(_object):
    """Proxy of C fz_document_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Document, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Document, name)
    __repr__ = _swig_repr

    def __init__(self, filename, stream=None, streamlen=0):
        """__init__(fz_document_s self, char const * filename, char * stream=None, int streamlen=0) -> Document"""

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")
        if not os.path.exists(filename) and streamlen == 0:
            raise IOError("no such file: " + filename)
        self.name = filename
        self.streamlen = streamlen
        self.isClosed = 0
        self.isEncrypted = 0
        self.metadata = None



        this = _fitz.new_Document(filename, stream, streamlen)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        if this:
            self.openErrCode = self._getGCTXerrcode();
            self.openErrMsg  = self._getGCTXerrmsg();
        if this and self.needsPass:
            self.isEncrypted = 1
        # we won't init encrypted doc until it is decrypted
        if this and not self.needsPass:
            self.initData()
            self.thisown = False




    def close(self):
        """close(Document self)"""

        if self.isClosed == 1:
            raise ValueError("operation on closed document")
        if hasattr(self, '_outline') and self._outline:
            self._dropOutline(self._outline)
            self._outline = None
        self.metadata = None
        self.isClosed = 1


        return _fitz.Document_close(self)


    def loadPage(self, number):
        """loadPage(Document self, int number) -> Page"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        val = _fitz.Document_loadPage(self, number)

        if val:
            val.thisown = True
            val.number = number
            val.parent = self


        return val


    def _loadOutline(self):
        """_loadOutline(Document self) -> Outline"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        return _fitz.Document__loadOutline(self)


    def _dropOutline(self, ol):
        """_dropOutline(Document self, Outline ol)"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        return _fitz.Document__dropOutline(self, ol)


    def _getPageCount(self):
        """_getPageCount(Document self) -> int"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        return _fitz.Document__getPageCount(self)


    def _getMetadata(self, key):
        """_getMetadata(Document self, char const * key) -> char *"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        return _fitz.Document__getMetadata(self, key)


    def _needsPass(self):
        """_needsPass(Document self) -> int"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        return _fitz.Document__needsPass(self)


    def _getGCTXerrcode(self):
        """_getGCTXerrcode(Document self) -> int"""
        return _fitz.Document__getGCTXerrcode(self)


    def _getGCTXerrmsg(self):
        """_getGCTXerrmsg(Document self) -> char *"""
        return _fitz.Document__getGCTXerrmsg(self)


    def authenticate(self, arg2):
        """authenticate(Document self, char const * arg2) -> int"""

        if self.isClosed:
            raise ValueError("operation on closed document")


        val = _fitz.Document_authenticate(self, arg2)

        if val: # the doc is decrypted successfully and we init the outline
            self.isEncrypted = 0
            self.initData()


        return val


    def save(self, filename, garbage=0, clean=0, deflate=0, incremental=0, ascii=0, expand=0, linear=0):
        """save(Document self, char * filename, int garbage=0, int clean=0, int deflate=0, int incremental=0, int ascii=0, int expand=0, int linear=0) -> int"""

        if self.isClosed == 1:
            raise ValueError("operation on closed document")
        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")
        if filename == self.name and incremental == 0:
            raise ValueError("cannot save to input file")
        if not self.name.lower().endswith(("/pdf", ".pdf")):
            raise ValueError("can only save PDF files")
        if incremental and (self.name != filename or self.streamlen > 0):
            raise ValueError("incremental save to original file only")
        if incremental and (garbage > 0 or linear > 0):
            raise ValueError("incremental excludes garbage and linear")
        if incremental and self.openErrCode > 0:
            raise ValueError("error '%s' during open - save to new file" % (self.openErrMsg,))
        if incremental and self.needsPass > 0:
            raise ValueError("decrypted files must be saved to new file")


        return _fitz.Document_save(self, filename, garbage, clean, deflate, incremental, ascii, expand, linear)


    def _select(self, liste):
        """_select(Document self, int * liste) -> int"""
        return _fitz.Document__select(self, liste)


    def _readPageText(self, pno, output=0):
        """_readPageText(Document self, int pno, int output=0) -> struct fz_buffer_s *"""
        return _fitz.Document__readPageText(self, pno, output)


    def getPermits(self):
        """getPermits(self) -> dictionary containing permissions"""

        if self.isClosed == 1:
            raise ValueError("operation on closed document")


        val = _fitz.Document_getPermits(self)

                    # transform bitfield response into dictionary
        d = {}
        if val % 2: # print permission?
            d["print"] = True
        else:
            d["print"] = False
        val = val >> 1
        if val % 2: # edit permission?
            d["edit"] = True
        else:
            d["edit"] = False
        val = val >> 1
        if val % 2: # copy permission?
            d["copy"] = True
        else:
            d["copy"] = False
        val = val >> 1
        if val % 2: # annotate permission?
            d["note"] = True
        else:
            d["note"] = False
        val = d


        return val


    def _getPageObjNumber(self, pno):
        """_getPageObjNumber(Document self, int pno) -> PyObject *"""
        return _fitz.Document__getPageObjNumber(self, pno)


    def _delToC(self):
        """_delToC(Document self) -> int"""
        val = _fitz.Document__delToC(self)

        self.initData()


        return val


    def _getOLRootNumber(self):
        """_getOLRootNumber(Document self) -> int"""
        return _fitz.Document__getOLRootNumber(self)


    def _getNewXref(self):
        """_getNewXref(Document self) -> int"""
        return _fitz.Document__getNewXref(self)


    def _updateObject(self, xref, text):
        """_updateObject(Document self, int xref, char * text) -> int"""
        return _fitz.Document__updateObject(self, xref, text)


    def _setMetadata(self, text):
        """_setMetadata(Document self, char * text) -> int"""
        return _fitz.Document__setMetadata(self, text)


    def initData(self):
        if self.isEncrypted:
            raise ValueError("cannot initData - document still encrypted")
        self._outline = self._loadOutline()
        self.metadata = dict([(k,self._getMetadata(v)) for k,v in {'format':'format', 'title':'info:Title', 'author':'info:Author','subject':'info:Subject', 'keywords':'info:Keywords','creator':'info:Creator', 'producer':'info:Producer', 'creationDate':'info:CreationDate', 'modDate':'info:ModDate'}.items()])
        self.metadata['encryption'] = None if self._getMetadata('encryption')=='None' else self._getMetadata('encryption')

    outline = property(lambda self: self._outline)
    pageCount = property(lambda self: self._getPageCount())
    needsPass = property(lambda self: self._needsPass())

    def __repr__(self):
        if self.streamlen == 0:
            return "fitz.Document('%s')" % (self.name,)
        return "fitz.Document('%s', stream = <data>, streamlen = %s)" % (self.name, self.streamlen)


    __swig_destroy__ = _fitz.delete_Document
    __del__ = lambda self: None
Document_swigregister = _fitz.Document_swigregister
Document_swigregister(Document)

class Page(_object):
    """Proxy of C fz_page_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Page, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Page, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _fitz.delete_Page
    __del__ = lambda self: None

    def bound(self):
        """bound(Page self) -> Rect"""

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        val = _fitz.Page_bound(self)

        if val:
            val.thisown = True


        return val


    def run(self, dw, m):
        """run(Page self, Device dw, Matrix m) -> int"""

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        return _fitz.Page_run(self, dw, m)


    def loadLinks(self):
        """loadLinks(Page self) -> Link"""

        if self.parent.isClosed == 1:
            raise ValueError("page operation on closed document")


        val = _fitz.Page_loadLinks(self)

        if val:
            val.thisown = True


        return val


    def _readPageText(self, output=0):
        """_readPageText(Page self, int output=0) -> struct fz_buffer_s *"""
        return _fitz.Page__readPageText(self, output)


    def __str__(self):
        return "page %s of %s" % (self.number, repr(self.parent))
    def __repr__(self):
        return repr(self.parent) + ".loadPage(" + str(self.number) + ")"

Page_swigregister = _fitz.Page_swigregister
Page_swigregister(Page)


def _fz_transform_rect(rect, transform):
    """_fz_transform_rect(Rect rect, Matrix transform) -> Rect"""
    return _fitz._fz_transform_rect(rect, transform)
class Rect(_object):
    """Proxy of C fz_rect_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x0"] = _fitz.Rect_x0_set
    __swig_getmethods__["x0"] = _fitz.Rect_x0_get
    if _newclass:
        x0 = _swig_property(_fitz.Rect_x0_get, _fitz.Rect_x0_set)
    __swig_setmethods__["y0"] = _fitz.Rect_y0_set
    __swig_getmethods__["y0"] = _fitz.Rect_y0_get
    if _newclass:
        y0 = _swig_property(_fitz.Rect_y0_get, _fitz.Rect_y0_set)
    __swig_setmethods__["x1"] = _fitz.Rect_x1_set
    __swig_getmethods__["x1"] = _fitz.Rect_x1_get
    if _newclass:
        x1 = _swig_property(_fitz.Rect_x1_get, _fitz.Rect_x1_set)
    __swig_setmethods__["y1"] = _fitz.Rect_y1_set
    __swig_getmethods__["y1"] = _fitz.Rect_y1_get
    if _newclass:
        y1 = _swig_property(_fitz.Rect_y1_get, _fitz.Rect_y1_set)

    def __init__(self, *args):
        """
        __init__(fz_rect_s self) -> Rect
        __init__(fz_rect_s self, Rect s) -> Rect
        __init__(fz_rect_s self, Point lt, Point rb) -> Rect
        __init__(fz_rect_s self, float x0, float y0, Point rb) -> Rect
        __init__(fz_rect_s self, Point lt, float x1, float y1) -> Rect
        __init__(fz_rect_s self, float x0, float y0, float x1, float y1) -> Rect
        """
        this = _fitz.new_Rect(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def round(self):
        """round(Rect self) -> IRect"""
        val = _fitz.Rect_round(self)

        val.thisown = True


        return val


    def includePoint(self, p):
        """includePoint(Rect self, Point p) -> Rect"""
        return _fitz.Rect_includePoint(self, p)


    def intersect(self, r):
        """intersect(Rect self, Rect r) -> Rect"""
        return _fitz.Rect_intersect(self, r)


    def includeRect(self, r):
        """includeRect(Rect self, Rect r) -> Rect"""
        return _fitz.Rect_includeRect(self, r)


    def transform(self, m):
        _fitz._fz_transform_rect(self, m)
        return self

    def __len__(self):
        return 4

    def __repr__(self):
        return "fitz.Rect" + str((self.x0, self.y0, self.x1, self.y1))

    width = property(lambda self: self.x1-self.x0)
    height = property(lambda self: self.y1-self.y0)

    __swig_destroy__ = _fitz.delete_Rect
    __del__ = lambda self: None
Rect_swigregister = _fitz.Rect_swigregister
Rect_swigregister(Rect)

class IRect(_object):
    """Proxy of C fz_irect_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IRect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x0"] = _fitz.IRect_x0_set
    __swig_getmethods__["x0"] = _fitz.IRect_x0_get
    if _newclass:
        x0 = _swig_property(_fitz.IRect_x0_get, _fitz.IRect_x0_set)
    __swig_setmethods__["y0"] = _fitz.IRect_y0_set
    __swig_getmethods__["y0"] = _fitz.IRect_y0_get
    if _newclass:
        y0 = _swig_property(_fitz.IRect_y0_get, _fitz.IRect_y0_set)
    __swig_setmethods__["x1"] = _fitz.IRect_x1_set
    __swig_getmethods__["x1"] = _fitz.IRect_x1_get
    if _newclass:
        x1 = _swig_property(_fitz.IRect_x1_get, _fitz.IRect_x1_set)
    __swig_setmethods__["y1"] = _fitz.IRect_y1_set
    __swig_getmethods__["y1"] = _fitz.IRect_y1_get
    if _newclass:
        y1 = _swig_property(_fitz.IRect_y1_get, _fitz.IRect_y1_set)

    def __init__(self, *args):
        """
        __init__(fz_irect_s self) -> IRect
        __init__(fz_irect_s self, IRect s) -> IRect
        __init__(fz_irect_s self, int x0, int y0, int x1, int y1) -> IRect
        """
        this = _fitz.new_IRect(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def translate(self, xoff, yoff):
        """translate(IRect self, int xoff, int yoff) -> IRect"""
        return _fitz.IRect_translate(self, xoff, yoff)


    def intersect(self, ir):
        """intersect(IRect self, IRect ir) -> IRect"""
        return _fitz.IRect_intersect(self, ir)


    width = property(lambda self: self.x1-self.x0)
    height = property(lambda self: self.y1-self.y0)

    def getRect(self):
        return Rect(self.x0, self.y0, self.x1, self.y1)

    def __len__(self):
        return 4

    def __repr__(self):
        return "fitz.IRect" + str((self.x0, self.y0, self.x1, self.y1))

    __swig_destroy__ = _fitz.delete_IRect
    __del__ = lambda self: None
IRect_swigregister = _fitz.IRect_swigregister
IRect_swigregister(IRect)

class Pixmap(_object):
    """Proxy of C fz_pixmap_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pixmap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pixmap, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _fitz.Pixmap_x_set
    __swig_getmethods__["x"] = _fitz.Pixmap_x_get
    if _newclass:
        x = _swig_property(_fitz.Pixmap_x_get, _fitz.Pixmap_x_set)
    __swig_setmethods__["y"] = _fitz.Pixmap_y_set
    __swig_getmethods__["y"] = _fitz.Pixmap_y_get
    if _newclass:
        y = _swig_property(_fitz.Pixmap_y_get, _fitz.Pixmap_y_set)
    __swig_setmethods__["w"] = _fitz.Pixmap_w_set
    __swig_getmethods__["w"] = _fitz.Pixmap_w_get
    if _newclass:
        w = _swig_property(_fitz.Pixmap_w_get, _fitz.Pixmap_w_set)
    __swig_setmethods__["h"] = _fitz.Pixmap_h_set
    __swig_getmethods__["h"] = _fitz.Pixmap_h_get
    if _newclass:
        h = _swig_property(_fitz.Pixmap_h_get, _fitz.Pixmap_h_set)
    __swig_setmethods__["n"] = _fitz.Pixmap_n_set
    __swig_getmethods__["n"] = _fitz.Pixmap_n_get
    if _newclass:
        n = _swig_property(_fitz.Pixmap_n_get, _fitz.Pixmap_n_set)
    __swig_setmethods__["interpolate"] = _fitz.Pixmap_interpolate_set
    __swig_getmethods__["interpolate"] = _fitz.Pixmap_interpolate_get
    if _newclass:
        interpolate = _swig_property(_fitz.Pixmap_interpolate_get, _fitz.Pixmap_interpolate_set)
    __swig_setmethods__["xres"] = _fitz.Pixmap_xres_set
    __swig_getmethods__["xres"] = _fitz.Pixmap_xres_get
    if _newclass:
        xres = _swig_property(_fitz.Pixmap_xres_get, _fitz.Pixmap_xres_set)
    __swig_setmethods__["yres"] = _fitz.Pixmap_yres_set
    __swig_getmethods__["yres"] = _fitz.Pixmap_yres_get
    if _newclass:
        yres = _swig_property(_fitz.Pixmap_yres_get, _fitz.Pixmap_yres_set)

    def __init__(self, *args):
        """
        __init__(fz_pixmap_s self, Colorspace cs, IRect bbox) -> Pixmap
        __init__(fz_pixmap_s self, Colorspace cs, int w, int h, char * samples) -> Pixmap
        __init__(fz_pixmap_s self, char * filename) -> Pixmap
        __init__(fz_pixmap_s self, char * imagedata, int size) -> Pixmap
        """
        this = _fitz.new_Pixmap(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_Pixmap
    __del__ = lambda self: None

    def gammaWith(self, gamma):
        """gammaWith(Pixmap self, float gamma)"""
        return _fitz.Pixmap_gammaWith(self, gamma)


    def tintWith(self, red, green, blue):
        """tintWith(Pixmap self, int red, int green, int blue)"""

                    # only GRAY and RGB pixmaps allowed
        if self.n not in (2, 4):
            raise TypeError("only gray and rgb pixmaps can be tinted")


        return _fitz.Pixmap_tintWith(self, red, green, blue)


    def clearWith(self, *args):
        """
        clearWith(Pixmap self, int value)
        clearWith(Pixmap self, int value, IRect bbox)
        """
        return _fitz.Pixmap_clearWith(self, *args)


    def copyPixmap(self, src, bbox):
        """copyPixmap(Pixmap self, Pixmap src, IRect bbox)"""
        return _fitz.Pixmap_copyPixmap(self, src, bbox)


    def getSize(self):
        """getSize(Pixmap self) -> int"""
        return _fitz.Pixmap_getSize(self)


    def writePNG(self, filename, savealpha=0):
        """writePNG(Pixmap self, char * filename, int savealpha=0) -> int"""

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")
        if not filename.lower().endswith(".png"):
            raise ValueError("filename must end with '.png'")


        return _fitz.Pixmap_writePNG(self, filename, savealpha)


    def getPNGData(self, savealpha=0):
        """getPNGData(Pixmap self, int savealpha=0) -> struct fz_buffer_s *"""
        return _fitz.Pixmap_getPNGData(self, savealpha)


    def samplesRGB(self):
        """samplesRGB(Pixmap self) -> PyObject *"""
        return _fitz.Pixmap_samplesRGB(self)


    def samplesAlpha(self):
        """samplesAlpha(Pixmap self) -> PyObject *"""
        return _fitz.Pixmap_samplesAlpha(self)


    def _writeIMG(self, filename, format, savealpha=0):
        """_writeIMG(Pixmap self, char * filename, int format, int savealpha=0) -> int"""
        return _fitz.Pixmap__writeIMG(self, filename, format, savealpha)


    def invertIRect(self, *args):
        """
        invertIRect(Pixmap self)
        invertIRect(Pixmap self, IRect irect)
        """
        return _fitz.Pixmap_invertIRect(self, *args)


    def _getSamples(self):
        """_getSamples(Pixmap self) -> PyObject *"""
        return _fitz.Pixmap__getSamples(self)


    samples = property(lambda self: self._getSamples())
    __len__ = getSize
    width  = w
    height = h

    def __repr__(self):
        cs = {2:"GRAY", 4:"RGB", 5:"CMYK"}
        return "fitz.Pixmap(fitz.cs%s, fitz.IRect(%s, %s, %s, %s))" % (cs[self.n], self.x, self.y, self.x + self.width, self.y + self.height)


Pixmap_swigregister = _fitz.Pixmap_swigregister
Pixmap_swigregister(Pixmap)

CS_RGB = _fitz.CS_RGB
CS_GRAY = _fitz.CS_GRAY
CS_CMYK = _fitz.CS_CMYK
class Colorspace(_object):
    """Proxy of C fz_colorspace_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Colorspace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Colorspace, name)
    __repr__ = _swig_repr

    def __init__(self, type):
        """__init__(fz_colorspace_s self, int type) -> Colorspace"""
        this = _fitz.new_Colorspace(type)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_Colorspace
    __del__ = lambda self: None
Colorspace_swigregister = _fitz.Colorspace_swigregister
Colorspace_swigregister(Colorspace)

class Device(_object):
    """Proxy of C DeviceWrapper struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Device, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(DeviceWrapper self, Pixmap pm, IRect clip) -> Device
        __init__(DeviceWrapper self, DisplayList dl) -> Device
        __init__(DeviceWrapper self, TextSheet ts, TextPage tp) -> Device
        """
        this = _fitz.new_Device(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_Device
    __del__ = lambda self: None
Device_swigregister = _fitz.Device_swigregister
Device_swigregister(Device)


def _fz_pre_scale(m, sx, sy):
    """_fz_pre_scale(Matrix m, float sx, float sy) -> Matrix"""
    return _fitz._fz_pre_scale(m, sx, sy)

def _fz_pre_shear(m, sx, sy):
    """_fz_pre_shear(Matrix m, float sx, float sy) -> Matrix"""
    return _fitz._fz_pre_shear(m, sx, sy)

def _fz_pre_rotate(m, degree):
    """_fz_pre_rotate(Matrix m, float degree) -> Matrix"""
    return _fitz._fz_pre_rotate(m, degree)
class Matrix(_object):
    """Proxy of C fz_matrix_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["a"] = _fitz.Matrix_a_set
    __swig_getmethods__["a"] = _fitz.Matrix_a_get
    if _newclass:
        a = _swig_property(_fitz.Matrix_a_get, _fitz.Matrix_a_set)
    __swig_setmethods__["b"] = _fitz.Matrix_b_set
    __swig_getmethods__["b"] = _fitz.Matrix_b_get
    if _newclass:
        b = _swig_property(_fitz.Matrix_b_get, _fitz.Matrix_b_set)
    __swig_setmethods__["c"] = _fitz.Matrix_c_set
    __swig_getmethods__["c"] = _fitz.Matrix_c_get
    if _newclass:
        c = _swig_property(_fitz.Matrix_c_get, _fitz.Matrix_c_set)
    __swig_setmethods__["d"] = _fitz.Matrix_d_set
    __swig_getmethods__["d"] = _fitz.Matrix_d_get
    if _newclass:
        d = _swig_property(_fitz.Matrix_d_get, _fitz.Matrix_d_set)
    __swig_setmethods__["e"] = _fitz.Matrix_e_set
    __swig_getmethods__["e"] = _fitz.Matrix_e_get
    if _newclass:
        e = _swig_property(_fitz.Matrix_e_get, _fitz.Matrix_e_set)
    __swig_setmethods__["f"] = _fitz.Matrix_f_set
    __swig_getmethods__["f"] = _fitz.Matrix_f_get
    if _newclass:
        f = _swig_property(_fitz.Matrix_f_get, _fitz.Matrix_f_set)

    def __init__(self, *args):
        """
        __init__(fz_matrix_s self) -> Matrix
        __init__(fz_matrix_s self, Matrix n) -> Matrix
        __init__(fz_matrix_s self, float sx, float sy, int shear=0) -> Matrix
        __init__(fz_matrix_s self, float degree) -> Matrix
        """
        this = _fitz.new_Matrix(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def invert(self, m):
        """invert(Matrix self, Matrix m) -> int"""
        return _fitz.Matrix_invert(self, m)


    def preTranslate(self, sx, sy):
        """preTranslate(Matrix self, float sx, float sy) -> Matrix"""
        return _fitz.Matrix_preTranslate(self, sx, sy)


    def concat(self, m1, m2):
        """concat(Matrix self, Matrix m1, Matrix m2) -> Matrix"""
        return _fitz.Matrix_concat(self, m1, m2)


    def preScale(self, sx, sy):
        """preScale(Matrix self, float sx, float sy) -> Matrix self updated"""
        _fitz._fz_pre_scale(self, sx, sy)
        return self
    def preShear(self, sx, sy):
        """preShear(Matrix self, float sx, float sy) -> Matrix self updated"""
        _fitz._fz_pre_shear(self, sx, sy)
        return self
    def preRotate(self, degree):
        """preRotate(Matrix self, float degree) -> Matrix self updated"""
        _fitz._fz_pre_rotate(self, degree)
        return self
    def __len__(self):
        return 6
    def __repr__(self):
        return "fitz.Matrix(%s, %s, %s, %s, %s, %s)" % (self.a, self.b, self.c, self.d, self.e, self.f)

    __swig_destroy__ = _fitz.delete_Matrix
    __del__ = lambda self: None
Matrix_swigregister = _fitz.Matrix_swigregister
Matrix_swigregister(Matrix)

class Outline(_object):
    """Proxy of C fz_outline_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Outline, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Outline, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["title"] = _fitz.Outline_title_get
    if _newclass:
        title = _swig_property(_fitz.Outline_title_get)
    __swig_getmethods__["dest"] = _fitz.Outline_dest_get
    if _newclass:
        dest = _swig_property(_fitz.Outline_dest_get)
    __swig_getmethods__["next"] = _fitz.Outline_next_get
    if _newclass:
        next = _swig_property(_fitz.Outline_next_get)
    __swig_getmethods__["down"] = _fitz.Outline_down_get
    if _newclass:
        down = _swig_property(_fitz.Outline_down_get)
    __swig_getmethods__["is_open"] = _fitz.Outline_is_open_get
    if _newclass:
        is_open = _swig_property(_fitz.Outline_is_open_get)

    def saveXML(self, filename):
        """saveXML(Outline self, char const * filename) -> int"""

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")


        return _fitz.Outline_saveXML(self, filename)


    def saveText(self, filename):
        """saveText(Outline self, char const * filename) -> int"""

        if type(filename) == str:
            pass
        elif type(filename) == unicode:
            filename = filename.encode('utf8')
        else:
            raise TypeError("filename must be a string")


        return _fitz.Outline_saveText(self, filename)

    __swig_destroy__ = _fitz.delete_Outline
    __del__ = lambda self: None
Outline_swigregister = _fitz.Outline_swigregister
Outline_swigregister(Outline)

LINK_NONE = _fitz.LINK_NONE
LINK_GOTO = _fitz.LINK_GOTO
LINK_URI = _fitz.LINK_URI
LINK_LAUNCH = _fitz.LINK_LAUNCH
LINK_NAMED = _fitz.LINK_NAMED
LINK_GOTOR = _fitz.LINK_GOTOR
class linkDest(_object):
    """Proxy of C fz_link_dest_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, linkDest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, linkDest, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["kind"] = _fitz.linkDest_kind_get
    if _newclass:
        kind = _swig_property(_fitz.linkDest_kind_get)

    def _getPage(self):
        """_getPage(linkDest self) -> int"""
        return _fitz.linkDest__getPage(self)


    def _getDest(self):
        """_getDest(linkDest self) -> char *"""
        return _fitz.linkDest__getDest(self)


    def _getFlags(self):
        """_getFlags(linkDest self) -> int"""
        return _fitz.linkDest__getFlags(self)


    def _getLt(self):
        """_getLt(linkDest self) -> Point"""
        return _fitz.linkDest__getLt(self)


    def _getRb(self):
        """_getRb(linkDest self) -> Point"""
        return _fitz.linkDest__getRb(self)


    def _getFileSpec(self):
        """_getFileSpec(linkDest self) -> char *"""
        return _fitz.linkDest__getFileSpec(self)


    def _getNewWindow(self):
        """_getNewWindow(linkDest self) -> int"""
        return _fitz.linkDest__getNewWindow(self)


    def _getUri(self):
        """_getUri(linkDest self) -> char *"""
        return _fitz.linkDest__getUri(self)


    def _getIsMap(self):
        """_getIsMap(linkDest self) -> int"""
        return _fitz.linkDest__getIsMap(self)


    def _getIsUri(self):
        """_getIsUri(linkDest self) -> int"""
        return _fitz.linkDest__getIsUri(self)


    def _getNamed(self):
        """_getNamed(linkDest self) -> char *"""
        return _fitz.linkDest__getNamed(self)

    __swig_destroy__ = _fitz.delete_linkDest
    __del__ = lambda self: None

    page = property(_getPage)
    dest = property(_getDest)
    flags = property(_getFlags)
    lt = property(_getLt)
    rb = property(_getRb)
    fileSpec = property(_getFileSpec)
    newWindow = property(_getNewWindow)
    uri = property(_getUri)
    isMap = property(_getIsMap)
    isUri = property(_getIsUri)
    named = property(_getNamed)

linkDest_swigregister = _fitz.linkDest_swigregister
linkDest_swigregister(linkDest)


def _fz_transform_point(point, transform):
    """_fz_transform_point(Point point, Matrix transform) -> Point"""
    return _fitz._fz_transform_point(point, transform)
class Point(_object):
    """Proxy of C fz_point_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _fitz.Point_x_set
    __swig_getmethods__["x"] = _fitz.Point_x_get
    if _newclass:
        x = _swig_property(_fitz.Point_x_get, _fitz.Point_x_set)
    __swig_setmethods__["y"] = _fitz.Point_y_set
    __swig_getmethods__["y"] = _fitz.Point_y_get
    if _newclass:
        y = _swig_property(_fitz.Point_y_get, _fitz.Point_y_set)

    def __init__(self, *args):
        """
        __init__(fz_point_s self) -> Point
        __init__(fz_point_s self, Point q) -> Point
        __init__(fz_point_s self, float x, float y) -> Point
        """
        this = _fitz.new_Point(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def transform(self, m):
        _fitz._fz_transform_point(self, m)
        return self

    def __len__(self):
        return 2

    def __repr__(self):
        return "fitz.Point" + str((self.x, self.y))

    __swig_destroy__ = _fitz.delete_Point
    __del__ = lambda self: None
Point_swigregister = _fitz.Point_swigregister
Point_swigregister(Point)

LINK_FLAG_L_VALID = _fitz.LINK_FLAG_L_VALID
LINK_FLAG_T_VALID = _fitz.LINK_FLAG_T_VALID
LINK_FLAG_R_VALID = _fitz.LINK_FLAG_R_VALID
LINK_FLAG_B_VALID = _fitz.LINK_FLAG_B_VALID
LINK_FLAG_FIT_H = _fitz.LINK_FLAG_FIT_H
LINK_FLAG_FIT_V = _fitz.LINK_FLAG_FIT_V
LINK_FLAG_R_IS_ZOOM = _fitz.LINK_FLAG_R_IS_ZOOM
class Link(_object):
    """Proxy of C fz_link_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Link, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Link, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["rect"] = _fitz.Link_rect_get
    if _newclass:
        rect = _swig_property(_fitz.Link_rect_get)
    __swig_getmethods__["dest"] = _fitz.Link_dest_get
    if _newclass:
        dest = _swig_property(_fitz.Link_dest_get)
    __swig_destroy__ = _fitz.delete_Link
    __del__ = lambda self: None

    def _getNext(self):
        """_getNext(Link self) -> Link"""
        val = _fitz.Link__getNext(self)

        if val:
            val.thisown = True


        return val


    next = property(_getNext)

Link_swigregister = _fitz.Link_swigregister
Link_swigregister(Link)

class DisplayList(_object):
    """Proxy of C fz_display_list_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DisplayList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DisplayList, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(fz_display_list_s self) -> DisplayList"""
        this = _fitz.new_DisplayList()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_DisplayList
    __del__ = lambda self: None

    def run(self, dw, m, area):
        """run(DisplayList self, Device dw, Matrix m, Rect area) -> int"""
        return _fitz.DisplayList_run(self, dw, m, area)

DisplayList_swigregister = _fitz.DisplayList_swigregister
DisplayList_swigregister(DisplayList)

class TextSheet(_object):
    """Proxy of C fz_stext_sheet_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextSheet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TextSheet, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(fz_stext_sheet_s self) -> TextSheet"""
        this = _fitz.new_TextSheet()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_TextSheet
    __del__ = lambda self: None
TextSheet_swigregister = _fitz.TextSheet_swigregister
TextSheet_swigregister(TextSheet)

class TextPage(_object):
    """Proxy of C fz_stext_page_s struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextPage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TextPage, name)
    __repr__ = _swig_repr
    __swig_setmethods__["len"] = _fitz.TextPage_len_set
    __swig_getmethods__["len"] = _fitz.TextPage_len_get
    if _newclass:
        len = _swig_property(_fitz.TextPage_len_get, _fitz.TextPage_len_set)

    def __init__(self):
        """__init__(fz_stext_page_s self) -> TextPage"""
        this = _fitz.new_TextPage()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fitz.delete_TextPage
    __del__ = lambda self: None

    def search(self, needle, hit_max=16):
        """search(TextPage self, char const * needle, int hit_max=16) -> Rect"""
        return _fitz.TextPage_search(self, needle, hit_max)


    def extractText(self):
        """extractText(TextPage self) -> struct fz_buffer_s *"""
        return _fitz.TextPage_extractText(self)


    def extractXML(self):
        """extractXML(TextPage self) -> struct fz_buffer_s *"""
        return _fitz.TextPage_extractXML(self)


    def extractHTML(self):
        """extractHTML(TextPage self) -> struct fz_buffer_s *"""
        return _fitz.TextPage_extractHTML(self)


    def extractJSON(self):
        """extractJSON(TextPage self) -> struct fz_buffer_s *"""
        return _fitz.TextPage_extractJSON(self)

TextPage_swigregister = _fitz.TextPage_swigregister
TextPage_swigregister(TextPage)

# This file is compatible with both classic and new-style classes.


