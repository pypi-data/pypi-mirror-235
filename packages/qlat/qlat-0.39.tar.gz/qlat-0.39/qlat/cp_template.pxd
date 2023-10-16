from . cimport everything as cqlat

cdef class Geometry:

    cdef cqlat.Geometry xx

    cdef readonly long cdata

cdef class PointsSelection:

    cdef cqlat.PointsSelection xx

    cdef readonly long cdata

    cdef readonly Geometry geo

    cdef readonly int view_count

cdef class FieldSelection:

    cdef cqlat.FieldSelection xx

    cdef readonly long cdata

cdef class FieldBase:

    cdef readonly long cdata

    cdef readonly int view_count

cdef class SelectedFieldBase:

    cdef readonly long cdata

    cdef readonly int view_count

    cdef public FieldSelection fsel

cdef class SelectedPointsBase:

    cdef readonly long cdata

    cdef readonly int view_count

    cdef public PointsSelection psel
