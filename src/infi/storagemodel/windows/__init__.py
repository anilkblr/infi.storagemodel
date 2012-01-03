
from infi.pyutils.lazy import cached_method, cached_property, clear_cache, LazyImmutableDict
from ..base import StorageModel, scsi, multipath, disk
from contextlib import contextmanager

# pylint: disable=W0212,E1002

class WindowsDiskModel(disk.DiskModel):
    pass

# TODO
# mount manager
# mount repository

class WindowsStorageModel(StorageModel):
    def _create_disk_model(self):
        return WindowsDiskModel()

    def _create_scsi_model(self):
        from .scsi import WindowsSCSIModel
        return WindowsSCSIModel()

    def _create_native_multipath_model(self):
        from .native_multipath import WindowsNativeMultipathModel
        return WindowsNativeMultipathModel()

    def initiate_rescan(self):
        from infi.devicemanager import DeviceManager
        dm = DeviceManager()
        for controller in dm.storage_controllers:
            if not controller.is_real_device():
                continue
            controller.rescan()
