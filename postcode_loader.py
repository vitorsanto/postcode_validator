import aiofiles


async def load_postcodes_from_file(file_path: str):
    # Loop through each CSV file and read the first column
    async with aiofiles.open(file_path, mode="r") as f:
        postcodes = {line.strip() for line in await f.readlines()}
    return postcodes
