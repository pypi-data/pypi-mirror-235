import os
import requests
import time

from rich.progress import Progress, SpinnerColumn, TextColumn
from snapctl.config.hashes import CLIENT_SDK_TYPES, SERVER_SDK_TYPES, PROTOS_TYPES
from snapctl.types.definitions import ResponseType
from snapctl.utils.echo import error, success, info
from sys import platform
from typing import Union

class Snapend:
  SUBCOMMANDS = ['download', 'update', 'state']
  DOWNLOAD_TYPES = ['client-sdk', 'server-sdk', 'protos']
  BLOCKING_CALL_SLEEP = 5
  MAX_BLOCKING_RETRIES = 24

  def __init__(self, subcommand: str, base_url: str, api_key: str, snapend_id: str, category: str, platform: str, path: Union[str, None], snaps: Union[str, None], byosnaps: Union[str, None], byogs: Union[str, None], blocking: bool = False) -> None:
    self.subcommand: str = subcommand
    self.base_url: str = base_url
    self.api_key: str = api_key
    self.snapend_id: str = snapend_id
    self.category: str = category
    self.download_types: Union[dict[str, dict[str, str]], None] = Snapend._make_download_type(category)
    self.platform: str = platform
    self.path: Union[str, None] = path
    self.snaps: Union[str, None] = snaps
    self.byosnap_list: Union[list, None] = Snapend._make_byosnap_list(byosnaps) if byosnaps else None
    self.byogs_list: Union[str, None] = Snapend._make_byogs_list(byogs) if byogs else None
    self.blocking: bool = blocking

  @staticmethod
  def _make_download_type(category: str):
    if category == 'client-sdk':
      return CLIENT_SDK_TYPES
    elif category == 'server-sdk':
      return SERVER_SDK_TYPES
    elif category == 'protos':
      return PROTOS_TYPES
    return None

  @staticmethod
  def _make_byosnap_list(byosnaps: str) -> list:
    byosnap_list = []
    for byosnap in byosnaps.split(','):
      byosnap = byosnap.strip()
      if len(byosnap.split(':')) != 2:
        return []
      byosnap_list.append({
        'service_id': byosnap.split(':')[0],
        'service_version': byosnap.split(':')[1]
      })
    return byosnap_list

  @staticmethod
  def _make_byogs_list(byogs: str) -> list:
    byogs_list = []
    for byog in byogs.split(','):
      byog = byog.strip()
      if len(byog.split(':')) != 3:
        return []
      byogs_list.append({
        'fleet_name': byog.split(':')[0],
        'service_id': byog.split(':')[1],
        'service_version': byog.split(':')[2]
      })
    return byogs_list

  def _get_snapend_state(self)-> str:
    try:
      url = f"{self.base_url}/v1/snapser-api/snapends/{self.snapend_id}"
      res = requests.get(url, headers={'api-key': self.api_key})
      clusterObject = res.json()
      if 'cluster' in clusterObject and 'id' in clusterObject['cluster'] and clusterObject['cluster']['id'] == self.snapend_id and 'state' in clusterObject['cluster']:
        return clusterObject['cluster']['state']
    except Exception as e:
      pass
    return 'INVALID'

  def _blocking_get_status(self) -> bool:
    total_tries = 0
    while True:
      total_tries += 1
      if total_tries > Snapend.MAX_BLOCKING_RETRIES:
        error(f"Goign past maximum tries. Exiting...")
        return False
      current_state = self._get_snapend_state()
      if current_state == 'INVALID':
        error(f"Unable to get the snapend state. Exiting...")
        return False
      if current_state == 'LIVE':
        success('Updated your snapend. Your snapend is Live.')
        return True
      info('Current snapend state is ' + current_state)
      info(f"Retrying in {Snapend.BLOCKING_CALL_SLEEP} seconds...")
      time.sleep(Snapend.BLOCKING_CALL_SLEEP)


  def validate_input(self) -> ResponseType:
    response: ResponseType = {
      'error': True,
      'msg': '',
      'data': []
    }
    # Check subcommand
    if not self.subcommand in Snapend.SUBCOMMANDS:
      response['msg'] = f"Invalid command. Valid commands are {', '.join(Snapend.SUBCOMMANDS)}."
      return response
    # Check sdk-download commands
    if self.subcommand == 'download':
      if self.category not in Snapend.DOWNLOAD_TYPES:
        response['msg'] = f"Invalid SDK category. Valid categories are {', '.join(Snapend.DOWNLOAD_TYPES)}."
        return response
      if self.download_types is None:
        response['msg'] = f"Invalid Download type."
        return response
      # Check file path
      if self.path and not os.path.isdir(f"{self.path}"):
        response['msg'] = f"Invalid path {self.path}. Please enter a valid path to save your SDK"
        return response
    elif self.subcommand == 'update':
      byosnap_present = True
      if self.byosnap_list is None or len(self.byosnap_list) == 0:
        byosnap_present = False
      byogs_present = True
      if self.byogs_list is None or len(self.byogs_list) == 0:
        byogs_present = False
      if not byosnap_present and not byogs_present:
        response['msg'] = f"The update command needs one of byosnaps or byogs"
        return response
    # Send success
    response['error'] = False
    return response

  def download(self) -> bool:
    with Progress(
      SpinnerColumn(),
      TextColumn("[progress.description]{task.description}"),
      transient=True,
    ) as progress:
      progress.add_task(description=f'Downloading your Custom {self.category}...', total=None)
      try:
        url = f"{self.base_url}/v1/snapser-api/snapends/{self.snapend_id}/download?category={self.category}&type={self.download_types[self.platform]['type']}&subtype={self.download_types[self.platform]['subtype']}"
        if self.snaps:
          url += f"&snaps={self.snaps}"
        res = requests.get(url, headers={'api-key': self.api_key})
        file_name = f"snapser-{self.snapend_id}-{self.category}-{self.platform}.zip"
        file_path_symbol = '/'
        if platform == 'win32':
          file_path_symbol = '\\'
        sdk_save_path = f"{self.path}{file_path_symbol}{file_name}" if self.path is not None else f"{os.getcwd()}{file_path_symbol}{file_name}"
        if res.ok:
          with open(sdk_save_path, "wb") as file:
            file.write(res.content)
          success(f"SDK saved at {sdk_save_path}")
          return True
        error(f'Unable to download your custom SDK')
      except Exception as e:
        error("Exception: Unable to download the SDK")
      return False

  def update(self) -> bool:
    with Progress(
      SpinnerColumn(),
      TextColumn("[progress.description]{task.description}"),
      transient=True,
    ) as progress:
      progress.add_task(description=f'Updating your Snapend...', total=None)
      try:
        payload = {
          'byosnap_updates': self.byosnap_list,
          'byogs_updates': self.byogs_list
        }
        url = f"{self.base_url}/v1/snapser-api/snapends/{self.snapend_id}"
        res = requests.patch(url, json=payload, headers={'api-key': self.api_key})
        if res.ok:
          if self.blocking:
            return self._blocking_get_status()
          success('Snapend update has been initiated. You can check the status using `snapctl snapend state`')
          return True
        else:
          response_json = res.json()
          error(response_json['details'][0])
      except Exception as e:
        error(e.message)
        error("Exception: Unable to update your snapend")
      return False

  def state(self) -> bool:
    with Progress(
      SpinnerColumn(),
      TextColumn("[progress.description]{task.description}"),
      transient=True,
    ) as progress:
      progress.add_task(description=f'Getting your Snapend state...', total=None)
      current_state = self._get_snapend_state()
      if current_state != 'INVALID':
        success('Current snapend state is: ' + current_state)
        return True
      error(f"Unable to get the snapend state.")
      return False

