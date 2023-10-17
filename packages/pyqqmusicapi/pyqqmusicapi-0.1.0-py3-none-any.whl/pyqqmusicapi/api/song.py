from __future__ import annotations

from random import choice
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List

if TYPE_CHECKING:
    from qqmusic import QQMusic

from ..helpers import Helpers
from ..utils import Utils
from .playlist import PlaylistApi


class SongApi:
    """歌曲API"""

    parent: ClassVar[QQMusic]

    """
    文件类
    """
    FILE_TYPE = {
        "AI00": ".flac",  # size_new[0]
        "Q000": ".flac",  # size_new[1]
        "Q001": ".flac",  # size_new[2]
        "F000": ".flac",  # size_flac
        "O600": ".ogg",  # size_192ogg
        "O400": ".ogg",  # size_96ogg
        "M800": ".mp3",  # size_320mp3
        "M500": ".mp3",  # size_128mp3
        "C600": ".m4a",  # size_192aac
        "C400": ".m4a",  # size_96aac
        "C200": ".m4a",  # size_48aac
        # 试听 "RS02": ".mp3" # size_try
    }

    @staticmethod
    async def detail(mid: str) -> Dict[str, Any]:
        """
        歌曲详细信息

        Args:
            mid: 歌曲mid

        Returns:
            Dict: 歌曲信息
        """
        response = await SongApi.parent.get_data(
            module="music.pf_song_detail_svr",
            method="get_song_detail_yqq",
            param={"song_mid": mid},
        )
        response["track_info"] = Helpers.parse_song_info(response["track_info"])
        return response

    @staticmethod
    async def query(
        mid: List[str] = [],
        id: List[int] = [],
    ) -> List[Dict[str, Any]]:
        """
        根据mid或id获取歌曲信息

        Args:
            mid: 歌曲mid
            id: 歌曲id

        Returns:
            List: 歌曲信息

        Raises:
            ValueError: mid和id都为空或都不为空
        """
        # 检查参数是否有效
        if not (bool(mid) ^ bool(id)):
            raise ValueError(
                "Either mid or id should be provided, but not both or none."
            )

        # 构造请求参数
        param = {
            "ids": id or [],
            "mids": mid or [],
            "types": [0 for i in range(len(mid or id))],
            "modify_stamp": [0 for i in range(len(mid or id))],
            "ctx": 0,
            "client": 1,
        }

        # 发送请求数据
        response = await SongApi.parent.get_data(
            module="music.trackInfo.UniformRuleCtrl",
            method="CgiGetTrackInfo",
            param=param,
        )
        return [Helpers.parse_song_info(song) for song in response["tracks"]]

    @staticmethod
    async def url(
        mid: List[str], filetype: str = "M500", mode: str = "play", **kwargs
    ) -> Dict[str, Any]:
        """
        获取歌曲链接

        Args:
            mid: 歌曲mid
            filetype: 文件标识符
            mode: 获取类型
            **kwargs: musicid, musickey

        Returns:
            Dict 歌曲链接

        Raises:
            ValueError: 如果文件类型或模式类型不在预定义范围内
        """
        # 检查文件类型是否有效
        if filetype not in SongApi.FILE_TYPE:
            raise ValueError(f"Invalid filetype: {filetype}")

        # 检查模式类型是否有效
        if mode not in ["play", "download"]:
            raise ValueError(f"Invalid mode: {mode}")

        # 确保mid列表长度不大于100
        mids_list = Helpers.split_list(mid, 100)

        # 获取文件类型对应的前缀和后缀
        file_type = SongApi.FILE_TYPE[filetype]

        # 根据模式类型选择请求模块和方法
        if mode == "play":
            module = "music.vkey.GetVkey"
            method = "UrlGetVkey"
        else:
            module = "music.vkey.GetDownUrl"
            method = "CgiGetDownUrl"

        urls = {}

        for mids in mids_list:
            # 构造请求参数
            param = {
                "filename": [f"{filetype}{mid}{file_type}" for mid in mids],
                "guid": Utils.random_string(32, "abcdef1234567890"),
                "songmid": mids,
                "songtype": [1 for i in range(len(mids))],
            }

            url = choice(
                [
                    "https://isure.stream.qqmusic.qq.com/",
                    "https://ws.stream.qqmusic.qq.com/",
                    "https://dl.stream.qqmusic.qq.com/",
                ]
            )

            # 发送请求数据
            response = await SongApi.parent.get_data(
                module=module,
                method=method,
                param=param,
                need_login=1,
                **kwargs,
            )
            print(response)

            data = response["midurlinfo"]

            urls.update(
                {
                    info["songmid"]: (url + info["wifiurl"] if info["wifiurl"] else "")
                    for info in data
                }
            )

        return urls

    @staticmethod
    async def similar(id: int) -> List[Dict[str, Any]]:
        """
        相似歌曲

        Args:
            id: 歌曲ID

        Returns:
            List: 相似歌曲
        """
        response = await SongApi.parent.get_data(
            module="music.recommend.TrackRelationServer",
            method="GetSimilarSongs",
            param={"songid": id},
        )
        return [
            Helpers.parse_song_info(song["track"])
            for song in response["vecSongNew"][0]["songs"]
        ]

    @staticmethod
    async def labels(id: int) -> Dict[str, Any]:
        """
        歌曲标签

        Args:
            id: 歌曲ID

        Returns:
            Dict: 歌曲标签
        """
        response = await SongApi.parent.get_data(
            module="music.recommend.TrackRelationServer",
            method="GetSongLabels",
            param={"songid": id},
        )
        return response["labels"]

    @staticmethod
    async def other(id: int) -> List[Dict[str, Any]]:
        """
        其他版本

        Args:
            id: 歌曲ID

        Returns:
            List: 其他版本
        """
        response = await SongApi.parent.get_data(
            module="music.musichallSong.OtherVersionServer",
            method="GetOtherVersionSongs",
            param={"songID": id, "sin": 0},
        )
        return [Helpers.parse_song_info(song) for song in response["versionList"]]

    @staticmethod
    async def playlist(id: str) -> Dict[str, Any]:
        """
        相关歌单

        Args:
            id: 歌曲ID

        Returns:
            Dict: 相关歌单
        """
        response = await SongApi.parent.get_data(
            module="music.recommend.TrackRelationServer",
            method="GetRelatedPlaylist",
            param={
                "songid": id,
            },
        )
        return response["vecPlaylistNew"][0]["playlists"]

    @staticmethod
    async def mv(id: int) -> Dict[str, Any]:
        """
        相关MV

        Args:
            id: 歌曲ID

        Returns:
            Dict: 相关MV
        """
        response = await SongApi.parent.get_data(
            module="MvService.MvInfoProServer",
            method="GetSongRelatedMv",
            param={"songid": str(id), "songtype": 1, "lastmvid": 0},
        )
        return response["list"]

    @staticmethod
    async def sheet(mid: str) -> Dict[str, Any]:
        """
        相关曲谱

        Args:
            mid: 歌曲mid

        Returns:
            Dict: 相关曲谱
        """
        response = await SongApi.parent.get_data(
            module="music.mir.SheetMusicSvr",
            method="GetMoreSheetMusic",
            param={"songMid": mid, "scoreType": -1},
        )
        return response["result"]

    @staticmethod
    async def producer(id: int) -> Dict[str, Any]:
        """
        制作团队

        Args:
            id: 歌曲ID

        Returns:
            Dict: 制作团队
        """
        response = await SongApi.parent.get_data(
            module="music.sociality.KolWorksTag",
            method="SongProducer",
            param={"SongID": id, "Pos": 1, "GetFollow": 0},
        )
        return response["Lst"]

    @staticmethod
    async def collect(id: List[int], op: int = 0, **kwargs) -> bool:
        """
        收藏歌曲

        Args:
            id: 歌曲ID
            op: 0：收藏 1：取消收藏

        Returns:
            bool: 是否成功
        """
        if not op:
            response = await PlaylistApi.add(201, id, **kwargs)
        else:
            response = await PlaylistApi.remove(201, id, **kwargs)
        return response
