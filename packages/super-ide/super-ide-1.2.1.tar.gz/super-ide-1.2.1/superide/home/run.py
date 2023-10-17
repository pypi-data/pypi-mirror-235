# Copyright (c) Mengning Software. 2023. All rights reserved.
#
# Super IDE licensed under GNU Affero General Public License v3 (AGPL-3.0) .
# You can use this software according to the terms and conditions of the AGPL-3.0.
# You may obtain a copy of AGPL-3.0 at:
#
#    https://www.gnu.org/licenses/agpl-3.0.txt
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the AGPL-3.0 for more details.

import os
from urllib.parse import urlparse
import requests
import zipfile

import click
import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_403_FORBIDDEN

from superide.compat import aio_get_running_loop
from superide.exception import SuperIDEException
from superide.home.rpc.handlers.account import AccountRPC
from superide.home.rpc.handlers.app import AppRPC
from superide.home.rpc.handlers.ide import IDERPC
from superide.home.rpc.handlers.misc import MiscRPC
from superide.home.rpc.handlers.os import OSRPC
from superide.home.rpc.handlers.piocore import PIOCoreRPC
# from superide.home.rpc.handlers.platform import PlatformRPC
from superide.home.rpc.handlers.project import ProjectRPC
from superide.home.rpc.handlers.registry import RegistryRPC
from superide.home.rpc.server import WebSocketJSONRPCServerFactory
# from superide.package.manager.core import get_core_package_dir
from superide.proc import force_exit


class ShutdownMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and b"__shutdown__" in scope.get("query_string", ""):
            await shutdown_server()
        await self.app(scope, receive, send)


async def shutdown_server(_=None):
    aio_get_running_loop().call_later(0.5, force_exit)
    return PlainTextResponse("Server has been shutdown!")


async def protected_page(_):
    return PlainTextResponse(
        "Protected superide Home session", status_code=HTTP_403_FORBIDDEN
    )


def run_server(host, port, no_open, shutdown_timeout, home_url):
    # contrib_dir = get_core_package_dir("contrib-piohome")
    contrib_dir = get_package_dir("contrib-sihome")
    if not os.path.isdir(contrib_dir):
        raise SuperIDEException("Invalid path to SuperIDE Home Contrib")

    ws_rpc_factory = WebSocketJSONRPCServerFactory(shutdown_timeout)
    ws_rpc_factory.add_object_handler(AccountRPC(), namespace="account")
    ws_rpc_factory.add_object_handler(AppRPC(), namespace="app")
    ws_rpc_factory.add_object_handler(IDERPC(), namespace="ide")
    ws_rpc_factory.add_object_handler(MiscRPC(), namespace="misc")
    ws_rpc_factory.add_object_handler(OSRPC(), namespace="os")
    ws_rpc_factory.add_object_handler(PIOCoreRPC(), namespace="core")
    ws_rpc_factory.add_object_handler(ProjectRPC(), namespace="project")
    # ws_rpc_factory.add_object_handler(PlatformRPC(), namespace="platform")
    ws_rpc_factory.add_object_handler(RegistryRPC(), namespace="registry")

    path = urlparse(home_url).path
    routes = [
        WebSocketRoute(path + "wsrpc", ws_rpc_factory, name="wsrpc"),
        Route(path + "__shutdown__", shutdown_server, methods=["POST"]),
        Mount(path, StaticFiles(directory=contrib_dir, html=True), name="static"),
    ]
    if path != "/":
        routes.append(Route("/", protected_page))

    uvicorn.run(
        Starlette(
            middleware=[Middleware(ShutdownMiddleware)],
            routes=routes,
            on_startup=[
                lambda: click.echo(
                    "SuperIDE Home has been started. Press Ctrl+C to shutdown."
                ),
                lambda: None if no_open else click.launch(home_url),
            ],
        ),
        host=host,
        port=port,
        log_level="warning",
    )

def get_package_dir(name):
  
    file_path =os.path.join(os.path.expanduser("~"), ".superide", "packages")
    package_path= os.path.join(file_path, name)

    
    if os.path.isdir(package_path):
        return package_path

    download_url = "http://139.196.184.241:8000"
    
    download_and_unzip(download_url,file_path)

    if os.path.isdir(package_path):
        return package_path  
    else:        
        return None

def download_and_unzip(url, destination_folder):
    # 发起HTTP请求并下载文件
    response = requests.get(url)
    
    # 提取文件名
    file_name = url.split("/")[-1]
    
    # 将文件保存到指定目标文件夹
    file_path = os.path.join(destination_folder, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    # 解压缩文件
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
    
    # 删除下载的压缩文件
    os.remove(file_path)
    
    print(f"已成功下载并解压文件：{file_name}")