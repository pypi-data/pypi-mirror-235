import shutil
from typing import Optional, Union
from stdio import write, deleteline, skipline


class Loader:
    def __init__(self,
                 min_progress: int = 0,
                 max_progress: int = 100,
                 current_progress: Optional[int] = None,
                 scale: Union[int, str] = "auto",
                 pre_string: str = "progress_total_number",
                 fill_string: str = "█",
                 empty_string: str = " ",
                 border_string: str = ""
                 ):
        self.min_progress = min_progress
        self.max_progress = max_progress
        self.current_progress = min_progress if current_progress is None else current_progress
        self.scale = scale

        self.pre_string = pre_string
        self.fill_string = fill_string
        self.empty_string = empty_string
        self.border_string = border_string

        skipline()
        self.render()

    def progress(self, current_progress):
        self.current_progress = current_progress

        self.render()

    def increase(self, increment):
        self.current_progress += increment

        self.render()

    def render(self):
        if self.current_progress < self.min_progress:
            self.current_progress = self.min_progress
        elif self.current_progress > self.max_progress:
            self.current_progress = self.max_progress

        if self.pre_string == "progress_number":
            pre_string = f"{self.current_progress}/{self.max_progress} {self.border_string}"
        elif self.pre_string == "progress_total_number":
            pre_string = f"{self.current_progress}/{self.max_progress} {self.border_string}"
        else:
            pre_string = f"{self.pre_string}{self.border_string}"

        terminal_size = shutil.get_terminal_size().columns

        scale = terminal_size - \
            len(pre_string +
                self.border_string) if self.scale == "auto" else self.scale

        scale_progress = ((self.current_progress - self.min_progress)
                          * scale) / (self.max_progress - self.min_progress)

        deleteline()
        skipline()

        write(pre_string)

        for i in range(scale):
            if i < scale_progress:
                write(self.fill_string)
            else:
                write(self.empty_string)

        write(self.border_string)
