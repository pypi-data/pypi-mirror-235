import inspect
import os
from .models import LoggerFrame


def merge_dicts(base_dict: dict, update_dict: dict) -> dict:
    """
    Recursively merge update_dict into base_dict.
    All keys in base_dict will be overwritten if they are in update_dict

    :param base_dict:
    :param update_dict:
    :return:
    """
    base_dict = base_dict.copy()
    for key, value in update_dict.items():
        if isinstance(value, dict):
            base_dict[key] = merge_dicts(base_dict.get(key, {}), value)
        else:
            base_dict[key] = value
    return base_dict


def calculate_frame(before: str = None, index: int = 2, before_strict: bool = False) -> LoggerFrame:
    """
        Calculate information about a frame in the call stack.

        This function returns details about a specific frame in the call stack using the `inspect` module.

        Parameters:
        - before (str): The name of the frame to look for in the call stack.
        - index (int): The index of the frame to retrieve (default is 2).
        - before_strict (bool): If True, match the frame name strictly; if False, partial matches are allowed.

        Returns:
        - LoggerFrame: An object containing frame information.

        Example:
        frame_info = calculate_frame(before="my_function", before_strict=True)
        print(frame_info.file_name, frame_info.line_number)

        """
    if before is None:
        index = index if index is not None else 2
        frame_info = inspect.stack()[index]
        try:
            frame_before = inspect.stack()[index + 1]
            fb_string = f"{frame_before.frame.f_globals.get('__name__')}.{frame_before.frame.f_code.co_qualname}::" \
                        f"{os.path.basename(frame_before.filename)}:{frame_before.lineno}"
        except IndexError:
            fb_string = None
        return LoggerFrame(
            function=frame_info.frame.f_code.co_qualname,
            module=frame_info.frame.f_globals.get("__name__"),
            line_number=frame_info.lineno,
            file_name=frame_info.filename,
            frame_before=fb_string,
            is_exception=False
        )
    elif before is not None:
        # TODO: Improve with lets say a tuple containing both class and function.
        on_next = False
        index = 0
        for frame_info in inspect.stack():
            if on_next:
                frame_before = inspect.stack()[index-1]
                fb_string = (f"{frame_before.frame.f_globals.get('__name__')}."
                             f"{frame_before.frame.f_code.co_qualname}::"
                             f"{os.path.basename(frame_before.filename)}:{frame_before.lineno}")
                return LoggerFrame(
                    function=frame_info.frame.f_code.co_qualname,
                    module=frame_info.frame.f_globals.get("__name__"),
                    line_number=frame_info.lineno,
                    file_name=frame_info.filename,
                    frame_before=fb_string,
                    is_exception=False
                )

            # Check if before is the frame name or when non-strict before is in the frame name set on_next to True.
            if (
                    before == frame_info.frame.f_code.co_qualname or (
                    not before_strict and before in frame_info.frame.f_code.co_qualname)
            ):
                on_next = True

            index += 1
