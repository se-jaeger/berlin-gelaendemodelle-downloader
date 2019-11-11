
import os

## CLI constants

SUPPORTED_FILE_FORMATS_HELP = "File formats that can be used to store the compressed data."
COMPRESS_HELP               = "Indicates how many tiles should be compressed to one.\b\n-> 0 means no compression and automatically keeps the original ones.\n-> 2000 have to be divisible by this without remainder."
KEEP_ORIGIGNAL_HELP         = "Indicates whether to keep the original files."


## Path constants

ORIGNAL_SUB_PATH    = "original"
COMPRESSED_SUB_PATH = "compressed"



DATA_URL = "https://fbinter.stadt-berlin.de/fb/berlin/service_intern.jsp?id=a_dgm@senstadt&type=FEED"