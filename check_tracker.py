#! /usr/bin/python3
# -*- coding: utf-8 -*-

# from bencode import bdecode, BTFailure
# from glob import glob
# import os
import transmissionrpc
import re
# import shutil
# from datetime import datetime as dt

# ======================================================================
tc = transmissionrpc.Client("192.168.1.113", 9091,"transmission", "dnTv7G3ms")
torrents = tc.get_torrents("77,306,506")
# torrents = filter(lambda t: re.match("torrents.ru", t.annonce), torrents)
for t in torrents:
    comment = re.sub("torrents\.ru", "rutracker.org", t.comment)
    if (comment):
        print(t.id, str(t.name), comment)

    # for tr in t.trackers:
    #     print("\tid - ", tr["id"])
    #     for item in tr.items():
    #         print("\t\t", str(item))
print()
# for tr in torrent.trackerStats:
#     for item in tr.items():
#         print(item)
#     print("--------")
# print("")
# ======================================================================
print("Done")
