import sys

def error_msg_details(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occurred in Python script name [{file_name}] at line number [{exc_tb.tb_lineno}] with error message: {error}"
    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_details(error_msg, error_detail)

    def __str__(self):
        return self.error_msg
