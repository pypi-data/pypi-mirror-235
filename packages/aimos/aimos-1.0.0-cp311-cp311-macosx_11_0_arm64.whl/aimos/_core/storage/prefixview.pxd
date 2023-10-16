# distutils: language = c++
# cython: language_level = 3
cimport cython

from aimos._core.storage.container cimport Container
from aimos._core.storage.container cimport ContainerItemsIterator
from aimos._core.storage.containertreeview cimport ContainerTreeView

cdef class PrefixView(Container):
    cdef public bytes prefix
    # TODO cdef public Container parent after all container bindings are ready
    cdef public parent
    cdef public bint read_only

    cpdef bytes absolute_path(self, bytes path = *)
    cpdef ContainerTreeView tree(self)

cdef class PrefixViewItemsIterator(ContainerItemsIterator):
    cdef PrefixView prefix_view
    cdef bytes begin
    cdef bytes end
    cdef int prefix_len
    cdef ContainerItemsIterator it

    @cython.locals(item=tuple, keys=bytes)
    cpdef object next(self)
