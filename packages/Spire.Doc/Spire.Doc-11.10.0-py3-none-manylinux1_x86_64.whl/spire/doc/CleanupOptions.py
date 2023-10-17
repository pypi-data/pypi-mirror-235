from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CleanupOptions(SpireObject):
    """
    Represents options for cleaning up a document.
    """
    @property
    def UnusedStyles(self)->bool:
        """
        Gets the flag indicating whether unused styles should be cleaned up.
        """
        GetDllLibDoc().CleanupOptions_get_UnusedStyles.argtypes=[c_void_p]
        GetDllLibDoc().CleanupOptions_get_UnusedStyles.restype=c_bool
        ret = GetDllLibDoc().CleanupOptions_get_UnusedStyles(self.Ptr)
        return ret

    @UnusedStyles.setter
    def UnusedStyles(self, value:bool):
        """
        Sets the flag indicating whether unused styles should be cleaned up.
        """
        GetDllLibDoc().CleanupOptions_set_UnusedStyles.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CleanupOptions_set_UnusedStyles(self.Ptr, value)

    @property
    def UnusedLists(self)->bool:
        """
        Gets the flag indicating whether unused lists should be cleaned up.
        """
        GetDllLibDoc().CleanupOptions_get_UnusedLists.argtypes=[c_void_p]
        GetDllLibDoc().CleanupOptions_get_UnusedLists.restype=c_bool
        ret = GetDllLibDoc().CleanupOptions_get_UnusedLists(self.Ptr)
        return ret

    @UnusedLists.setter
    def UnusedLists(self, value:bool):
        """
        Sets the flag indicating whether unused lists should be cleaned up.
        """
        GetDllLibDoc().CleanupOptions_set_UnusedLists.argtypes=[c_void_p, c_bool]
        GetDllLibDoc().CleanupOptions_set_UnusedLists(self.Ptr, value)

