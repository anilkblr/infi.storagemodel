from infi.instruct.buffer import Buffer, buffer_field, bytes_ref, be_uint_field, len_ref, self_ref, json_field
from infi.asi.cdb.inquiry import PeripheralDeviceDataBuffer
from infi.asi.cdb.inquiry.vpd_pages import EVPDInquiryCommand


class JSONInquiryPageBuffer(Buffer):
    peripheral_device = buffer_field(where=bytes_ref[0:], type=PeripheralDeviceDataBuffer)
    page_code = be_uint_field(where=bytes_ref[1])
    page_length = be_uint_field(where=bytes_ref[3], set_before_pack=len_ref(self_ref.json_data))
    json_data = json_field(where=bytes_ref[4:4+page_length])


class JSONInquiryPageCommand(EVPDInquiryCommand):
    def __init__(self):
        # pylint: disable=E1002
            # pylint: disable=E1002
        super(JSONInquiryPageCommand, self).__init__(0xc5, 1024, JSONInquiryPageBuffer)
