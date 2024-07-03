from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file :Path
    unzip_dir :Path

# class DataIngestionConfig:
#     def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
#         self.root_dir = root_dir
#         self.source_URL = source_URL
#         self.local_data_file = local_data_file
#         self.unzip_dir = unzip_dir
