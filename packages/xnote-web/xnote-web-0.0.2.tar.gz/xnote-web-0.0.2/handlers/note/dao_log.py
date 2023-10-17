# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2021/12/29 23:48:27
# @modified 2022/07/31 21:00:41
# @filename dao_log.py

"""笔记相关的访问日志有两个部分：
1. 某个用户对某个笔记的访问记录，用于统计个人对笔记的行为倾向，
    记录在 user_note_log.visit_cnt 中

2. 所有用户对某个笔记的访问记录，用于统计群体对笔记的行为倾向，
    记录在 note_index.visit_cnt 中
"""

import xauth
import xutils
import xconfig
from xutils import dbutil
from xutils import dateutil
from xutils import Storage
from .dao_api import NoteDao
from . import dao as note_dao


NOTE_DAO = xutils.DAO("note")
MAX_EDIT_LOG = 500
MAX_VIEW_LOG = 500

def log_debug(fmt, *args):
    print(dateutil.format_time(), fmt.format(*args))

def is_debug_enabled():
    return xconfig.DEBUG

def get_user_note_log_table(user_name):
    assert user_name != None, "invalid user_name:%r" % user_name
    return dbutil.get_table("user_note_log", user_name = user_name)

class UserNoteLogDao:
    db = dbutil.get_table("user_note_log")

class NoteVisitLogDO(Storage):
    def __init__(self):
        self.note_id = 0
        self.visit_cnt = 0
        self.ctime = dateutil.format_datetime()
        self.mtime = dateutil.format_datetime()
        self.atime = dateutil.format_datetime()
        self.user = ""

@xutils.timeit_deco(name = "_update_log", switch_func = is_debug_enabled)
def _update_log(user_name, note, increment = 1, insert_only = False):
    # 部分历史数据是int类型，所以需要转换一下
    note_id = note.id
    atime = dateutil.format_datetime()
    db = UserNoteLogDao.db
    
    with dbutil.get_write_lock(user_name):
        log = db.get_by_id(note_id, user_name = user_name)
        
        # print(f"_update_log={log}")

        if log is None:
            log = NoteVisitLogDO()
            log.note_id = note_id
            log.visit_cnt  = increment
            log.atime = atime
            log.mtime = note.mtime
            log.ctime = note.ctime
            log.user = user_name
            db.put_by_id(note_id, log)
        else:
            if insert_only:
                log_debug("skip for insert_only mode, note_id:{!r}", note_id)
                return
            if log.visit_cnt is None:
                log.visit_cnt = 1
            log.visit_cnt += increment
            log.atime = atime
            log.mtime = note.mtime
            log.ctime = note.ctime
            log.user = user_name
            db.update(log)

def get_note_ids_from_logs(logs):
    return list(map(lambda x:x.note_id, logs))

@xutils.timeit(name = "NoteDao.ListRecentViewed", logfile = True, logargs = True)
def list_recent_viewed(creator = None, offset = 0, limit = 10):
    if limit is None:
        limit = xconfig.PAGE_SIZE

    user = xauth.current_name()
    if user is None:
        user = "public"

    db = get_user_note_log_table(user)
    logs = db.list_by_index("atime", offset = offset, limit = limit, reverse = True)
    atime_dict = dict()
    for log in logs:
        note_id = int(log.note_id)
        atime_dict[note_id] = log.atime
    
    # print("atime_dict", atime_dict)

    note_ids = get_note_ids_from_logs(logs)

    result = []
    note_dict = note_dao.batch_query_dict(note_ids)
    for log in logs:
        note_id = int(log.note_id)
        note_info = note_dict.get(note_id)
        if note_info != None:
            note_info.badge_info = dateutil.format_date(log.atime, "/")
            result.append(note_info)
    return result


def list_hot(user_name, offset = 0, limit = 100):
    if limit < 0:
        limit = MAX_VIEW_LOG

    db = get_user_note_log_table(user_name)
    logs = db.list_by_index("visit_cnt", 
        offset = offset, limit = limit, reverse = True)

    hot_dict = dict()
    log_dict = dict()
    for log in logs:
        try:
            note_id = int(log.note_id)
        except:
            note_id = 0

        hot_dict[note_id] = log.visit_cnt
        log_dict[note_id] = log
        
    note_ids = get_note_ids_from_logs(logs)

    result = []
    note_dict = note_dao.batch_query_dict(note_ids)
    for log in logs:
        note_id = int(log.note_id)
        note_info = note_dict.get(note_id)
        if note_info != None:
            note_info.badge_info = str(hot_dict.get(note_id))
            note_info.user_log = log_dict.get(note_id)
            result.append(note_info)

    return result

def list_most_visited(user_name, offset, limit):
    return list_hot(user_name, offset, limit)

@xutils.timeit(name = "NoteDao.ListRecentEdit:leveldb", logfile = True, logargs = True)
def list_recent_edit(user_name = None, offset = 0, limit = None, skip_deleted = True):
    """查询最近编辑的笔记"""
    if limit is None:
        limit = xconfig.PAGE_SIZE
    
    assert user_name != None
    creator_id = xauth.UserDao.get_id_by_name(user_name)
    result = []
    note_list = note_dao.NoteIndexDao.list(creator_id=creator_id, offset=offset, limit=limit, order="mtime desc")
    for note in note_list:
        note.badge_info = dateutil.format_date(note.mtime, "/")
        result.append(note)

    return result

@xutils.timeit(name = "NoteDao.ListRecentCreated", logfile = True)
def list_recent_created(user_name = None, offset = 0, limit = 10, skip_archived = False):
    if limit is None:
        limit = xconfig.PAGE_SIZE

    assert user_name != None
    creator_id = xauth.UserDao.get_id_by_name(user_name)
    result = []
    note_list = note_dao.NoteIndexDao.list(creator_id=creator_id, offset=offset, limit=limit, order="ctime desc")
    for note in note_list:
        note.badge_info = dateutil.format_date(note.ctime, "/")
        result.append(note)
    return result

def count_visit_log(user_name):
    return get_user_note_log_table(user_name).count()

def delete_visit_log(user_name, note_id):
    db = get_user_note_log_table(user_name)
    db.delete_by_id(note_id)

def add_visit_log(user_name, note):
    return _update_log(user_name, note)

def add_edit_log(user_name, note):
    return _update_log(user_name, note)

def add_create_log(user_name, note):
    return _update_log(user_name, note)

def list_recent_events(user_name = None, offset = 0, limit = xconfig.PAGE_SIZE):
    create_events = list_recent_created(user_name, offset, limit)
    edit_events = list_recent_edit(user_name, offset, limit)
    view_events = list_recent_viewed(user_name, offset, limit)

    def map_notes(notes, action):
        for note in notes:
            note.action = action
            if action == "create":
                note.action_time = note.ctime
            elif action == "edit":
                note.action_time = note.mtime
            else:
                note.action_time = note.atime

    map_notes(create_events, "create")
    map_notes(edit_events, "edit")
    map_notes(view_events, "view")

    events = create_events + edit_events + view_events
    events.sort(key = lambda x: x.action_time, reverse = True)
    return events[offset: offset + limit]

# 读操作
xutils.register_func("note.count_visit_log", count_visit_log)
xutils.register_func("note.list_recent_viewed", list_recent_viewed)
xutils.register_func("note.list_hot", list_hot)
xutils.register_func("note.list_recent_edit", list_recent_edit)
xutils.register_func("note.list_recent_created", list_recent_created)
xutils.register_func("note.list_most_visited", list_most_visited)
xutils.register_func("note.list_recent_events", list_recent_events)

# 写操作
xutils.register_func("note.add_edit_log", add_edit_log)
xutils.register_func("note.add_visit_log", add_visit_log)
xutils.register_func("note.add_create_log", add_create_log)
xutils.register_func("note.delete_visit_log", delete_visit_log)

NoteDao.delete_visit_log = delete_visit_log
