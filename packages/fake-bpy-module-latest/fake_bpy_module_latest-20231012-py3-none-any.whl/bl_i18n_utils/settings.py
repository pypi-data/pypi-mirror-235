import sys
import typing

GenericType = typing.TypeVar("GenericType")


class I18nSettings:
    BLENDER_I18N_PO_DIR = None
    ''' '''

    BLENDER_I18N_ROOT = None
    ''' '''

    FILE_NAME_POT = None
    ''' '''

    POTFILES_SOURCE_DIR = None
    ''' '''

    PRESETS_DIR = None
    ''' '''

    PY_SYS_PATHS = None
    ''' '''

    TEMPLATES_DIR = None
    ''' '''

    WORK_DIR = None
    ''' '''

    def from_dict(self, mapping):
        ''' 

        '''
        pass

    def from_json(self, string):
        ''' 

        '''
        pass

    def load(self, fname, reset):
        ''' 

        '''
        pass

    def save(self, fname):
        ''' 

        '''
        pass

    def to_dict(self):
        ''' 

        '''
        pass

    def to_json(self):
        ''' 

        '''
        pass
