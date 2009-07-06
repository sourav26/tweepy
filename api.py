import base64

from binder import bind_api
from parsers import *
from models import User, Status

"""Twitter API"""
class API(object):

  def __init__(self, username=None, password=None, host='twitter.com', secure=False,
                classes={'user': User, 'status': Status}):
    if username and password:
      self._b64up = base64.b64encode('%s:%s' % (username, password))
    else:
      self._b64up = None
    self.host = host
    self.secure = secure
    self.classes = classes

    if username:
      self.me = self.get_user(screen_name=username)

  """Get public timeline"""
  public_timeline = bind_api(
      path = '/statuses/public_timeline.json',
      parser = parse_statuses,
      allowed_param = []
  )

  """Get friends timeline"""
  friends_timeline = bind_api(
      path = '/statuses/friends_timeline.json',
      parser = parse_statuses,
      allowed_param = ['since_id', 'max_id', 'count', 'page'],
      require_auth = True
  )

  """Get user timeline"""
  user_timeline = bind_api(
      path = '/statuses/user_timeline.json',
      parser = parse_statuses,
      allowed_param = ['id', 'user_id', 'screen_name', 'since_id',
                        'max_id', 'count', 'page']
  )

  """Get mentions"""
  mentions = bind_api(
      path = '/statuses/mentions.json',
      parser = parse_statuses,
      allowed_param = ['since_id', 'max_id', 'count', 'page'],
      require_auth = True
  )

  """Show status"""
  get_status = bind_api(
      path = '/statuses/show.json',
      parser = parse_status,
      allowed_param = ['id']
  )

  """Update status"""
  update_status = bind_api(
      path = '/statuses/update.json',
      method = 'POST',
      parser = parse_status,
      allowed_param = ['status', 'in_reply_to_status_id'],
      require_auth = True
  )

  """Destroy status"""
  destroy_status = bind_api(
      path = '/statuses/destroy.json',
      method = 'DELETE',
      parser = parse_status,
      allowed_param = ['id'],
      require_auth = True
  )

  """Show user"""
  get_user = bind_api(
      path = '/users/show.json',
      parser = parse_user,
      allowed_param = ['id', 'user_id', 'screen_name']
  )

  """Show friends"""
  friends = bind_api(
      path = '/statuses/friends.json',
      parser = parse_users,
      allowed_param = ['id', 'user_id', 'screen_name', 'page']
  )

  """Show followers"""
  followers = bind_api(
      path = '/statuses/followers.json',
      parser = parse_users,
      allowed_param = ['id', 'user_id', 'screen_name', 'page'],
      require_auth = True
  )

api = API('jitterapp', 'josh1987')
