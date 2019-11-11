
## CLI constants

COMPRESS_HELP               = "Indicates how many tiles should be compressed to one.\b\n-> 0 means no compression and automatically keeps the original ones.\n-> 2000 have to be divisible by this without remainder."
KEEP_ORIGIGNAL_HELP         = "Indicates whether to keep the original files or not."
SUPPORTED_FILE_FORMATS_HELP = "File formats that can be used to store the downloaded data. Case insensitive values"

COMPRESS_DEFAULT = 0

SUPPORTED_FILE_FORMATS_DEFAULT  = ["txt"]
SUPPORTED_FILE_FORMATS_CHOICE   = ["txt"] # TODO: GeoJson, CSV


## Path constants

ORIGNAL_SUB_PATH    = "original"
COMPRESSED_SUB_PATH = "compressed"



DATA_URL = "https://fbinter.stadt-berlin.de/fb/berlin/service_intern.jsp?id=a_dgm@senstadt&type=FEED"
