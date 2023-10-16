from typing import Optional, List
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class R34Post:
    data: Optional[dict]
    preview_url: Optional[str]
    sample_url: Optional[str]
    file_url: Optional[str]
    file_type: Optional[str]  # new
    directory: Optional[int]
    hash: Optional[str]
    width: Optional[int]
    height: Optional[int]
    id: Optional[int]
    # image: Optional[str]
    change: Optional[int]
    owner: Optional[str]
    # parent_id: Union[str, int]
    rating: Optional[str]
    # sample
    # sample_height
    # sample_width
    score: Optional[int]
    tags: List[str]
    # source
    # status
    # has_notes
    # comment_count

    @staticmethod
    def from_json(json):
        pFileUrl = json["file_url"]
        file_type = "video" if pFileUrl.endswith(".mp4") else "gif" if pFileUrl.endswith(".gif") else "image"

        return R34Post(
            json,
            json["preview_url"],
            json["sample_url"],
            json["file_url"],
            file_type,
            json["directory"],
            json["hash"],
            json["width"],
            json["height"],
            json["id"],
            json["change"],
            json["owner"],
            json["rating"],
            json["score"],
            json["tags"].split(" ")
        )


# @dataclass(init=True, frozen=True)
# class DanbooruMediaVariants:
#     type: Optional[str]
#     url: Optional[str]
#     width: Optional[int]
#     height: Optional[int]
#     file_ext: Optional[str]
#
#     @staticmethod
#     def from_json(json):
#         return DanbooruMediasMedia(
#             json[0]["type"],
#             json[0]["url"],
#             json[0]["width"],
#             json[0]["height"],
#             json[0]["file_ext"]
#         )


@dataclass(init=True, frozen=True)
class DanbooruMediasMedia:
    data: Optional[dict]
    id: Optional[int]
    created_at: Optional[str]
    # updated_at, md5
    file_ext: Optional[str]
    file_size: Optional[int]
    image_width: Optional[int]
    image_height: Optional[int]
    # duration, status, file_key, is_public, pixel_hash
    variants: Optional[str]  # Optional[DanbooruMediaVariants]

    @staticmethod
    def from_json(json):
        return DanbooruMediasMedia(
            json,
            json["id"],
            json["created_at"],
            json["file_ext"],
            json["file_size"],
            json["image_width"],
            json["image_height"],
            json["variants"]  # DanbooruMediaVariants.from_json(json["variants"])
        )


@dataclass(init=True, frozen=True)
class DanbooruPostsPost:
    data: Optional[dict]
    id: Optional[int]
    created_at: Optional[str]
    uploader_id: Optional[int]
    score: Optional[int]
    # source, md5, last_comment_bumped_at
    rating: Optional[str]
    image_width: Optional[int]
    image_height: Optional[int]
    tag_string: Optional[str]
    # fav_count
    file_ext: Optional[str]
    # last_noted_at, parent_id, has_children, approver_id, tag_count_general, tag_count_artist, tag_count_character, tag_count_copyright, file_size, up_score, down_score, is_pending, is_flagged, is_deleted
    tag_count: Optional[int]
    updated_at: Optional[str]
    # is_banned, pixiv_id, last_commented_at, has_active_children, bit_flags, tag_count_meta, has_large, has_visible_children
    media_asset: Optional[DanbooruMediasMedia]
    tag_string_general: Optional[str]
    # tag_string_character, tag_string_copyright, tag_string_artist, tag_string_meta
    file_url: Optional[str]
    large_file_url: Optional[str]
    preview_file_url: Optional[str]

    @staticmethod
    def from_json(json):
        return DanbooruPostsPost(
            json,
            json["id"],
            json["created_at"],
            json["uploader_id"],
            json["score"],
            json["rating"],
            json["image_width"],
            json["image_height"],
            json["tag_string"],
            json["file_ext"],
            json["tag_count"],
            json["updated_at"],
            DanbooruMediasMedia.from_json(json["media_asset"]),  # json["media_asset"],
            json["tag_string_general"],
            json["file_url"],
            json["large_file_url"],
            json["preview_file_url"],
        )
