import aiohttp
from typing import Iterable, ClassVar, Union

from .objects import *


# __base_url__ = "https://rule34.xxx/"
# __api_url__ = "https://api.rule34.xxx/"
# SEARCH = f"{__api_url__}index.php?page=dapi&s=post&q=index&limit={{LIMIT}}&tags={{TAGS}}&json=1"  # returns: JSON
# GET_POST = f"{__api_url__}index.php?page=dapi&s=post&q=index&id={{POST_ID}}&json=1"  # returns: JSON
# POOL = f"{__api_url__}index.php?page=pool&s=show&id={{POOL_ID}}"  # returns: HTML
# COMMENTS = f"{__api_url__}index.php?page=dapi&s=comment&q=index&post_id={{POST_ID}}"  # returns: XML
#
# USER_FAVORITES = f"{__api_url__}index.php?page=favorites&s=view&id={{USR_ID}}"  # returns: HTML
# USER_PAGE = f"{__api_url__}index.php?page=account&s=profile&id={{USER_ID}}"  # returns: HTML
#
# ICAME = f"{__base_url__}index.php?page=icame"  # returns: HTML
# RANDOM_POST = f"{__base_url__}index.php?page=post&s=random"  # returns: HTML
# TOPMAP = f"{__base_url__}index.php?page=toptags"
# STATS = f"{__base_url__}index.php?page=stats"  # returns: HTML


class AsyncRule34:
    BASE_API_URL: ClassVar[str] = "https://api.rule34.xxx/index.php?page=dapi&q=index&json=1"

    def __init__(self):
        """
        Asynchronous rule34.xxx wrapper
        """
        self.session = aiohttp.ClientSession()
        self.url = AsyncRule34.BASE_API_URL

    async def search(
            self,
            tags: Iterable[str],
            *,
            exclude_tags: Iterable[str] = None,
            limit: Optional[int] = 100,
            page_id: Optional[int] = 0,
            random: Optional[bool] = False
    ) -> list[R34Post]:
        """
        Searches rule34.xxx with specified inclusion and exclusion tags.

        :param tags: The include tags
        :param exclude_tags: The exclude tags
        :param limit: The (maximum) number of posts to grab
        :param page_id: The page number of search results
        :param random: Whether to return random posts with the tags.
        :return: A tuple of returned posts
        """
        if random:
            tags = list(tags) + ['sort:random']

        url = self.url + '&tags=' + self._format_tags(tags, exclude_tags) + f'&limit={limit}&s=post'

        if page_id:
            url += f"&pid={page_id}"

        async with self.session.get(url) as response:
            json = (await response.json())

        if json is None:
            return []

        return list([R34Post.from_json(post) for post in json])

    async def get_posts(
            self,
            posts_id: Optional[Union[list, int]],
            md5: Optional[str] = None
    ) -> List[R34Post]:
        """
        Get a post(as) either by ID or md5 hash

        :param posts_id: The id(s) of the post to get
        :param md5: The md5 hash of the post
        :return: A tuple that contains the post / matching posts.
        :raises ValueError: If there is not a post id or an md5 hash, or there is both
        """
        if isinstance(posts_id, int):
            posts_id = [posts_id]

        if (posts_id and md5) or (not posts_id and not md5):
            raise ValueError("Must specify a post id or an md5, and not both.")

        posts = []

        for post_id in posts_id:
            url = (self.url + (f'&tags=md5:{md5}' if md5 else f'&id={post_id}')) + '&s=post'
            async with self.session.get(url) as response:
                for post in await response.json():
                    res = R34Post.from_json(post)
                    posts.extend(["The md5 of the post does not match the assigned md5"] if md5 and res.md5 != md5 else list([res]))

        return posts

    async def get_random_post(self) -> R34Post:
        async with self.session.get("https://rule34.xxx/index.php?page=post&s=random") as response:
            print(await response.json())
            return R34Post.from_json((await response.json())[0])

    @staticmethod
    def _format_tags(include_tags: Iterable[str], exclude_tags: Iterable[str] = None) -> str:
        """

        :param include_tags:
        :param exclude_tags:
        :return: include tags + exclude tags
        """
        include = '+'.join(tag.strip().lower().replace(' ', '_') for tag in include_tags)
        exclude = '+'.join('-' + tag.strip().lstrip('-').lower().replace(' ', '_') for tag in exclude_tags) if exclude_tags else ''
        return include + '+' + exclude

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def close(self):
        await self.session.close()


class DanbooruBaseMin(Exception):
    def __init__(self):
        """
        danbooru.donmai.us API wrapper
        """

    # @staticmethod
    async def random_post(self) -> DanbooruPostsPost:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://testbooru.donmai.us/posts/random.json") as response:  # ?rating=s
                return DanbooruPostsPost.from_json(await response.json())
