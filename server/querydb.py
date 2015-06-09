##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################

"""
This class provides an interface to pytables.
"""

import numpy as np
import tables
import os.path as op
import os
import logging


class Querydb:

    
    @staticmethod
    def getVersionInfo():
        versionInfo = {}
        versionInfo['pytables_version'] = tables.__version__
        versionInfo['hdf5_version'] = tables.hdf5Version
        return versionInfo

    def __init__(self, filePath, readonly=True, app_logger=None):
        if app_logger:
            self.log = app_logger
        else:
            self.log = logging.getLogger()
        mode = 'r'
        if readonly:
            self.readonly = True
        else:
            if os.access(filePath, os.W_OK):
                mode = 'r+'
                self.readonly = False
            else:
                self.readonly = True

        self.log.info("init -- filePath: " + filePath + " mode: " + mode)

        self.f = tables.open_file(filePath, mode)


    def __enter__(self):
        self.log.info('querydb __enter')
        return self

    def __exit__(self, type, value, traceback):
        self.log.info('querydb __exit')
        filename = self.f.filename
        self.f.flush()
        self.f.close()
        
    def doQuery(self, path, query, start=0, stop=-1, step=1, limit=None):
        print "querydb getValues - path:", path, "query:", query
        print "limit:", limit, type(limit)
        dset = self.f.root._f_get_child(path)
        #print "colnames", dset.colnames
        values = []
        indexes = []
        count = 0
        if stop == -1:
            stop = dset.nrows
        for row in dset.where(query, start=start, stop=stop, step=step):
            item = []
            for field in dset.colnames:
                item.append(row[field])
            values.append(item)
            indexes.append(row.nrow)
            count += 1
            #print "count:", count
            if limit and (count == limit):
                #print "break!"
                break  # no more rows for this batch
        rsp = {}
        rsp["indexes"] = indexes
        rsp["values"] = values
        return rsp


    