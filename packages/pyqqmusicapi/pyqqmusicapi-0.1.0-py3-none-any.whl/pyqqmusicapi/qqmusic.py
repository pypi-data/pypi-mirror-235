import json
import threading
from typing import Dict, Optional

import aiohttp

from .api.album import AlbumApi
from .api.login import Login, LoginApi
from .api.mv import MvApi
from .api.playlist import PlaylistApi
from .api.search import SearchApi
from .api.singer import SingerApi
from .api.song import SongApi
from .api.top import TopApi
from .api.user import UserApi
from .exceptions import GetQimeiFailedException, NotLoginedException, RequestException
from .qimei import Qimei
from .utils import Utils

_thread_lock = threading.Lock()


class QQMusic:
    _qimei36: Optional[str] = None
    _uid: Optional[str] = None

    album = AlbumApi
    search = SearchApi
    song = SongApi
    login = LoginApi
    top = TopApi
    mv = MvApi
    playlist = PlaylistApi
    user = UserApi
    singer = SingerApi

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(
        self,
        musicid: Optional[int] = 0,
        musickey: Optional[str] = None,
    ):
        """
        初始化QQMusic

        Args:
            musicid: musicid
            musickey: musickey
        """
        with _thread_lock:
            self._initialize(
                musicid=musicid,
                musickey=musickey,
            )

    def _initialize(self, *args, **kwargs):
        # 获取qimei36
        if not QQMusic._qimei36:
            qimei = Qimei.get()
            if not qimei.q36:
                raise GetQimeiFailedException("获取Qimei36失败")
            QQMusic._qimei36 = qimei.q36
            QQMusic._uid = Utils.random_string(10, "0123456789")

        self.musicid = kwargs.get("musicid", 0)
        self.musickey = kwargs.get("musickey", "")

        AlbumApi.parent = self
        SearchApi.parent = self
        SongApi.parent = self
        Login.parent = self
        LoginApi.parent = self
        TopApi.parent = self
        PlaylistApi.parent = self
        MvApi.parent = self
        UserApi.parent = self
        SingerApi.parent = self

    def update(self, musicid: int, musickey: str):
        """
        更新musickey

        Args:
            musicid: musicid
            musickey: musickey
        """
        with _thread_lock:
            self.musicid = musicid
            self.musickey = musickey

    async def get(self, *args, **kwargs) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.get(*args, **kwargs)

    async def post(self, *args, **kwargs) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.post(*args, **kwargs)

    async def get_data(self, module: str, method: str, param: Dict, **kwargs) -> Dict:
        # 构造公用参数
        common = {
            "ct": "11",
            "cv": "12060012",
            "v": "12060012",
            "tmeAppID": "qqmusic",
            "QIMEI36": QQMusic._qimei36,
            "uid": QQMusic._uid,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
        }

        if kwargs.get("tmeLoginMethod", None):
            common["tmeLoginMethod"] = str(kwargs.get("tmeLoginMethod", 0))

        musicid = kwargs.get("musicid", self.musicid)
        musickey = kwargs.get("musickey", self.musickey)

        if kwargs.get("need_login", False) and musicid:
            common["qq"] = str(musicid)
            common["authst"] = musickey
            if "W_X" in musickey:
                tmeLoginType = 1
            else:
                tmeLoginType = 2
        else:
            tmeLoginType = kwargs.get("tmeLoginType", 0)
        common["tmeLoginType"] = str(tmeLoginType)

        # 构造请求参数
        data = {
            "comm": common,
            "request": {
                "module": module,
                "method": method,
                "param": param,
            },
        }

        # print(json.dumps(data))

        # 格式化请求数据
        formated_data = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

        # 请求API
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://u.y.qq.com/cgi-bin/musicu.fcg",
                data=formated_data.encode("utf-8"),
            ) as response:
                res = json.loads(await response.text(kwargs.get("charset", "utf-8")))

        # 返回请求数据
        code = res["request"].get("code", 0)
        if code == 1000:
            raise NotLoginedException("QQ music token is invalid.")
        res_data = res["request"].get("data", {})
        if not res_data:
            raise RequestException("获取接口数据失败，请检查提交的数据")
        return res_data
