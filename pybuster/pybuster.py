import asyncio

from colorama import Fore, init

from tools.exceptions import BadConnectionError, CantWriteFile
from tools.buster import Buster
from tools.arguments import parse_args
from tools.loader import Loader
from tools.welcome import SNAKE, NAME, print_welcome_msg
from tools.write_to_file import write_file


async def main():
    print_welcome_msg(art=SNAKE, name=NAME)
    user_args = parse_args()
    endpoints_file = user_args.path
    website_url = user_args.link
    output_file = user_args.output

    endpoints_list = [line.strip() for line in open(endpoints_file)]
    loader = Loader(
        "Checking endpoints...", "All done (•‿•)\nLook in the output file"
    ).start()

    buster = Buster()

    urls_info = []
    partitions = [endpoints_list[i: i + 10] for i in range(0, len(endpoints_list), 10)]
    for partition in partitions:
        try:
            urls_info += await buster.get_codes(website_url, partition)
        except BadConnectionError:
            pass
    if not output_file:
        for url_info in urls_info:
            print(url_info.url, ">>>", url_info.code)
    else:
        for url_info in urls_info:
            try:
                if url_info.code == 200:
                    write_file(output_file, url_info)
            except CantWriteFile:
                print(f"Could not write to {output_file}.")
    loader.stop()


if __name__ == "__main__":
    init(autoreset=True)  # enables colorama for all platforms
    asyncio.run(main())
