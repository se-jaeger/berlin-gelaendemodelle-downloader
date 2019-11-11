import os
import click

from tqdm import tqdm

from .download import get_subset_links, download_zip
from .file import fix_file_names, write_file_content
from .utils import file_content_2_data_frame, create_directories, compress_data_frame, data_frame_2_file_content
from .constant import COMPRESS_HELP, KEEP_ORIGIGNAL_HELP, COMPRESS_DEFAULT, SUPPORTED_FILE_FORMATS_DEFAULT, SUPPORTED_FILE_FORMATS_HELP, SUPPORTED_FILE_FORMATS_CHOICE


@click.group()
def cli():
    """
    Entrypoint of CLI implementation.
    """


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument("download_path", type=click.Path(exists=True, dir_okay=True, writable=True))
@click.option("--keep-original", type=bool, is_flag=True, help=KEEP_ORIGIGNAL_HELP)
@click.option("--compress", type=int, default=COMPRESS_DEFAULT, help=COMPRESS_HELP)
@click.option("--file-format", type=click.Choice(SUPPORTED_FILE_FORMATS_CHOICE, case_sensitive=False), help=SUPPORTED_FILE_FORMATS_HELP, multiple=True)
def download(download_path: str, keep_original: bool, compress: int, file_format: tuple):

    # creats all necessary directories
    original_path, compressed_path = create_directories(download_path, keep_original)
    links = get_subset_links()

    # Without compression: download and keep the original files.
    if compress <= 0:
        for link in tqdm(links):

            file_name, file_content = download_zip(link)
            write_file_content(original_path, file_name, file_content)

        fix_file_names(download_path)


    # With compression: download and compress the data. Only save the originals it ``--keep-original`` is set.
    elif 2000 % compress == 0:
        for link in tqdm(links):

            file_name, file_content = download_zip(link)

            if keep_original:
                write_file_content(original_path, file_name, file_content)

            data_frame = file_content_2_data_frame(file_content)
            compressed_data_frame = compress_data_frame(data_frame, compress)

            file_content_compressed = data_frame_2_file_content(compressed_data_frame)
            write_file_content(compressed_path, file_name, file_content_compressed)

        fix_file_names(download_path)


    else:
        raise click.BadParameter("Argument 'compress' have to divide 2000 without remainder.")
