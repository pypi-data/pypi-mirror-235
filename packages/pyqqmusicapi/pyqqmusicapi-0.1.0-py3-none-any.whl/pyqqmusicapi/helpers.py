from typing import Any, Dict, List


class Helpers:
    @staticmethod
    def ensure_list(value: Any) -> List:
        if isinstance(value, list):
            return value
        else:
            return [value] if value else []

    @staticmethod
    def parse_song_info(song_info) -> Dict:
        # 解析歌曲信息
        info = {
            "id": song_info["id"],
            "mid": song_info["mid"],
            "name": song_info["name"],
            "title": song_info["title"],
            "subTitle": song_info.get("subtitle", ""),
            "language": song_info["language"],
            "timePublic": song_info.get("time_public", ""),
            "tag": song_info.get("tag", ""),
            "type": song_info["type"],
        }

        # 解析专辑信息
        album = {
            "id": song_info["album"]["id"],
            "mid": song_info["album"]["mid"],
            "name": song_info["album"]["name"],
            "timePublic": song_info["album"].get("time_public", ""),
        }

        # 解析MV信息
        mv = {
            "id": song_info["mv"]["id"],
            "name": song_info["mv"].get("name", ""),
            "vid": song_info["mv"]["vid"],
        }

        # 解析歌手信息
        singer = [
            {
                "id": s["id"],
                "mid": s["mid"],
                "name": s["name"],
                "type": s.get("type"),
                "uin": s.get("uin"),
            }
            for s in song_info["singer"]
        ]

        # 解析文件信息
        file = {
            "mediaMid": song_info["file"]["media_mid"],
            "AI00": song_info["file"]["size_new"][0],
            "Q000": song_info["file"]["size_new"][1],
            "Q001": song_info["file"]["size_new"][2],
            "F000": song_info["file"]["size_flac"],
            "O600": song_info["file"]["size_192ogg"],
            "O400": song_info["file"]["size_96ogg"],
            "M800": song_info["file"]["size_320mp3"],
            "M500": song_info["file"]["size_128mp3"],
            "C600": song_info["file"]["size_192aac"],
            "C400": song_info["file"]["size_96aac"],
            "C200": song_info["file"]["size_48aac"],
        }

        # 组装结果
        result = {
            "info": info,
            "album": album,
            "mv": mv,
            "singer": singer,
            "file": file,
            "lyric": {
                "match": song_info.get("lyric", ""),
                "content": song_info.get("content", ""),
            },
            "pay": song_info.get("pay", {}),
            "grp": [Helpers.parse_song_info(song) for song in song_info.get("grp", [])],
            "vs": song_info.get("vs", []),
        }

        return result

    @staticmethod
    def filter_data(data: Dict) -> Dict:
        keys = [
            "relainfo",
            "identity",
            "iconurl",
            "page_rank",
            "settleIn",
            "is_intervene",
            "isFollow",
            "pic_icon",
            "hotness",
            "audio_play",
            "hotness_desc",
            "smallIcons",
            "pay",
            "notplay",
            "new_video_switch",
            "msg",
            "mid_desc",
            "auto_play",
            "watchtype",
            "watchid",
            "video_switch",
            "video_pay",
            "pmid",
            "track_id",
        ]
        for key in keys:
            data.pop(key, "")
        return data

    @staticmethod
    def singer_to_str(data: Dict):
        return "&".join([singer["name"] for singer in data["singer"]])

    @staticmethod
    def split_list(lst: List, chunk_size: int) -> List:
        return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]

    @staticmethod
    def search_song(songs: List[Dict], mid: str) -> Dict:
        return next(filter(lambda x: x["info"]["mid"] == mid, songs), {})
