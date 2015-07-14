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
import sys
sys.path.append('..')
import h5pyd

f = h5pyd.File("committed_type.test.hdfgroup.org", "r", endpoint="http://127.0.0.1:5000")

print "filename,", f.filename
print "name:", f.name
print "uuid:", f.id.uuid
print "id:", f.id.id

type_obj = f['Sensor_Type']

print "type obj uuid:", type_obj.id.uuid
print "type obj name:", type_obj.name
print "dtype:", type_obj.dtype